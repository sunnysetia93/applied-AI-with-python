# Lecture 3 — AI vs ML vs Deep Learning

**Date:** 2026-03-23  
**Status:** Done  
**Roadmap lesson:** L03 — AI vs ML vs Deep Learning

---

## Objective
Understand the relationship between **AI**, **Machine Learning (ML)**, and **Deep Learning (DL)**, and build an intuition for when to use each.

---

## Core Definitions

### Artificial Intelligence (AI)
The **broad umbrella field** focused on making machines behave intelligently — reasoning, planning, deciding, understanding, perceiving, and acting.

- Includes rule-based systems, search, planning, ML, DL, etc.
- AI is the **goal/field**, not one specific technique.

> Mental model: **AI = the whole universe of building intelligent behavior in machines.**

---

### Machine Learning (ML)
A **subset of AI** where systems **learn patterns from data** instead of us hardcoding rules.

- Input: data (+ often labels)
- Training: algorithm learns a **model** (a set of parameters/patterns)
- Output: the model can **generalize** to new, unseen data

Typical ML tasks:
- Classification (spam vs non-spam, churn vs no-churn)
- Regression (predicting a continuous value, like price or temperature)
- Clustering (grouping similar items)
- Recommendation ("you might also like" suggestions)

> Mental model: **ML = learning patterns from data to make predictions or decisions.**

---

### Deep Learning (DL)
A **subset of ML** that uses **neural networks with multiple layers** ("deep" networks).

Key idea:
- Instead of hand-crafting features yourself, a deep network can **learn useful features automatically** from data, especially unstructured data like images, text, audio, and video.

Deep Learning shines when:
- You have **lots of data**
- The data is **unstructured** (pixels, text, sound)
- Patterns are complex

Examples powered by DL:
- Image classifiers (cats vs dogs)
- Speech recognition
- Machine translation
- Large Language Models (LLMs) like ChatGPT
- Image generation models

> Mental model: **DL = using deep neural networks to learn features + patterns end-to-end.**

---

## Neural Networks, Neurons, and Layers (Intuition)

### Neuron (in a simple feed-forward network)
A **neuron** is a tiny computation unit that:
- Takes input numbers
- Multiplies them by **weights** and adds a **bias**
- Passes the result through an **activation function** (like ReLU or sigmoid)

Mathematically:
- Inputs: \(x_1, x_2, ..., x_n\)
- Weights: \(w_1, w_2, ..., w_n\), bias: \(b\)
- Compute: \(z = w_1x_1 + w_2x_2 + ... + w_nx_n + b\)
- Output: \(a = \text{activation}(z)\)

> Mental model: **Neuron = weighted sum + bias + nonlinearity.**

---

### Layer
A **layer** is a group of neurons that all look at the same input and produce an output vector.

- Input: a vector (e.g., [x1, x2, x3])
- Each neuron has its own weights and bias
- Output: a new vector (e.g., [h1, h2, h3, h4])

In matrix form:
- Output = activation(**W** · input + **b**)

> Mental model: **Layer = a transformation from one vector to another.**

---

### Deep Neural Network
A **deep** neural network stacks multiple layers:

> input → layer1 → layer2 → … → layerN → output

Each layer:
- Takes the previous layer’s outputs as its inputs
- Learns increasingly abstract features (edges → shapes → parts → objects, etc.)

> Mental model: **Deep network = many layers of neurons stacked, each building on the previous.**

---

## Classical ML vs Deep Learning (Workflow Intuition)

### Classical ML Workflow (e.g., spam detection)
1. You collect emails.
2. **You design features** manually, like:
   - number_of_exclamation_marks
   - contains_word("free")
   - email_length
   - sender_domain_reputation
3. You feed these features into ML algorithms such as Logistic Regression, Random Forest, or XGBoost.
4. The model learns a mapping: features → spam / not spam.

You are doing a lot of **feature engineering** yourself.

---

### Deep Learning Workflow (e.g., image classification)
1. You collect labeled images.
2. You feed in **raw-ish inputs** (pixels) into a neural network.
3. The network learns multiple layers of features:
   - early layers: edges, corners
   - middle layers: textures, shapes
   - later layers: high-level concepts (faces, cats, dogs)
4. The network learns both **features** and **the final decision boundary**.

You rely more on the **network** to discover useful features.

---

## When to Use Classical ML vs Deep Learning

### Classical ML (good starting point when):
- Data is **tabular** (CSV-style rows/columns)
- Dataset is small to medium
- You care about simpler models and interpretability
- Features can be reasonably hand-crafted

Examples:
- Loan default prediction
- Customer churn prediction
- Lead scoring
- Basic fraud risk scoring

---

### Deep Learning (good choice when):
- Data is **unstructured** (images, text, audio, video)
- You have significant data and need strong performance
- The patterns are complex and hard to hand-engineer

Examples:
- Cat vs dog image classifier
- Speech-to-text
- Machine translation
- LLM-based assistants and content generation

---

## Student Answers (Concept Check)

Two concept-check questions were answered during the session:

1. **How is ML different from just programming rules?**  
   > ML predicts for new data by learning patterns from an algorithm + dataset (often with labels), instead of us writing explicit rules.

2. **Why is DL especially good for images and text?**  
   > Images and text require learning many complex features; DL uses layers of neurons to automatically learn these features as depth and data increase.

These answers are aligned with the right intuition.

---

## Key Takeaways
- **AI** is the broad field of making machines behave intelligently.
- **ML** is a subset of AI where systems learn patterns from data to make predictions instead of following hand-coded rules.
- **DL** is a subset of ML that uses deep neural networks (multiple layers of neurons) to automatically learn complex features, especially from unstructured data.
- A **neuron** is a simple computation: weighted sum + bias + activation; a **layer** is many neurons; a **deep network** is many layers stacked.
- Practical rule-of-thumb:
  - For **tabular** prediction problems → start with classical ML.
  - For **images, text, audio** and large-scale pattern problems → reach for Deep Learning.

---

## One-Line Summary
**AI is the goal, ML is one family of techniques to reach it by learning from data, and Deep Learning is a powerful subset of ML using deep neural networks that learn complex features automatically.**

---

## Status Update for Next Session
- **Completed today:** L03 — AI vs ML vs Deep Learning
- **Next recommended lesson:** L04 — What is Machine Learning at a high level?
- **Next class plan:** zoom in on ML itself — training data, labels, models, and the basic learning loop without heavy math.