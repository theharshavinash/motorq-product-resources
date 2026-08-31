# Practice brief

Pick **one** of the two scenarios below and work it the way you would work the data-exploration and one-pager parts of our working session. Both use the same task shape as the real round; neither is the real dataset. Give yourself roughly 60 minutes on the data and 15 on the write-up, and use whatever tools you like, AI included.

The deliverable is a one-page recommendation, using [`one-pager-template.md`](one-pager-template.md). There is no answer key and nobody will mark it. The value is entirely in doing it — and in noticing what you can and cannot defend when you are done.

A general note that applies to both: the data is deliberately messy. Somewhere in each set are numbers you should not trust at face value. Part of the exercise is deciding what to believe before you build an argument on it.

---

## Scenario A — Voltways (EV charging network)

Voltways operates a network of public EV charging stations across six cities, sited at retail, workplace, highway, and municipal hosts. You have joined as the first PM. The VP of Operations asks you a deliberately open question:

> "Reliability complaints are up and I don't know where to spend. Where is our uptime and revenue actually coming from, and what should we fix first?"

Data in [`data/ev-charging/`](data/ev-charging/):

- `stations.csv` — one row per station: host type, city, connector type, count, commissioning date.
- `sessions.csv` — one row per charging session: energy delivered, price, status, timestamps.
- `faults.csv` — reported connector faults, with a code and a resolution time.

Your one-pager should end on a recommendation of what to fix or invest in first, sized against the data — not a list of everything you noticed.

## Scenario B — Frostlink (cold-chain logistics)

Frostlink moves temperature-controlled freight — frozen, chilled, and pharma — across a handful of lanes, in multi-leg journeys handed between vehicles. You have joined as the first PM. The Head of Operations asks:

> "We're getting SLA penalties for temperature excursions and the team blames the sensors. Are the excursions real, and if so where are they actually happening?"

Data in [`data/cold-chain/`](data/cold-chain/):

- `shipments.csv` — one row per shipment: lane, product category, target temperature, dispatch and delivery times.
- `legs.csv` — the legs each shipment is split into, and the vehicle that ran each.
- `readings.csv` — temperature readings over time, tied to a shipment and leg.

Your one-pager should end on whether the excursions are real and where the problem concentrates — a claim you can stand behind, sized against the data.

---

Both datasets are synthetic and reproducible; see [`README.md`](README.md) for how they were made and what "no answer key" means.
