# ⚽ ACLE 2026 --- How Busy Is a Tournament Schedule?

> **I planned a holiday, thought I might catch some football, got the
> timing wrong... and somehow ended up with a data project.** 😂

The original plan was simple:

**Holiday in Bangkok + maybe watch some ACLE football = nice bonus.**

Then I checked properly.

Wrong city.

Different tournament setup.

And my arrival was **one day after the final**.

So:

**Holiday:** ✅ Still happening\
**Football:** ❌ Timing fail

But the mistake gave me a better question:

> ## **When many matches are played across only a few stadiums, how busy does each stadium become?**

That's what this project explores.

------------------------------------------------------------------------

![ACLE](./ACLE.png)

------------------------------------------------------------------------

## 🤔 What Am I Looking At?

A football tournament has a limited number of:

**Matches.**

**Stadiums.**

**Days.**

Put many matches into fewer stadiums and the schedule becomes more
packed.

Spread them across more stadiums and the workload may be shared more
evenly.

Simple idea.

But instead of guessing which plan is better:

> **Let's check the numbers.**

------------------------------------------------------------------------

## 📊 What Can We Compare?

For each tournament plan, we can look at:

**⚽ Matches**\
How many games are played?

**🏟️ Stadiums**\
How many venues are being used?

**📅 Days**\
How many days does the tournament have?

**⏱️ Time Between Matches**\
How much time passes before the same stadium is used again?

**📍 Matches Per Stadium**\
How many games does each venue host?

These numbers help us see how tightly the tournament is packed.

------------------------------------------------------------------------

## 🔍 What Can We Analyse?

The project can ask:

**Which stadium hosts the most matches?**

**How evenly are matches shared between stadiums?**

**How much time is there between games at the same venue?**

**Does using more stadiums spread the schedule better?**

**Which plan puts more matches into a shorter period?**

And if suitable pitch-condition data is available:

> **Is a busier match schedule linked to changes in pitch condition?**

That's important.

A busy schedule alone does **not** prove that a pitch will be ruined.

The data has to support that conclusion.

------------------------------------------------------------------------

## 🆚 Bangkok Idea vs Actual Plan

My original idea imagined a different tournament setup in Bangkok.

The actual tournament plan was different.

Instead of saying:

> **"My plan is better."**

This project asks:

> **"What actually changes when we compare the two schedules?"**

Maybe one plan is more packed.

Maybe matches are spread differently.

Maybe the difference isn't as big as expected.

**Let the numbers decide.**

------------------------------------------------------------------------

## 🧮 About the "61%" Number

My earlier version described the Jeddah schedule as **61% busier**.

For this project, that number should not be treated as a fact just
because it appeared in an earlier calculation.

It needs to be clearly defined and checked.

For example:

**What exactly does "busier" mean?**

Matches per stadium?

Matches per stadium per day?

Average time between games?

Something else?

If the calculation gives **61%**, we show how.

If it gives another number, we use the new result.

> **The goal isn't to protect the old answer. The goal is to find the
> right one.**

------------------------------------------------------------------------

## 🛠️ The Simple Analysis

**1. Get the schedule**

Find the matches, dates and stadiums.

**2. Organise the data**

Put everything into a clean list.

**3. Count**

How many matches does each stadium host?

**4. Compare**

Look at how the different plans spread the matches.

**5. Show the results**

Use simple charts or a dashboard.

**6. Explain what we found**

No need to make the result sound more dramatic than it is.

The numbers are enough. 😂

------------------------------------------------------------------------

# 🧠 The Whole Project in One Line

**Holiday plan → Football idea → Timing fail → Check the schedule →
Compare stadium use → Find out what the numbers actually say**

Sometimes a failed plan still gives you something useful.

In this case:

**a football analytics project.**

------------------------------------------------------------------------

# ⚽ The Simple Idea

This project isn't about proving that one city or organiser made a bad
decision.

It's about asking a simple question:

> ## **How does the number of matches, stadiums and days change how busy a football tournament becomes?**

Then using data to answer it.

And yes...

I still missed the football by one day. 😂

------------------------------------------------------------------------

## 🐍 Python Version

Two simple Python files are included:

**Bangkok idea:**\
[View `model_bangkok.py`](./model_bangkok.py)

**Actual schedule:**\
[View `model_jeddah.py`](./model_jeddah.py)

------------------------------------------------------------------------

## ⚠️ Disclaimer

A personal football and data project. Any comparison or result should be
based on the data used in the analysis and should not be treated as an
official assessment of the tournament, stadiums or organisers.

## ✍️ Credits

**Idea & analysis:** Wansaidon\
**Written with:** ChatGPT by OpenAI

------------------------------------------------------------------------

> **I missed the match.**

***At least I got a data project out of it.*** 😂