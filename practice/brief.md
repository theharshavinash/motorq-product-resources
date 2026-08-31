# Practice brief

Pick **one** scenario below and work it the way you would work the data-exploration and one-pager parts of our working session. Use real public datasets; download, explore, and build a one-page recommendation. Give yourself roughly 60 minutes on the data and 15 on the write-up, using whatever tools you like — SQL, spreadsheets, AI, whatever you're fastest in.

The deliverable is a one-page recommendation using [`one-pager-template.md`](one-pager-template.md). There is no answer key and nobody will mark it. The value is in doing it and noticing what you can actually defend. Real data is messier than you expect; decide what to believe before you build an argument on it.

---

## Scenario A — EV charging network

You have joined a company operating a network of public EV charging stations. The VP of Operations asks:

> "Reliability complaints are up and I don't know where to spend. Where is our uptime and revenue actually coming from, and what should we fix first?"

**Real dataset:** [Electric Vehicle Charging Dataset](https://www.kaggle.com/datasets/mexwell/electric-vehicle-charging-dataset) (Kaggle, updated Oct 2024)

Download and explore. Likely columns: charging sessions with timestamps, energy consumed, status (completed/faulted/aborted), station info, connector details.

Your recommendation should identify where uptime and revenue are concentrated, and what the first priority is — sized against the data, not a laundry list.

## Scenario B — Cold-chain logistics

You have joined a logistics firm moving temperature-controlled freight. The Head of Operations asks:

> "We're getting SLA penalties for temperature excursions and the team blames the sensors. Are the excursions real, and if so where are they actually happening?"

**Real dataset:** [Smart Logistics Supply Chain Dataset](https://www.kaggle.com/datasets/ziya07/smart-logistics-supply-chain-dataset) (Kaggle, 2024 data with IoT sensors)

Download and explore. Likely columns: shipments across routes, vehicle assignments, temperature/humidity readings over time, alert/anomaly flags.

Your recommendation should land on whether excursions are real, where they concentrate (route? vehicle? shipper?), and what that implies — sized against the data.

---

See [`README.md`](README.md) for how to approach this exercise and what "no answer key" means.
