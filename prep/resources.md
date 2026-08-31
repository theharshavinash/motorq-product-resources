# Preparation resources

These are resources, not a curriculum. They are organised in the order of our interview process, and each area states what it is for. How you use them is up to you — that judgment is itself something we are hiring for. There are no drills here and no week-by-week plan; pick the areas where you are weakest and go deep.

One correction to make early, because it costs candidates the most: almost all free PM prep material is consumer-app content, and our case round uses an operational B2B user (a fleet operations manager). Expect to translate. A framework built for a photo-sharing app needs real surgery before it survives contact with someone whose job is keeping two hundred vehicles moving.

Two other things worth knowing: AI tools are allowed and expected in our working session, and we do not expect any prior knowledge of telematics or automotive. We will give you the domain context. We cannot give you product judgment.

---

## Written product thinking

Three questions on the application form are graded. They ask you to justify a product change, criticise a real product decision, and describe something you built. Generic answers score zero regardless of how well written they are — we are reading for a named user, a mechanism, a metric, and an honest account of the tradeoff you accepted. The objective here is to be able to make an argued product decision in under 200 words.

- Julie Zhuo, The Looking Glass — https://lg.substack.com/
- Lenny's Newsletter, free archive — https://www.lennysnewsletter.com/archive
- Shreyas Doshi's pinned threads on product sense and writing — https://x.com/shreyas

## Product sense with an unfamiliar user

Our case round puts you in front of a fleet operations manager, not a consumer. The gap most candidates arrive with is B2B: separating the user from the buyer, and taking an unglamorous operational workflow seriously. The objective is to be able to frame a problem, name a metric, and cut scope for a user whose job you have never done.

- Exponent's PM question bank and mock interviews — https://www.tryexponent.com/questions?role=pm
- Decode and Conquer (Lewis Lin) — frameworks as scaffolding, not script
- Lenny's Newsletter, search the archive for B2B and enterprise product

## Data judgment

You will get a messy multi-table synthetic dataset and an hour to find what matters in it. Enough SQL or spreadsheet fluency to explore it unaided is table stakes; the real thing we are watching is whether you distrust a number before you present it — mixed units, duplicates, nulls that mean "not applicable" rather than "missing". The objective is to go from raw data to a sized, defensible recommendation without supervision.

- Mode's SQL Tutorial, Basic and Intermediate — https://mode.com/sql-tutorial/
- Kaggle's free Pandas and Data Cleaning micro-courses — https://www.kaggle.com/learn
- Storytelling with Data (Cole Nussbaumer Knaflic), blog is enough — http://www.storytellingwithdata.com/blog

You can practise this end to end against the dataset in [`../practice/`](../practice/).

## Metrics and diagnosis

Finding an insight is half of the working session; knowing which number should move, and being able to reason backwards when a number moves on its own, is the other half. The objective is to be able to define a non-vanity metric and structure a diagnosis out loud.

- Amplitude's North Star Playbook — https://amplitude.com/north-star
- Lenny's Newsletter, search for metric trees and metric drops

## Building with AI

One round asks you to prototype what you would ship. AI tools are good enough now that a working prototype proves very little on its own, so what we score is the reasoning you make visible while building: why this scope, what you cut, where you overrode the model. Fluency in one tool matters far more than familiarity with five. The objective is to get from a one-line brief to a demoable artifact under time pressure while narrating your decisions.

- Pick one and get fast: v0 (https://v0.dev), Lovable (https://lovable.dev), Replit (https://replit.com), Claude (https://claude.ai), Cursor (https://cursor.com)
- Aakash Gupta's vibe coding interview guide — https://www.news.aakashg.com/p/vibe-coding-interview
- Vibe-Coding Won't Save Your Product Sense Interview — https://joshatlas.substack.com/p/vibe-coding-wont-save-your-product

## Technical fluency

Motorq is a data platform: vehicle data arrives from OEMs over APIs and reaches customers as something they can act on. You will not write code in our interviews, but you will be asked to reason about push versus pull, data freshness against cost, what "real-time" actually commits us to, and how to spec something so that support and the customer trust the same number. The objective is to hold a credible tradeoff conversation with a senior engineer.

- Postman's API 101 and learning centre — https://learning.postman.com/
- Designing Data-Intensive Applications (Kleppmann) — chapters 1 and 11 only
- Exponent's technical PM guides — https://www.tryexponent.com/questions?role=pm
- Motorq's own site and blog, plus any primer on connected-vehicle data

## Ownership and judgment under uncertainty

Our final round is past-tense only: decisions made without enough information, times you were wrong, the hardest no you delivered, things you built or ran unasked. Candidates consistently under-prepare this round because it feels unpreparable. The objective is to have real stories with real numbers, told briefly.

- Exponent's behavioural question bank — https://www.tryexponent.com/questions?role=pm
- Radical Candor (Kim Scott), blog and summaries — https://www.radicalcandor.com/blog/

---

Books are listed separately in [`books.md`](books.md). If you are an engineer moving into product, start with [`engineers-to-pm.md`](engineers-to-pm.md). Three video playlists are in [`playlists.md`](playlists.md).
