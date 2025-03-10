# Solution to Homework 4
# Traehan Arnold CPSC406

## Step 1: Viewing DFA as an NFA

A DFA is a special case of an NFA where each state has exactly one transition per input. Since NFAs allow multiple transitions but do not require them, any DFA can be viewed as an NFA where each transition set contains at most one state.

## Step 2: Constructing NFA $\mathcal{A}'$ from DFA $\mathcal{A}$

Given the DFA:

- **Start state:** `1`
- **Transitions:**
  - `δ(1, b) = 1`, `δ(1, a) = 2`
  - `δ(2, a) = 2`, `δ(2, b) = 3`
  - `δ(3, a) = 3`, `δ(3, b) = 3` (Final state)

Define the equivalent NFA:

```math
\mathcal{A}' = (Q', \Sigma, \delta': Q' \times \Sigma \to P(Q'), q_0', F')
```

where:

- `Q' = Q = {1,2,3}`
- `Σ = {a, b}`
- `δ'(q, x) = { δ(q, x) }` (Each transition is treated as a singleton set)
- `q_0' = 1`
- `F' = F = {3}`

## Step 3: Justification

Since $\mathcal{A}'$ follows the same transitions as $\mathcal{A}$ but in set notation, it recognizes the same language:

```math
L(\mathcal{A}) = L(\mathcal{A}')
```

Thus, the construction is correct.

# Solutions to Homework 2

## 1. Language Accepted by **A**

The NFA **A** accepts all binary strings that contain at least one occurrence of the substring `00` or reach the accepting state `q3`.

## 2. Specification of **A**

The NFA **A** is defined as:

- **States**: `{q0, q1, q2, q3}`
- **Alphabet**: `{0,1}`
- **Start state**: `q0`
- **Accepting state**: `{q3}`
- **Transition function**:

| Current State | Input `0` | Input `1`  |
|--------------|----------|----------|
| `q0`        | `{q0}`   | `{q0, q1}` |
| `q1`        | `∅`      | `{q2}`   |
| `q2`        | `{q1, q3}` | `∅` |
| `q3`        | `{q3}`   | `{q3}` |

## 3. Extended Transition Function `δ(q0, 10110)`

Step-by-step evaluation:

1. `δ(q0, 1) = {q0, q1}`
2. `δ({q0, q1}, 0) = {q0}`
3. `δ({q0}, 1) = {q0, q1}`
4. `δ({q0, q1}, 1) = {q0, q2}`
5. `δ({q0, q2}, 0) = {q0, q1, q3}`

Final state: `{q0, q1, q3}` (Accepting, since `q3` is in the set).

## 4. Paths for `v = 1100` and `w = 1010`

### For `v = 1100`:

'q0 --1--> {q0, q1} --1--> {q0, q2} --0--> {q0, q1, q3} --0--> {q0, q1, q3}'

Accepting, since `q3` is reached.

### For `w = 1010`:

'q0 --1--> {q0, q1} --0--> {q0} --1--> {q0, q1} --0--> {q0}'

Not accepting, since `q3` is not reached.

## 5. Determinization **Aᴰ** (Power Set Construction)

Using the power set construction, the DFA states are subsets of `{q0, q1, q2, q3}`:

'Qᴰ = { ∅, {q0}, {q0, q1}, {q0, q2}, {q0, q1, q3}, {q3}, ... }'

The transition table is computed by determining transitions for each subset. The accepting states in the DFA are those containing `q3`.
## 6. Minimization of **Aᴰ**

Since `L(A) = L(Aᴰ)`, we minimize the DFA by merging equivalent states.

### Step 1: Identify the states of **Aᴰ**  
The states of the DFA before minimization are:

'{q0}, {q0, q1}, {q0, q2}, {q0, q1, q3}, {q3}'

Observing the transitions, `{q0, q1}` and `{q0, q2}` behave similarly except when processing `1`. However, `{q0, q1, q3}` and `{q3}` are distinguishable because `{q3}` is a trap state.  

By merging states where possible, we obtain a **smaller** DFA with the following minimized states:

'{q0}, {q0, q1}, {q0, q1, q3}, {q3}'

This reduces the number of states while still recognizing the same language.

### Conclusion  
The minimized DFA has fewer states than **Aᴰ** but still accepts the same language. Thus, a smaller DFA **does exist** that recognizes `L(A)`.
