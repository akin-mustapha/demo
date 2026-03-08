import logging
import json
import os
import re
from datetime import datetime, UTC
from collections import defaultdict

# --------------------
# Config
# --------------------

DICT_FILE = "state_dictionary.json"
PHRASE_WEIGHT = 3
KEYWORD_WEIGHT = 1
CONFIDENCE_THRESHOLD = 2

# --------------------
# Logging
# --------------------

logging.basicConfig(
    level=logging.INFO,
    filename="info.log",
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s"
)

# --------------------
# NLP utils
# --------------------

def tokenize(text: str) -> list[str]:
    return re.findall(r"\b\w+\b", text.lower())

def lemmatize(token: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if token.endswith(suffix) and len(token) > len(suffix) + 2:
            return token[:-len(suffix)]
    return token

def normalize(text: str) -> list[str]:
    return [lemmatize(t) for t in tokenize(text)]

# --------------------
# Dictionary loading
# --------------------

def load_states() -> dict:
    if not os.path.exists(DICT_FILE):
        raise FileNotFoundError("State dictionary missing.")
    with open(DICT_FILE, "r") as f:
        return json.load(f)

def save_states(states: dict):
    with open(DICT_FILE, "w") as f:
        json.dump(states, f, indent=2)

# --------------------
# State detection
# --------------------

def detect_state(text: str, states: dict) -> tuple[str, dict]:
    scores = defaultdict(int)
    lowered = text.lower()

    for state, data in states.items():
        for phrase in data["phrases"]:
            if phrase in lowered:
                scores[state] += PHRASE_WEIGHT

    tokens = normalize(text)

    for state, data in states.items():
        for token in tokens:
            if token in data["keywords"]:
                scores[state] += KEYWORD_WEIGHT

    if not scores:
        return "DEFAULT", {}

    best_state, best_score = max(scores.items(), key=lambda x: x[1])

    if best_score < CONFIDENCE_THRESHOLD:
        return "DEFAULT", dict(scores)

    return best_state, dict(scores)

# --------------------
# Learning loop
# --------------------

def learn_new_phrase(text: str, states: dict):
    print("\nI’m not sure how to categorize that.")
    choice = input("Should I learn from this? (y/n): ").strip().lower()

    if choice != "y":
        return states

    print("\nWhich state does this best fit?")
    state_list = list(states.keys())

    for i, state in enumerate(state_list, start=1):
        print(f"{i}. {state}")

    selection = input("> ").strip()

    if not selection.isdigit() or not (1 <= int(selection) <= len(state_list)):
        print("No changes made.")
        return states

    chosen_state = state_list[int(selection) - 1]

    states[chosen_state]["phrases"].append(text.lower())

    save_states(states)
    print(f"Got it. I’ll remember this as {chosen_state.lower()}.")

    logging.info(f"Learned new phrase '{text}' → {chosen_state}")

    return states

# --------------------
# Prompts
# --------------------

PROMPTS = {
    "OVERWHELMED": [
        "What is the *one* thing making today feel heavy?"
    ],
    "SCATTERED": [
        "Which task actually matters in the next 30 minutes?"
    ],
    "FOCUSED": [
        "What would make this session a win?"
    ],
    "DEFAULT": [
        "What feels most unfinished right now?"
    ]
}

# --------------------
# Response generation
# --------------------

def generate_response(log: str, states: dict) -> tuple[dict, dict]:
    state, scores = detect_state(log, states)
    prompt = PROMPTS[state][0]

    response = {
        "timestamp": datetime.now(UTC).isoformat(),
        "state": state,
        "scores": scores,
        "reflection": (
            f"It sounds like you're feeling {state.lower().replace('_', ' ')}."
            if state != "DEFAULT"
            else "Thanks for writing that out."
        ),
        "prompt": prompt
    }

    return response, scores

# --------------------
# CLI
# --------------------

def main():
    states = load_states()

    print("Rapid Log (type and press enter):")
    user_input = input("> ")

    logging.info(f"User input: {user_input}")

    response, scores = generate_response(user_input, states)

    print("\n---")
    print(response["reflection"])
    print(response["prompt"])

    if response["state"] == "DEFAULT":
        states = learn_new_phrase(user_input, states)

if __name__ == "__main__":
    main()