# Lecture 2 — Orientation: Where AI Is Useful vs Where It Is Hype

**Date:** 2026-03-13  
**Status:** Done  
**Roadmap lesson:** L02 — Where AI is useful vs where it is hype

---

## Objective
Develop practical judgment about when AI creates real value and when it is mostly buzzword-driven marketing.

---

## Core Idea
AI is useful when it solves a real problem in a way that is meaningfully better, faster, cheaper, or more scalable than the alternative.

AI is hype when it sounds impressive but does not improve the actual outcome for the user or the business.

A flashy demo is not enough.
A practical AI system should create measurable value.

---

## Four-Question Test for Any AI Claim
When evaluating an AI product or feature, ask:

1. **What exact problem is being solved?**
2. **Is AI actually needed here?**
3. **What measurable improvement does it create?**
4. **What are the failure modes, risks, and costs?**

This helps separate practical utility from marketing language.

---

## Mental Model: Useful AI vs Hype AI

### Useful AI usually:
- saves significant time or effort
- handles messy, unstructured, or ambiguous inputs well
- improves productivity or decision support at scale
- remains useful even if outputs are not perfect every time
- fits naturally into the workflow instead of making it worse

### Hype AI usually:
- is added mainly for branding or investor/demo appeal
- solves no painful or expensive problem
- creates more friction than the non-AI alternative
- breaks badly when wrong
- is expensive relative to the value it provides

---

## Examples Covered

### Clearly useful examples
- email spam filtering
- transcription
- code autocomplete and code review assistance
- support ticket classification
- OCR and document information extraction

### Mostly hype or commonly overhyped examples
- forcing chatbots into structured flows where forms work better
- replacing every human decision with an LLM
- “AI-powered” features that cannot explain any real ROI
- novelty AI features with weak user value

### Unclear / depends-on-execution examples
- AI therapist
- AI interviewer
- AI investment advisor
- AI tutor

These can be helpful in some contexts, but the cost of being wrong can be high, so design quality and guardrails matter a lot.

---

## Strong Group Example 1 — AI in Code Reviews
A practical example raised during discussion was **AI for code reviews**.

Why it is useful:
- catches obvious bugs and missing edge cases
- speeds up the first-pass review process
- reduces reviewer fatigue on repetitive checks
- helps human reviewers focus on architecture, product context, and tradeoffs

Important nuance:
AI works best here as a **review assistant**, not as a complete replacement for human review.

This is a good example of AI reducing friction without taking over the highest-context decision-making.

---

## Strong Group Example 2 — Replacing Forms with Chatbots
A clear hype-pattern example raised during discussion was replacing simple, structured flows with chatbots.

Example discussed:
- a finance company using a chatbot for a home loan application flow instead of a clear form

Why this is often worse:
- users want clarity and progress visibility
- structured information is easier to scan in a form
- correcting errors is easier in a form
- validation is more predictable in a form
- chat makes the process feel smarter but often makes the UX slower and more frustrating

Key takeaway:

**If the task is structured, repeatable, and mainly about collecting clear inputs, a well-designed form often beats a chatbot.**

---

## Risk Lens — When AI Looks Useful but Becomes Dangerous
A strong high-risk example raised during discussion was:

**Giving an AI agent broad codebase access plus production database access with orchestration.**

Why it looks useful:
- the agent can inspect systems deeply
- it can debug faster
- it can automate multiple steps end-to-end
- it can potentially speed up incident response or implementation work

Why it becomes dangerous:
- it may corrupt or delete production data
- it may expose sensitive customer information
- it may run unsafe migrations or commands
- orchestration can chain mistakes into larger incidents
- poor permission design can make a capable system unsafe

Key takeaway:

**AI capability without permission design is a liability.**

Recommended guardrails:
- least-privilege access
- read-only by default
- sandbox/staging-first execution
- approval gates for destructive actions
- detailed audit logs
- rollback paths
- scoped permissions per task

---

## Practical Builder Rule
Use AI where:
- the task is messy, probabilistic, language-heavy, or classification/generation-based
- partial assistance still creates value
- humans can review or correct outputs when needed

Be cautious using AI where:
- errors are expensive
- truthfulness must be highly reliable
- deterministic software already solves the problem cleanly
- the workflow is highly structured and predictable

---

## Student Responses / Discussion Highlights
### Useful
- **AI in code reviews** — helps save time, catches bugs that human reviewers may miss, and improves review efficiency.

### Hype
- **Replacing user-friendly form flows with chatbots** — especially in domains like finance or home-loan applications where structured forms are faster and clearer.

### High-risk use case
- **AI agent with broad codebase + production database access + orchestration** — useful on paper, but potentially dangerous without strict permissions and guardrails.

---

## Key Takeaways
- AI value should be judged by outcomes, not demos.
- Useful AI reduces friction; hype AI often adds friction.
- Structured tasks do not automatically become better when wrapped in a chatbot.
- In high-risk environments, permissions and guardrails matter as much as model capability.
- The right question is not “Can AI do this?” but “Should AI do this, and under what limits?”

---

## One-Line Summary
**Useful AI creates measurable value with acceptable risk; hype AI creates excitement without improving the real user outcome.**

---

## Status Update for Next Session
- **Completed today:** L02 — Where AI is useful vs where it is hype
- **Next recommended lesson:** L03 — AI vs ML vs Deep Learning
- **Next class plan:** move from judgment about AI use cases into the core foundational terminology.
