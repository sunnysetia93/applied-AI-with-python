# L05 — Supervised, Unsupervised, and Reinforcement Learning

## 1. The three learning styles in plain English

### Supervised learning
- You give the model examples **with answers (labels)**.
- Goal: learn a mapping from input → output.
- Mental model: "Here are many inputs with the correct outputs; learn to predict the output for new inputs."
- Examples:
  - Spam vs not spam classification for email.
  - Predicting whether a loan will default.
  - Image classification (cat / dog / car).

### Unsupervised learning
- You give the model **only data, no labels**.
- Goal: discover structure or patterns in the data.
- Mental model: "Group or compress the data in a useful way so we can understand it better."
- Examples:
  - Customer segmentation based on behavior.
  - Clustering users by spending patterns.
  - Finding anomalous or unusual events in logs.

### Reinforcement learning (RL)
- An **agent** interacts with an **environment** over time.
- It takes actions, receives **rewards or penalties**, and learns a **policy** (what to do in each situation).
- Goal: maximize long-term reward.
- Examples:
  - Game-playing agents (Atari, Go, Dota).
  - Robotics: teaching a robot to walk or grasp objects.
  - Some recommendation and ad systems tuning decisions over time.

## 2. Choosing the right learning style

A simple decision process:

1. **Do you have labels (answers) for past data?**
   - Yes → start with **supervised learning**.
   - No → consider **unsupervised learning** to understand the structure, or start by labeling a subset.

2. **Is this a sequential decision / control problem?**
   - Many steps over time, actions influence future options and rewards → candidate for **reinforcement learning**.

3. **Do you mainly want insight or exploration rather than prediction?**
   - Understanding groups, patterns, or structure in the data → **unsupervised learning**.


## 3. Example: stock suggestion assistant

Problem: "I am not very good at investing; I want good suggestions for which stocks or funds to look at or buy."

This is essentially a **recommendation problem**. In practice, systems like this often use a mixture of:

1. **Supervised learning (core)**
   - Input: user profile + instrument features (risk tolerance, time horizon, sectors liked/disliked, stock fundamentals, volatility, history of performance for similar users, etc.).
   - Label: did the user **like/buy/hold/profit** from this recommendation?
   - The model learns: "For users like this, which instruments are usually a good fit?"

2. **Unsupervised learning (supporting)**
   - Cluster users into investor types (e.g., conservative income, growth oriented, short-term traders).
   - Cluster instruments (e.g., stable dividend, high-growth tech, cyclicals, etc.).
   - This helps build simple, understandable segments.

3. **Reinforcement learning (advanced)**
   - Decide which recommendations to show and in what order over time.
   - Balance **exploration** (trying new ideas) vs **exploitation** (sticking to what works).

For a practical v1 system, you can usually:
- treat the problem as **supervised learning** (predict "good fit for this user"),
- optionally use **unsupervised clustering** to design reasonable buckets,
- and postpone RL until you actually need dynamic, long-horizon optimization.


## 4. Regression vs classification inside supervised learning

Within supervised learning, there are two core task types:

### Regression
- Output: a **continuous value** (a number on a scale).
- Examples:
  - Predict monthly revenue.
  - Predict house price.
  - Predict expected rent for a 2BHK in a location.
- Questions that sound like: "How much?", "What value?", "How many?" usually map to regression.

### Classification
- Output: a **discrete class/label**.
- Examples:
  - Spam vs not spam.
  - Will default vs will not default.
  - Risk bucket: low / medium / high.
- Questions that sound like: "Which category?", "Which label?" usually map to classification.

In the lesson, we mapped:
- "Predict the expected rent of a 2BHK" → **regression**.
- "Predict whether this loan will default" → **classification**.


## 5. Key takeaways

- Most real-world ML systems can be understood in terms of:
  - supervised vs unsupervised vs reinforcement learning, and
  - regression vs classification inside supervised learning.
- A practical mental model:
  - **Supervised**: you have answers, want predictions.
  - **Unsupervised**: you have data, want structure/insight.
  - **Reinforcement**: you have an agent acting over time, want good long-term behavior.
- For product thinking, stock suggestions and many recommendation problems are best treated as supervised learning first, with unsupervised clustering as a helper, and RL reserved for more advanced ranking/ordering behavior over time.
