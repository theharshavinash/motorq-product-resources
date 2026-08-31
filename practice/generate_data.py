#!/usr/bin/env python3
"""Generate the practice datasets for the Motorq PM working-session warm-up.

Two independent, fictional scenarios are produced:

  data/ev-charging/   -- "Voltways", a public EV charging network operator
  data/cold-chain/    -- "Frostlink", a temperature-controlled logistics firm

Everything here is synthetic. No real company, customer, OEM, vehicle, or
price appears anywhere. The generator is committed for two reasons: so the
data is reproducible (fixed seed -> identical files), and so you can see there
is nothing magic in it. Reading this script closely will of course show you
how the data was built. That is fine — this is practice, and there is no
answer key to protect. The real interview dataset is a different scenario and
you will not have its generator.

Run:  python3 generate_data.py
Requires only the Python standard library (tested on 3.11).
"""

import csv
import os
import random
from datetime import datetime, timedelta

SEED = 20260420
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def _writer(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"  wrote {len(rows):>5} rows  {os.path.relpath(path, os.path.dirname(OUT))}")


def _ts(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------------------
# Scenario A: Voltways -- EV charging network operator
# ---------------------------------------------------------------------------
def gen_ev_charging(rng):
    print("ev-charging (Voltways):")
    base = os.path.join(OUT, "ev-charging")

    cities = ["Cascade", "Rendon", "Ashfield", "Beloit", "Karnes", "Yorkline"]
    connector_types = ["CCS", "CHAdeMO", "Type2"]
    host_types = ["retail", "workplace", "highway", "municipal"]

    # --- stations ---
    stations = []
    station_rows = []
    # One commissioning batch in 2025-03 uses a connector firmware that will
    # later show a raised fault rate. It is spread across cities so it is not
    # obvious from geography alone.
    for i in range(1, 43):
        sid = f"ST-{i:03d}"
        city = rng.choice(cities)
        host = rng.choice(host_types)
        n_conn = rng.choice([2, 2, 4, 4, 6])
        ctype = rng.choices(connector_types, weights=[6, 2, 3])[0]
        # commissioning dates across 2024-06 .. 2026-02
        comm = datetime(2024, 6, 1) + timedelta(days=rng.randint(0, 610))
        batch = "B-2025-03" if datetime(2025, 3, 1) <= comm <= datetime(2025, 3, 31) else "B-std"
        stations.append(dict(sid=sid, city=city, host=host, n_conn=n_conn,
                             ctype=ctype, comm=comm, batch=batch))
        station_rows.append([sid, city, host, n_conn, ctype, comm.strftime("%Y-%m-%d")])
    _writer(os.path.join(base, "stations.csv"),
            ["station_id", "city", "host_type", "num_connectors",
             "connector_type", "commissioned_date"], station_rows)

    # --- sessions ---
    # Revenue and energy are concentrated in a handful of highway stations.
    # A single station's connector reports energy in watt-hours, not kWh,
    # so a naive SUM(energy_kwh) is inflated by that connector.
    session_rows = []
    seen_ids = set()
    wh_station = "ST-017"          # this station's energy is logged in Wh
    price_per_kwh = 0.32
    sess_counter = 0
    start_window = datetime(2026, 5, 1)
    for day in range(60):          # ~2 months of activity
        d = start_window + timedelta(days=day)
        for st in stations:
            # highway hosts get far more sessions than workplace/municipal
            demand = {"highway": 11, "retail": 5, "workplace": 3, "municipal": 2}[st["host"]]
            if st["comm"] > d:     # not yet commissioned
                continue
            n = max(0, int(rng.gauss(demand, demand * 0.35)))
            for _ in range(n):
                sess_counter += 1
                sid_num = sess_counter
                session_id = f"SE-{sid_num:07d}"
                connector = rng.randint(1, st["n_conn"])
                start = d + timedelta(minutes=rng.randint(0, 1439))
                dur_min = max(6, int(rng.gauss(42, 18)))
                end = start + timedelta(minutes=dur_min)
                kwh = round(max(1.5, rng.gauss(0.55, 0.18) * dur_min), 2)
                # batch B-2025-03 connectors sometimes fault mid-session
                faulted = st["batch"] == "B-2025-03" and rng.random() < 0.11
                status = "faulted" if faulted else (
                    "aborted" if rng.random() < 0.03 else "completed")
                # promo / free sessions: price is blank, meaning $0, NOT missing
                promo = rng.random() < 0.06
                if faulted:
                    kwh = round(kwh * rng.uniform(0.1, 0.5), 2)
                energy_field = kwh
                if st["sid"] == wh_station:
                    energy_field = int(kwh * 1000)   # <-- logged in Wh
                price = "" if promo else round(kwh * price_per_kwh, 2)
                if faulted:
                    price = "" if promo else round(kwh * price_per_kwh, 2)
                session_rows.append([session_id, st["sid"], connector,
                                     _ts(start), _ts(end), energy_field, price, status])
                seen_ids.add(session_id)

    # a small number of duplicated session_ids (double-logged), same values
    dupes = rng.sample(session_rows, k=max(1, len(session_rows) // 900))
    for row in dupes:
        session_rows.append(list(row))
    rng.shuffle(session_rows)
    _writer(os.path.join(base, "sessions.csv"),
            ["session_id", "station_id", "connector_id", "start_time",
             "end_time", "energy_kwh", "price_usd", "status"], session_rows)

    # --- faults ---
    # Fault rate is materially higher on the B-2025-03 commissioning batch,
    # concentrated on one fault_code. resolved_at blank means still open OR
    # auto-cleared without a technician -- it does not mean "data missing".
    fault_codes = ["F-COMM", "F-OVERTEMP", "F-GND", "F-PILOT", "F-METER"]
    fault_rows = []
    fcount = 0
    for st in stations:
        rate = 0.9 if st["batch"] == "B-2025-03" else 0.28
        n_faults = int(rng.gauss(rate * 30, 6))
        for _ in range(max(0, n_faults)):
            fcount += 1
            reported = datetime(2026, 5, 1) + timedelta(minutes=rng.randint(0, 60 * 1440))
            if st["batch"] == "B-2025-03":
                code = rng.choices(fault_codes, weights=[60, 8, 8, 8, 8])[0]
            else:
                code = rng.choice(fault_codes)
            # ~35% left blank (open or auto-cleared)
            if rng.random() < 0.35:
                resolved = ""
            else:
                resolved = _ts(reported + timedelta(hours=rng.randint(1, 96)))
            fault_rows.append([f"FA-{fcount:05d}", st["sid"],
                               rng.randint(1, st["n_conn"]), _ts(reported),
                               code, resolved])
    rng.shuffle(fault_rows)
    _writer(os.path.join(base, "faults.csv"),
            ["fault_id", "station_id", "connector_id", "reported_at",
             "fault_code", "resolved_at"], fault_rows)


# ---------------------------------------------------------------------------
# Scenario B: Frostlink -- cold-chain logistics firm
# ---------------------------------------------------------------------------
def gen_cold_chain(rng):
    print("cold-chain (Frostlink):")
    base = os.path.join(OUT, "cold-chain")

    lanes = [
        ("Portmere", "Hollis"), ("Portmere", "Dunwich"), ("Calvert", "Hollis"),
        ("Calvert", "Redmond"), ("Hollis", "Redmond"), ("Dunwich", "Calvert"),
    ]
    categories = ["frozen", "chilled", "pharma"]
    target_temp = {"frozen": -18, "chilled": 4, "pharma": 5}

    # --- shipments ---
    shipment_rows = []
    shipments = []
    for i in range(1, 321):
        ship = f"SH-{i:05d}"
        origin, dest = rng.choice(lanes)
        cat = rng.choices(categories, weights=[5, 4, 2])[0]
        dispatched = datetime(2026, 6, 1) + timedelta(minutes=rng.randint(0, 90 * 1440))
        transit_h = rng.randint(8, 40)
        # ~8% still in transit: delivered_at blank means in-transit, not missing
        in_transit = rng.random() < 0.08
        delivered = "" if in_transit else _ts(dispatched + timedelta(hours=transit_h))
        status = "in_transit" if in_transit else "delivered"
        shipments.append(dict(ship=ship, origin=origin, dest=dest, cat=cat,
                              dispatched=dispatched, transit_h=transit_h,
                              in_transit=in_transit))
        shipment_rows.append([ship, origin, dest, cat, target_temp[cat],
                              _ts(dispatched), delivered, status])
    _writer(os.path.join(base, "shipments.csv"),
            ["shipment_id", "origin", "destination", "product_category",
             "target_temp_c", "dispatched_at", "delivered_at", "status"],
            shipment_rows)

    # --- legs ---
    # One vehicle batch (VB-207 reefers) runs a miscalibrated sensor that
    # reports in Fahrenheit while the column says Celsius -- excursions on
    # those legs look wildly out of range. Breaches also concentrate on the
    # Portmere->Dunwich lane (a long leg with a known handoff gap).
    leg_rows = []
    legs = []
    vehicles = [f"VH-{n:03d}" for n in range(1, 46)]
    fahrenheit_vehicles = set(rng.sample(vehicles, k=4))   # the VB-207 batch
    leg_counter = 0
    for sh in shipments:
        n_legs = rng.choice([1, 2, 2, 3])
        cursor = sh["dispatched"]
        for seq in range(1, n_legs + 1):
            leg_counter += 1
            leg_id = f"LG-{leg_counter:06d}"
            veh = rng.choice(vehicles)
            leg_h = max(2, sh["transit_h"] // n_legs)
            start = cursor
            end = start + timedelta(hours=leg_h)
            cursor = end
            legs.append(dict(leg_id=leg_id, ship=sh["ship"], seq=seq, veh=veh,
                             start=start, end=end, cat=sh["cat"],
                             origin=sh["origin"], dest=sh["dest"]))
            leg_rows.append([leg_id, sh["ship"], seq, veh, _ts(start), _ts(end)])
    _writer(os.path.join(base, "legs.csv"),
            ["leg_id", "shipment_id", "leg_seq", "vehicle_id",
             "start_time", "end_time"], leg_rows)

    # --- readings ---
    reading_rows = []
    rcount = 0
    for lg in legs:
        target = target_temp[lg["cat"]]
        # sample a reading roughly every ~30 min of the leg
        span_min = int((lg["end"] - lg["start"]).total_seconds() // 60)
        n = max(3, span_min // 30)
        fahrenheit = lg["veh"] in fahrenheit_vehicles
        # breach-prone leg: the long Portmere->Dunwich handoff
        breach_prone = (lg["origin"], lg["dest"]) == ("Portmere", "Dunwich")
        for k in range(n):
            rcount += 1
            t = lg["start"] + timedelta(minutes=k * 30)
            temp = rng.gauss(target, 0.8)
            if breach_prone and rng.random() < 0.18:
                temp += rng.uniform(4, 9)          # real excursion
            if fahrenheit:
                temp = round(temp * 9 / 5 + 32, 1)  # <-- logged in F, labelled C
            else:
                temp = round(temp, 1)
            # ~1.5% sensor dropouts recorded as -999 sentinel, not real temps
            if rng.random() < 0.015:
                temp = -999
            reading_rows.append([f"RD-{rcount:07d}", lg["ship"], lg["leg_id"],
                                 _ts(t), temp])
    _writer(os.path.join(base, "readings.csv"),
            ["reading_id", "shipment_id", "leg_id", "timestamp", "temp_c"],
            reading_rows)


def main():
    rng = random.Random(SEED)
    print(f"Generating practice datasets (seed={SEED}) into {OUT}\n")
    gen_ev_charging(rng)
    gen_cold_chain(rng)
    print("\nDone. These files are synthetic and contain no real Motorq data.")


if __name__ == "__main__":
    main()
