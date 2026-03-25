# Applied AI Roadmap

A practical, trackable roadmap for learning **Applied AI** from beginner to solid intermediate level.

This document is the shared source of truth for daily learning. We will use it to:
- track progress lesson by lesson
- decide what to study next each day
- note key takeaways and exercises
- build small practical intuition before jumping into advanced systems

---

## How We’ll Use This Roadmap

### Learning style
- **Default pace:** 1 lesson per day
- **After every 5 lessons:** do a recap + mini checkpoint
- **Goal:** understand concepts clearly, then connect them to real products, workflows, and code
- **Approach:** simple explanation -> example -> exercise -> short reflection

### Recommended daily format
For each lesson, we should try to cover:
1. **Concept** — what it is
2. **Why it matters** — where it shows up in real life
3. **Example** — one practical use case
4. **Exercise** — one small question or task
5. **Notes** — any takeaway worth remembering

### Status legend
- `[ ]` Not started
- `[~]` In progress
- `[x]` Done
- `[*]` Needs revision / revisit

---

## Overall Outcomes

By the end of this roadmap, the learner should be able to:
- explain the difference between AI, ML, deep learning, and LLM-based systems
- understand how modern LLM products work at a practical level
- use prompts more effectively and reliably
- work with model APIs and structured outputs
- understand embeddings, retrieval, and RAG
- understand what agents are and when they are useful
- reason about evaluation, hallucinations, reliability, safety, cost, and latency
- think clearly about where AI helps in the real world and where it is mostly hype
- build a strong enough mental model to continue into hands-on applied AI with Python

---

# Phase 0 — Orientation

**Objective:** build the right mindset before the technical details.

## Lessons
- [ ] **L00. What this roadmap covers**
  - Outcome: understand the scope of Applied AI and how we will learn.
  - Exercise: write in 2–3 lines what you want from Applied AI.

- [x] **L01. What “Applied AI” actually means**
  - Outcome: distinguish between AI as research and AI as a practical tool.
  - Exercise: list 3 products or workflows that feel like Applied AI.
  - Notes: Covered on 2026-03-12. Examples discussed included Augment AI, OpenClaw, and n8n as part of practical AI systems/workflows.

- [x] **L02. Where AI is useful vs where it is hype**
  - Outcome: develop early judgment instead of blind excitement.
  - Exercise: categorize 5 AI claims as practical, exaggerated, or unclear.
  - Notes: Covered on 2026-03-13. Discussed a four-question test for evaluating AI claims, useful AI in code reviews, hype patterns like replacing clean forms with chatbots, and high-risk autonomy issues when agents get broad production access without guardrails.

### Phase checkpoint
- Can explain Applied AI in simple language to a beginner.
- Can identify whether an AI use case sounds practical or mostly hype.

---

# Phase 1 — Foundations

**Objective:** understand the core language and mental models behind AI systems.

## Lessons
- [x] **L03. AI vs ML vs Deep Learning**
  - Outcome: know the relationship between the three.
  - Exercise: explain the difference in your own words.
  - Notes: Covered on 2026-03-23. Discussed the hierarchy AI ⊃ ML ⊃ DL, neural network intuition (neurons, layers, deep networks), and when to use classical ML vs Deep Learning based on data type (tabular vs unstructured) and problem shape.

- [x] **L04. What is Machine Learning at a high level?**
  - Outcome: understand “learning from data” without heavy math.
  - Exercise: identify examples of ML in apps you use.
  - Notes: Covered on 2026-03-25. Clarified ML as learning patterns from data instead of hand-written rules, walked through the basic data → training → model → prediction loop, and identified ML-driven behavior in apps like iPhone Face ID, Swiggy recommendations, Instagram Reels ranking, and Cred bill detection.

- [ ] **L05. Supervised, unsupervised, and reinforcement learning**
  - Outcome: know the broad learning categories.
  - Exercise: match example problems to each category.

- [ ] **L06. What is a model?**
  - Outcome: understand a model as a learned pattern system.
  - Exercise: define model, training, and prediction/inference.

- [ ] **L07. Training vs inference**
  - Outcome: understand the difference between building a model and using it.
  - Exercise: describe where ChatGPT fits in this lifecycle.

- [ ] **L08. Classical AI vs modern AI**
  - Outcome: understand rules/symbolic systems vs data-driven learning systems.
  - Exercise: compare a rule-based chatbot and an LLM assistant.

- [ ] **L09. What is an LLM?**
  - Outcome: understand language models at a practical level.
  - Exercise: explain why LLMs feel smart.

- [ ] **L10. Tokens and context windows**
  - Outcome: understand how models read and process text.
  - Exercise: estimate why long conversations can degrade quality.

- [ ] **L11. Parameters, scale, and capability**
  - Outcome: understand why bigger models often perform better, but not always wisely.
  - Exercise: name 2 benefits and 2 tradeoffs of larger models.

- [ ] **L12. Hallucinations and limitations**
  - Outcome: understand why models can sound confident while being wrong.
  - Exercise: write 3 strategies to reduce hallucinations.

### Phase checkpoint
- Can explain the main AI terms without jargon.
- Can explain training vs inference and what an LLM is.
- Can describe why hallucinations happen.

---

# Phase 2 — How LLMs Work in Practice

**Objective:** build practical intuition around modern text-generation systems.

## Lessons
- [ ] **L13. Next-token prediction: the core idea**
  - Outcome: understand the basic mechanism behind LLM text generation.
  - Exercise: explain why predicting “next token” can produce useful answers.

- [ ] **L14. Why LLMs appear intelligent**
  - Outcome: understand emergence, pattern synthesis, and language competence.
  - Exercise: list what feels like intelligence vs what is just pattern completion.

- [ ] **L15. System prompts, user prompts, and assistant behavior**
  - Outcome: understand instruction hierarchy in chat-based systems.
  - Exercise: write a simple system prompt for a tutor.

- [ ] **L16. Temperature, randomness, and determinism**
  - Outcome: understand why outputs vary.
  - Exercise: decide when low vs high temperature is better.

- [ ] **L17. Context management and forgetting**
  - Outcome: understand why older context can be lost or diluted.
  - Exercise: suggest how to improve long conversation quality.

- [ ] **L18. Embeddings: the meaning space intuition**
  - Outcome: understand embeddings conceptually before using them in retrieval.
  - Exercise: explain embeddings without using the word “vector” if possible.

### Phase checkpoint
- Can explain how an LLM generates responses.
- Can explain why outputs vary and why context quality matters.

---

# Phase 3 — Prompting Properly

**Objective:** move from casual usage to deliberate model interaction.

## Lessons
- [ ] **L19. What good prompting actually is**
  - Outcome: understand prompting as instruction design, not magic phrasing.
  - Exercise: improve a vague prompt into a clear one.

- [ ] **L20. Anatomy of a good prompt**
  - Outcome: know how to specify task, context, constraints, and output shape.
  - Exercise: write a prompt with all four parts.

- [ ] **L21. Zero-shot, one-shot, and few-shot prompting**
  - Outcome: know when examples help.
  - Exercise: create a 2-example prompt for classification.

- [ ] **L22. Asking for structured outputs**
  - Outcome: understand how to request predictable output formats.
  - Exercise: rewrite a prompt to return JSON.

- [ ] **L23. Prompting for reasoning vs prompting for format**
  - Outcome: understand task framing differences.
  - Exercise: compare a “think carefully” prompt vs a strict schema prompt.

- [ ] **L24. Prompting mistakes beginners make**
  - Outcome: avoid ambiguity, overload, and missing constraints.
  - Exercise: debug a bad prompt.

- [ ] **L25. Prompt iteration and evaluation mindset**
  - Outcome: learn to test prompts systematically.
  - Exercise: define what “good output” means for one task.

### Phase checkpoint
- Can write better prompts than average users.
- Can ask for structured, constrained responses.
- Can improve prompts through iteration instead of guessing.

---

# Phase 4 — APIs and Building Blocks

**Objective:** understand how AI moves from chat UI to application feature.

## Lessons
- [ ] **L26. From chat app to API**
  - Outcome: understand the difference between using a product and integrating a model.
  - Exercise: describe what an app sends to a model API.

- [ ] **L27. Model providers and ecosystem overview**
  - Outcome: know the role of OpenAI, Anthropic, Google, open-source models, etc.
  - Exercise: compare 3 provider tradeoffs.

- [ ] **L28. Inputs, outputs, and message formats**
  - Outcome: understand common API request/response patterns.
  - Exercise: sketch a simple chat request in plain English.

- [ ] **L29. Structured outputs and JSON schemas**
  - Outcome: understand why production systems prefer machine-readable outputs.
  - Exercise: define a simple schema for a support-ticket classifier.

- [ ] **L30. Tool/function calling**
  - Outcome: understand how models can decide to use tools.
  - Exercise: describe a weather assistant with tool calling.

- [ ] **L31. Streaming responses**
  - Outcome: understand why apps stream text token by token.
  - Exercise: list 3 reasons streaming improves UX.

- [ ] **L32. Cost, tokens, and pricing intuition**
  - Outcome: understand what drives AI costs.
  - Exercise: explain why prompt length matters financially.

- [ ] **L33. Latency and model selection**
  - Outcome: understand quality/speed/cost tradeoffs.
  - Exercise: choose a model profile for chat, extraction, and research.

### Phase checkpoint
- Can explain how an AI app talks to a model.
- Can explain function calling, structured outputs, and cost tradeoffs.

---

# Phase 5 — Retrieval, Knowledge, and RAG

**Objective:** understand how AI systems answer using external knowledge.

## Lessons
- [ ] **L34. Why prompting alone is not enough**
  - Outcome: understand the limits of relying only on model memory.
  - Exercise: list cases where fresh/private data is required.

- [ ] **L35. Embeddings revisited: semantic similarity**
  - Outcome: connect embeddings to retrieval.
  - Exercise: explain semantic search vs keyword search.

- [ ] **L36. What is retrieval?**
  - Outcome: understand fetching relevant information before generation.
  - Exercise: describe retrieval in a company FAQ bot.

- [ ] **L37. What is RAG?**
  - Outcome: understand retrieval-augmented generation as a system pattern.
  - Exercise: define RAG in one paragraph.

- [ ] **L38. Chunking and document preparation**
  - Outcome: understand why document splitting matters.
  - Exercise: suggest a chunking strategy for blog posts.

- [ ] **L39. Ranking and relevance**
  - Outcome: understand that retrieval quality matters as much as generation quality.
  - Exercise: list reasons retrieval might fail.

- [ ] **L40. Grounding and citation behavior**
  - Outcome: understand how systems reduce unsupported answers.
  - Exercise: explain why “answer only from provided context” is useful but imperfect.

- [ ] **L41. RAG failure modes**
  - Outcome: understand bad chunks, missing context, wrong ranking, and overconfident generation.
  - Exercise: identify at least 4 failure modes.

- [ ] **L42. Fine-tuning vs RAG vs prompting**
  - Outcome: understand when each approach fits.
  - Exercise: classify 5 use cases into prompting, RAG, or fine-tuning.

### Phase checkpoint
- Can explain RAG clearly.
- Can explain why retrieval systems fail.
- Can reason about when to use RAG instead of fine-tuning.

---

# Phase 6 — Agents and Workflows

**Objective:** understand automation patterns beyond single prompts.

## Lessons
- [ ] **L43. What an AI agent actually is**
  - Outcome: separate real agents from overhyped marketing claims.
  - Exercise: define an agent in simple terms.

- [ ] **L44. Single-step vs multi-step tasks**
  - Outcome: understand when a workflow is enough and when an agent helps.
  - Exercise: split a complex task into steps.

- [ ] **L45. Planning, acting, and observing**
  - Outcome: understand the loop many agents follow.
  - Exercise: map this loop to a travel assistant.

- [ ] **L46. Tool use in agent systems**
  - Outcome: understand the role of tools, APIs, and external actions.
  - Exercise: design a minimal toolset for a research agent.

- [ ] **L47. Memory and state**
  - Outcome: understand short-term vs long-term memory in AI systems.
  - Exercise: suggest what an assistant should remember across sessions.

- [ ] **L48. Guardrails for agents**
  - Outcome: understand why autonomous systems need limits.
  - Exercise: list 5 guardrails for a business automation agent.

- [ ] **L49. Multi-agent systems**
  - Outcome: understand when multiple specialized agents help and when they are unnecessary complexity.
  - Exercise: describe one sensible multi-agent use case.

### Phase checkpoint
- Can explain what an agent is without hype.
- Can judge whether a task needs a workflow or an agent.
- Can explain why memory, tools, and guardrails matter.

---

# Phase 7 — Real-World Use Cases

**Objective:** connect concepts to practical categories of value creation.

## Lessons
- [ ] **L50. AI for content generation**
  - Outcome: understand strengths and limits for writing, ideation, editing, and repurposing.
  - Exercise: list useful and low-quality content use cases.

- [ ] **L51. AI for coding assistance**
  - Outcome: understand copilots, debugging help, scaffolding, and limitations.
  - Exercise: list 3 coding tasks AI helps with and 3 where human review is critical.

- [ ] **L52. AI for research and synthesis**
  - Outcome: understand summarization, comparison, extraction, and source-grounded workflows.
  - Exercise: design a simple research assistant workflow.

- [ ] **L53. AI for customer support**
  - Outcome: understand support bots, routing, deflection, and escalation.
  - Exercise: list what support bots should and should not do.

- [ ] **L54. AI for internal knowledge assistants**
  - Outcome: understand company-document assistants and their common pitfalls.
  - Exercise: define an internal knowledge assistant for onboarding.

- [ ] **L55. AI for personal productivity**
  - Outcome: understand assistants for note organization, scheduling, summaries, and reminders.
  - Exercise: identify one personal productivity workflow to improve with AI.

- [ ] **L56. AI automations for business workflows**
  - Outcome: understand extraction, classification, triage, and routing systems.
  - Exercise: propose an automation for lead qualification or inbox triage.

### Phase checkpoint
- Can identify where AI delivers real business/user value.
- Can explain the practical shape of common AI products.

---

# Phase 8 — Reliability, Evaluation, and Safety

**Objective:** think like a builder, not just a user.

## Lessons
- [ ] **L57. What does “good output” mean?**
  - Outcome: define quality criteria for an AI feature.
  - Exercise: define success metrics for one use case.

- [ ] **L58. Evaluating AI systems**
  - Outcome: understand manual evals, benchmark tasks, and representative test sets.
  - Exercise: create 5 test cases for a summarization assistant.

- [ ] **L59. Hallucination mitigation strategies**
  - Outcome: understand retrieval, constraints, verification, and human review.
  - Exercise: rank mitigation strategies by usefulness for a chosen app.

- [ ] **L60. Prompt robustness and edge cases**
  - Outcome: understand adversarial input, ambiguity, and weird user behavior.
  - Exercise: invent 5 edge cases for a chatbot.

- [ ] **L61. Privacy and security basics**
  - Outcome: understand data sensitivity, provider trust, and access boundaries.
  - Exercise: explain why some company data should not be sent to public APIs.

- [ ] **L62. Safety and misuse considerations**
  - Outcome: understand harmful outputs, abuse risks, and policy constraints.
  - Exercise: list safeguards for a public-facing assistant.

- [ ] **L63. Human-in-the-loop design**
  - Outcome: understand when humans must approve, review, or intervene.
  - Exercise: choose review gates for a content or support workflow.

### Phase checkpoint
- Can think about evaluation, safety, and privacy like a responsible builder.
- Can explain that “works in demo” is not the same as “works in production.”

---

# Phase 9 — Production and Product Thinking

**Objective:** understand how AI features survive in real products.

## Lessons
- [ ] **L64. Building AI features into real apps**
  - Outcome: understand end-to-end flow from user input to model output to UI.
  - Exercise: sketch the architecture of a simple AI feature.

- [ ] **L65. Monitoring and feedback loops**
  - Outcome: understand how teams improve systems over time.
  - Exercise: list logs/feedback signals worth tracking.

- [ ] **L66. Cost control in production**
  - Outcome: understand prompt trimming, caching, routing, and fallbacks.
  - Exercise: suggest 4 cost-control ideas for a chat app.

- [ ] **L67. Reliability under scale**
  - Outcome: understand retries, fallbacks, partial failures, and degraded modes.
  - Exercise: describe what happens if a model API is slow or down.

- [ ] **L68. Open-source vs closed models**
  - Outcome: understand control, privacy, cost, quality, and ops tradeoffs.
  - Exercise: compare when to prefer each.

- [ ] **L69. The product manager mindset for AI**
  - Outcome: understand user value, trust, UX, and failure handling.
  - Exercise: write the product goal for one AI feature.

### Phase checkpoint
- Can reason about AI features like someone shipping them in production.
- Can discuss tradeoffs rather than only model capability.

---

# Phase 10 — Staying Current Without Drowning

**Objective:** stay informed while avoiding hype addiction.

## Lessons
- [ ] **L70. How to evaluate new model launches**
  - Outcome: know how to compare releases beyond marketing.
  - Exercise: define a checklist for judging a new model.

- [ ] **L71. Which AI news matters and which does not**
  - Outcome: develop signal-vs-noise judgment.
  - Exercise: classify sample news items by importance.

- [ ] **L72. Tool ecosystem awareness**
  - Outcome: understand categories like model providers, orchestration, vector DBs, eval tools, agent frameworks, and UI wrappers.
  - Exercise: map 6 tools to the category they belong to.

- [ ] **L73. Building your own point of view**
  - Outcome: move from consuming opinions to forming your own.
  - Exercise: write your current view of where Applied AI is strongest today.

### Phase checkpoint
- Can stay updated intelligently.
- Can evaluate AI news and tools with healthy skepticism.

---

# Review Milestones

These are recommended pause points for revision and mini-projects.

## Milestone A — After Phase 1
- Explain AI/ML/LLMs to a complete beginner.
- Define training, inference, tokens, and hallucination.

## Milestone B — After Phase 3
- Improve bad prompts.
- Write prompts that ask for reliable structured output.

## Milestone C — After Phase 5
- Explain RAG clearly.
- Compare prompting vs RAG vs fine-tuning.

## Milestone D — After Phase 6
- Explain what an agent is and when it is useful.
- Distinguish workflow automation from agent marketing.

## Milestone E — After Phase 8
- Design a simple evaluation approach for an AI feature.
- Explain privacy/safety concerns sensibly.

## Milestone F — End of roadmap
- Be able to discuss Applied AI confidently.
- Be ready to start or deepen practical Python-based implementation work.

---

# Suggested Mini Projects

These are not mandatory yet, but they are good checkpoints.

- [ ] **Mini Project 1: Prompt Improvement Pack**
  - Take 5 vague prompts and improve them.

- [ ] **Mini Project 2: AI Feature Breakdown**
  - Choose one real AI product and break it into inputs, model behavior, retrieval, outputs, and risks.

- [ ] **Mini Project 3: Simple RAG Design**
  - Design a document assistant for a small knowledge base.

- [ ] **Mini Project 4: Agent vs Workflow Analysis**
  - Compare one task solved by prompt, workflow, and agent.

- [ ] **Mini Project 5: Production Readiness Review**
  - Evaluate one AI use case for reliability, privacy, cost, and UX.

---

# Progress Log

Use this section for quick check-ins.

## Current status
- **Current phase:** Phase 1 — Foundations
- **Current lesson:** L05
- **Last completed lesson:** L04
- **Overall status:** In progress

## Daily log
- **Day 1 (2026-03-12):** Completed L01 — What “Applied AI” actually means. Covered the difference between AI research and Applied AI, discussed real-world examples, and captured the student response: Augment AI, OpenClaw, and n8n.
- **Day 2 (2026-03-13):** Completed L02 — Where AI is useful vs where it is hype. Built a simple framework to judge AI claims, discussed real value vs hype patterns, and captured examples around AI code reviews, chatbot-vs-form UX, and the risks of broad autonomous production access.
- **Day 3 (2026-03-23):** Completed L03 — AI vs ML vs Deep Learning. Clarified the hierarchy AI ⊃ ML ⊃ DL, built intuition for neurons/layers/deep networks, and discussed when to use classical ML vs Deep Learning in practical problems.
- **Day 4 (2026-03-25):** Completed L04 — What is Machine Learning at a high level? Defined ML as learning patterns from data instead of hand-written rules, introduced the basic data → training → model → prediction loop, and analyzed ML-driven behavior in iPhone Face ID, Swiggy restaurant ranking, Instagram Reels recommendations, and Cred bill detection.
- **Day 5:** _Pending_

---

# Notes for Future Updates

This roadmap is version 1.

We may later add:
- Python implementation checkpoints
- API coding exercises
- hands-on projects with embeddings and RAG
- practical agent-building patterns
- selected tooling stacks for real development

For now, the focus is clear understanding first, implementation second.

---

# Rule for Daily Study

When continuing from this roadmap on any day:
1. resume from the **current lesson**
2. teach it simply
3. include one real-world example
4. end with one small exercise or reflection question
5. update the progress state after finishing
