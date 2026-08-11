# ACLE 2026 — My Notes

## What is it?

I wanted to compare:

🇹🇭 **Bangkok** — my what-if idea

🇸🇦 **Jeddah** — what actually happened

The question is:

**Which schedule is more packed?**

---

## What does my Python do?

Both models use:

- Number of matches
- Number of stadiums
- Number of days

Python then works out:

- Matches per stadium
- Matches per day
- A simple busy score

---

## Bangkok Example

**12 matches / 3 stadiums / 8 days**

- 4 matches per stadium
- 1.5 matches per day
- Busy score: **0.500**

---

## Jeddah Example

**12 matches / 2 stadiums / 8 days**

- 6 matches per stadium
- 1.5 matches per day
- Busy score: **0.750**

Jeddah is more packed because the same number of matches is spread across fewer stadiums.

---

## What is the Busy Score?

`Matches ÷ (Stadiums × Days)`

Higher score = **more packed**

Lower score = **less packed**

It does **not** tell me if the pitch will be damaged.

---

## Important

The current numbers are examples.

I need real schedule data before making a final conclusion.

---

## One-Sentence Explanation

> **"I used two simple Python models to compare how packed my Bangkok idea was against the Jeddah schedule."**
