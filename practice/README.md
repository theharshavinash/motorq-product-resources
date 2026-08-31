# Practice

Almost nobody gives campus candidates a real dataset to practise on. This is ours. It exists so you can rehearse the two hardest parts of our working session — exploring a messy dataset under time pressure, and turning what you find into a one-page recommendation — before you do it live.

## This is not the interview dataset

Read this twice, because it matters. **The data here is not the data you will see in the interview.** It is a different fictional scenario, built to feel like the real exercise without previewing it. **There is no answer key**, here or anywhere. We are not going to publish "the right answer," because in the real round there isn't one — there are defensible recommendations and indefensible ones, and the point of practising is to learn the difference by doing it, not by checking your work against a key.

## How to use it

1. Open [`brief.md`](brief.md) and pick one of the two scenarios.
2. Spend about 60 minutes with the data. Explore it however you like — SQL, a spreadsheet, pandas, an AI tool. Use whatever you are fastest in.
3. Write a one-pager using [`one-pager-template.md`](one-pager-template.md), in about 15 minutes.
4. Then reread your own one-pager and ask the question we will ask: which of these claims can I actually defend, and which did I assert because it was convenient?

The data is deliberately messy. Some numbers in each set should not be trusted at face value, and finding out which is part of the exercise. If your recommendation rests on a number you never sanity-checked, that is exactly the habit this is meant to surface.

## What's here

```
practice/
├── brief.md               the two scenarios and their prompts
├── one-pager-template.md  the exact format we ask for
├── generate_data.py       the committed, seeded generator (stdlib only)
└── data/
    ├── ev-charging/       Scenario A — Voltways
    └── cold-chain/        Scenario B — Frostlink
```

## About the generator

`generate_data.py` is committed so the data is reproducible — a fixed seed produces byte-identical files — and so there is nothing hidden. It needs only the Python standard library; run `python3 generate_data.py` to regenerate. Reading it closely will show you how the data was constructed, including where the messy bits are. That is fine: this is practice. The real interview dataset is a different scenario and its generator is not in your hands.

Everything here is synthetic. There are no real companies, customers, vehicles, OEMs, or prices anywhere in it.
