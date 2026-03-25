# Q1: Conditionals

# You’re building a tiny access control for an AI dashboard.

# Rules:

# • If role is "admin", print "Full access".
# • If role is "user", print "Limited access".
# • For anything else, print "No access".

# Write a Python function:

def get_access_message(role):
    if role == "admin":
        return "Full access"
    elif role == "user":
        return "Limited access"
    else:
        return "No access"


print(get_access_message("admin"))
print(get_access_message("user"))
print(get_access_message("guest"))


# Q2: Collections (lists + dicts)

# You’re storing simple model metrics from an experiment:

# • model name: "tiny-llm"
# • accuracy: 0.87
# • latency_ms: 120

# 1. Store this in a Python dict called metrics.
# 2. Add a new key "passed_threshold" that should be True if accuracy >= 0.85, else False.

# Write the code (not in a function, just top-level):

metrics = {
    "model_name": "tiny-llm",
    "accuracy": 0.87,
    "latency_ms": 120,
}

metrics["passed_threshold"] = metrics["accuracy"] >= 0.85

print(metrics["passed_threshold"])


# Q3: Functions + a tiny AI-ish flavor

# You’re scoring model predictions.

# Rules:

# • Input: a list of booleans, predictions_correct, e.g. [True, False, True].
# • You need to compute accuracy = correct_count / total_count.
# • If the list is empty, return 0.0 to avoid a crash.

# Write a function:

# Python

# def compute_accuracy(predictions_correct):
# # your code here
# It should:

# • return a float between 0.0 and 1.0
# • handle the empty list safely

predictions_correct = [True, False, True]

def compute_accuracy(predictions_correct):
    if len(predictions_correct) == 0:
        return 0.0

    return sum(predictions_correct) / len(predictions_correct)

print(compute_accuracy(predictions_correct))
print(compute_accuracy([]))


# Mini Debug Round (common Python mistakes)

# I’ll show a buggy snippet, you tell me what’s wrong (no need to fully fix yet, just describe):
# Q4: What’s the bug here, and what should that line inside the loop be?

scores = [0.8, 0.9, 0.75]

def average_score(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)

print(average_score(scores))