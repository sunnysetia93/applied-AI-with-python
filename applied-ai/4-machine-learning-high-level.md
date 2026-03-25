# Lecture 4 — What is Machine Learning at a High Level?

**Date:** 2026-03-25  
**Status:** Done  
**Roadmap lesson:** L04 — What is Machine Learning at a high level?

---

## Objective
Build an intuition for **Machine Learning (ML)** as "learning patterns from data" instead of writing explicit rules, and connect this to real apps you already use.

---

## Core Idea: From Rules → Learning from Data

### Traditional Programming (no ML)
- You write **explicit rules**:
  - If condition X and Y → do Z
- Flow: **Input + Rules → Output**
- Example: spam filter using hand-written rules
  - If subject contains "FREE" and sender domain in [suspicious list] → mark as spam

Here, all intelligence lives in the **rules you wrote by hand**.

### Machine Learning
- You provide **examples**, not rules:
  - Many (input, label) pairs
- Flow to *create* the model:
  - **Data** → Learning algorithm → **Model** (learned pattern)
- Flow to *use* the model:
  - New input + Model → Prediction/decision

> Mental model: **Instead of hardcoding logic, we let the computer *learn* the logic from data.**

---

## The Basic ML Loop (High-Level)

1. **Collect data**
   - Examples: emails, images, transactions, user behavior.

2. **Label/structure it (for many tasks)**
   - Email → spam / not-spam
   - Transaction → fraud / not-fraud
   - Image → cat / dog

3. **Train a model**
   - Algorithm looks at many examples.
   - Adjusts internal parameters to **reduce mistakes**.
   - Output: a **model** that captures patterns in the data.

4. **Evaluate**
   - Test the model on new, unseen examples.
   - Check how well it **generalizes** beyond the training data.

5. **Use in real life (Inference)**
   - A new email arrives → model predicts spam/not-spam.
   - A new transaction happens → model outputs a fraud risk score.

> Training = **learning** from historical data.  
> Inference = **using** the learned model on new inputs.

We did not go into math here; we stayed at the intuition/pipeline level.

---

## Real-World Examples (Student Intuition)

During the session, we used apps Sunny already uses to spot ML in the wild:

### 1. iPhone Face ID
- **Setup:** you scan your face from many angles → this becomes **training data**.
- The device trains/updates a **face recognition model** on-device.
- **Unlock:** when you look at the phone, it runs the model:
  - "Does this face match the learned pattern for Sunny within a threshold?" → allow / deny.
- This is a clear case of **training once, using many times**.

### 2. Swiggy — Restaurant Recommendations
- Likely uses ML to decide **which restaurants to show and in what order**.
- Inputs may include:
  - Your past orders, cuisines, price sensitivity
  - Time of day, location, popularity of restaurants
- Model predicts something like:
  - "How likely is Sunny to order from this restaurant now?"
- Output is a **ranked list** of restaurants personalized to you.

### 3. Instagram — Reels Feed
- Entire Reels experience is heavily ML-driven.
- Inputs:
  - Which reels you watch, how long you watch, what you like, share, save, skip.
  - Scroll speed, replays, etc.
- Model predicts:
  - "What is the probability Sunny will engage with this reel?"
- The feed is sorted by these predicted engagement scores.

### 4. Cred — Detecting Bills/Statements in Email
- Cred likely uses a mix of:
  - **Rules** (known senders/subjects)
  - **ML models** for classification and information extraction:
    - "Is this email a statement/bill?"
    - "What is the due date and amount?"
- Then it can issue reminders like "your credit card bill is due".

Across all these, the **pattern is the same**:
- Use historical examples to **train** a model.
- Then use that model to make decisions on new data, repeatedly.

---

## Key Takeaways from L04

- Machine Learning = **learning patterns from data** instead of writing explicit rules.
- The basic ML loop is: **data → training → model → predictions**.
- "Training" and "inference" are different phases:
  - Training: build/update the model from many examples.
  - Inference: apply the model to new inputs in real time.
- Many everyday products quietly use ML under the hood: Face ID, recommendation feeds, fraud/bill detection, etc.
- L04 sets up the intuition for the **types of learning** (supervised, unsupervised, reinforcement), which we’ll cover next.

---

## Status Update for Next Session
- **Completed today:** L04 — What is Machine Learning at a high level?
- **Next recommended lesson:** L05 — Supervised, unsupervised, and reinforcement learning.
- **Next class plan:** explore the three main categories of ML, with examples of each and how they show up in real products.
