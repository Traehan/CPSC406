# Homework 1 Solutions

## Question 1: Vending Machine Automaton
# Determine the accepted words for reaching state 25.

accepted_words_vending_machine = [
    "55555",
    "55510",
    "55105",
    "51055",
    "10555",
    "10105"
]

# Any sequence of 5s and 10s summing to 25 is accepted.

---

## Question 2: Turnstile Automaton
# Describe accepted words via a regular expression.

regular_expression_turnstile = r"pay (pay | push pay)*"

# Explanation:
# - "pay" must be the first input to unlock the turnstile.
# - Additional "pay" keeps it unlocked.
# - "push pay" locks and then unlocks, repeating indefinitely.

---

## Question 3: Binary Language Classification
# Determine which words belong to L1, L2, and L3.

binary_language_classification = {
    "10011": {"L1": False, "L2": False, "L3": False},
    "100": {"L1": False, "L2": False, "L3": False},
    "10100100": {"L1": True, "L2": True, "L3": True},
    "1010011100": {"L1": True, "L2": False, "L3": True},
    "11110000": {"L1": False, "L2": True, "L3": True}
}

---

## Question 4: DFA Accepting States
# Determine which words end in the accepting state q1.

dfa_accepting_states = {
    "0010": True,
    "1101": True,
    "1100": False
}

# Words "0010" and "1101" end in q1, while "1100" does not.
