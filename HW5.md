# DFA Regular Expressions and State Elimination (Exercise 3.2.1)

Given the transition table:

|       | 0   | 1   |
|-------|-----|-----|
| →q₁   | q₂  | q₁  |
| q₂    | q₃  | q₁  |
| *q₃   | q₃  | q₂  |

---

### a) Rᵢⱼ⁽⁰⁾ (Initial regular expressions with no intermediate states)

Let Rᵢⱼ⁽⁰⁾ = 
- the symbol(s) labeling direct transitions from state i to state j,
- ∅ if no direct transition,
- ε if i = j.
R₁₁⁽⁰⁾ = ε R₁₂⁽⁰⁾ = 0 R₁₃⁽⁰⁾ = ∅ R₂₁⁽⁰⁾ = 1 R₂₂⁽⁰⁾ = ε R₂₃⁽⁰⁾ = 0 R₃₁⁽⁰⁾ = ∅ R₃₂⁽⁰⁾ = 1 R₃₃⁽⁰⁾ = 0 | ε

---

### b) Rᵢⱼ⁽¹⁾ (Using state q₁ as intermediate)

Using the formula:
**Rᵢⱼ⁽k⁾ = Rᵢⱼ⁽k−1⁾ | Rᵢₖ⁽k−1⁾ (Rₖₖ⁽k−1⁾)\* Rₖⱼ⁽k−1⁾**

With q₁ as the only intermediate state:
R₁₁⁽¹⁾ = ε | (ε)(ε)*ε = ε R₁₂⁽¹⁾ = 0 | (ε)(ε)0 = 0 R₁₃⁽¹⁾ = ∅ | (ε)(ε)∅ = ∅

R₂₁⁽¹⁾ = 1 | (1)(ε)*ε = 1 R₂₂⁽¹⁾ = ε | (1)(ε)0 = 10 R₂₃⁽¹⁾ = 0 | (1)(ε)∅ = 0

R₃₁⁽¹⁾ = ∅ | (1)(ε)*ε = ∅ R₃₂⁽¹⁾ = 1 | (1)(ε)0 = 1 R₃₃⁽¹⁾ = 0 | (1)(ε)∅ = 0

---

### c) Rᵢⱼ⁽²⁾ (Using q₁ and q₂ as intermediates)

We now add q₂ as an intermediate state:

R₁₁⁽²⁾ = ε | 0(10)*1 R₁₂⁽²⁾ = 0 | 0(10)*10 R₁₃⁽²⁾ = 0(10)*0

R₂₁⁽²⁾ = 1 | 10(10)*1 R₂₂⁽²⁾ = 10(10)*10 | ε R₂₃⁽²⁾ = 0 | 10(10)*0

R₃₁⁽²⁾ = ∅ | 1(10)*1 R₃₂⁽²⁾ = 1 | 1(10)*10 R₃₃⁽²⁾ = 0 | 1(10)*0

---

### d) Regular expression for the language

Start state: q₁  
Final state: q₃

Regular expression is **R₁₃⁽²⁾**, which is:

R = 0(10)*0

---

### e) Transition diagram and state elimination (eliminate q₂)

#### DFA Transition Diagram (simplified):

q₁ --0--> q₂ --0--> q₃ (final) | | 1| |1 v v q₁ <------ q₁ | v q₃ <----0---- q₃ ^ | | | +----1-------+

#### Regular expression (after eliminating q₂):

From q₁ to q₃: (1|01)00(0)

So, final regular expression: R = (1|01)00(0)

---

# DFA Regular Expressions and State Elimination (Exercise 3.2.2)

Given the transition table:

|       | 0   | 1   |
|-------|-----|-----|
| →q₁   | q₂  | q₃  |
| q₂    | q₁  | q₃  |
| *q₃   | q₂  | q₁  |

---

### a) Rᵢⱼ⁽⁰⁾ (Initial regular expressions with no intermediate states)

Let Rᵢⱼ⁽⁰⁾ = 
- the symbol(s) labeling direct transitions from state i to state j,
- ∅ if no direct transition,
- ε if i = j.
R₁₁⁽⁰⁾ = ε R₁₂⁽⁰⁾ = 0 R₁₃⁽⁰⁾ = 1 R₂₁⁽⁰⁾ = 0 R₂₂⁽⁰⁾ = ε R₂₃⁽⁰⁾ = 1 R₃₁⁽⁰⁾ = 1 R₃₂⁽⁰⁾ = 0 R₃₃⁽⁰⁾ = ε

---

### b) Rᵢⱼ⁽¹⁾ (Using q₁ as intermediate)

Apply:  
**Rᵢⱼ⁽¹⁾ = Rᵢⱼ⁽⁰⁾ | Rᵢ₁⁽⁰⁾ (R₁₁⁽⁰⁾)\* R₁ⱼ⁽⁰⁾**

R₁₁⁽¹⁾ = ε | ε·ε·ε = ε R₁₂⁽¹⁾ = 0 | ε·ε·0 = 0 R₁₃⁽¹⁾ = 1 | ε·ε·1 = 1

R₂₁⁽¹⁾ = 0 | 0·ε·ε = 0 R₂₂⁽¹⁾ = ε | 0·ε·0 = ε | 00 R₂₃⁽¹⁾ = 1 | 0·ε·1 = 1 | 01

R₃₁⁽¹⁾ = 1 | 1·ε·ε = 1 R₃₂⁽¹⁾ = 0 | 1·ε·0 = 0 | 10 R₃₃⁽¹⁾ = ε | 1·ε·1 = ε | 11

---

### c) Rᵢⱼ⁽²⁾ (Using q₁ and q₂ as intermediates)

Apply:
**Rᵢⱼ⁽²⁾ = Rᵢⱼ⁽¹⁾ | Rᵢ₂⁽¹⁾ (R₂₂⁽¹⁾)\* R₂ⱼ⁽¹⁾**

R₁₁⁽²⁾ = ε | 0·(ε|00)·0 = ε | 0(ε|00)0 R₁₂⁽²⁾ = 0 | 0·(ε|00)·(ε | 00) = 0 | 0(ε|00)(ε|00) R₁₃⁽²⁾ = 1 | 0·(ε|00)·(1 | 01) = 1 | 0(ε|00)(1|01)

R₂₁⁽²⁾ = 0 | (ε|00)0 R₂₂⁽²⁾ = ε | (ε|00)(ε|00) R₂₃⁽²⁾ = 1 | (ε|00)*(1|01)

R₃₁⁽²⁾ = 1 | (0|10)(ε|00)0 R₃₂⁽²⁾ = 0 | (0|10)(ε|00)(ε|00) R₃₃⁽²⁾ = ε | (0|10)(ε|00)*(1|01)

---

### d) Regular expression for the language

Start state: q₁  
Final state: q₃

So the regular expression is: R = R₁₃⁽²⁾ = 1 | 0(ε|00)*(1|01)

---

### e) Transition diagram and state elimination (eliminate q₂)

#### DFA Transition Diagram: q₁ --0--> q₂ --0--> q₁ | | 1| |1 v v q₃ <------ q₃

#### Eliminate q₂:
Paths through q₂:
- q₁ --0--> q₂ --1--> q₃ → 01
- q₁ --0--> q₂ --0--> q₁ → 00
- q₂ loops: q₂ --0--> q₁ --0--> q₂ → 00 loops

Apply elimination:
- q₁ to q₃: 1 | 0(00)*1
- q₁ to q₁: ε | 0(00)*0

#### Final Regular Expression: R = (1 | 0(00)*1)

---
# DFA Minimization (Exercise 4.4.1)

Given the transition table:

|     | 0   | 1   |
|-----|-----|-----|
| →A  | B   | A   |
| B   | A   | C   |
| C   | D   | B   |
| *D  | D   | A   |
| E   | D   | F   |
| F   | G   | E   |
| G   | F   | G   |
| H   | G   | D   |

---

## a) Table of Distinguishabilities

We construct a lower-triangular table marking distinguishable state pairs.

### Step 1: Mark final vs. non-final states
- Final state: D
- All pairs with one final (D) and one non-final are **marked** (distinguishable)

### Step 2: Fill table and mark by checking transitions
Use implication: if δ(p, x) and δ(q, x) are already marked, then mark (p, q)

We'll show just the result here (✓ = marked/inequivalent, blank = equivalent):

|     | A | B | C | D | E | F | G | H |
|-----|---|---|---|---|---|---|---|---|
| B   | ✓ |   |   |   |   |   |   |   |
| C   | ✓ | ✓ |   |   |   |   |   |   |
| D   | ✓ | ✓ | ✓ |   | ✓ | ✓ | ✓ | ✓ |
| E   | ✓ | ✓ | ✓ | ✓ |   |   |   |   |
| F   | ✓ | ✓ | ✓ | ✓ | ✓ |   |   |   |
| G   | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |   |   |
| H   | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |   |

### Equivalent states (not marked):
- (E, F)
- (F, G)
- (E, G)

We conclude that E, F, and G are equivalent.

---

## b) Construct the minimum-state equivalent DFA

### Step 1: Merge equivalent states

New state groups:
- [E, F, G] → call it `EFG`
- All other states remain unchanged

### Step 2: Create new transition table

| State | 0   | 1   | Accept? |
|-------|-----|-----|---------|
| A     | B   | A   | No      |
| B     | A   | C   | No      |
| C     | D   | B   | No      |
| D     | D   | A   | **Yes** |
| EFG   | EFG | EFG | No      |
| H     | EFG | D   | No      |

- Transitions:
  - EFG on 0:
    - E → D
    - F → G
    - G → F
    - D and F/G collapse → go to EFG
  - EFG on 1:
    - E → F
    - F → E
    - G → G
    - All lead to E, F, or G → stay in EFG

### Final minimized DFA:

| State | 0   | 1   | Accept? |
|-------|-----|-----|---------|
| →A    | B   | A   | No      |
| B     | A   | C   | No      |
| C     | D   | B   | No      |
| D     | D   | A   | **Yes** |
| EFG   | EFG | EFG | No      |
| H     | EFG | D   | No      |

---

### Notes:
- DFA reduced from 8 states → 6 states
- States E, F, G are indistinguishable and safely merged
# DFA Minimization (Exercise 4.4.2)

Given the transition table:

|     | 0   | 1   |
|-----|-----|-----|
| →A  | B   | E   |
| B   | C   | F   |
| *C  | D   | H   |
| D   | E   | I   |
| E   | F   | H   |
| *F  | G   | B   |
| G   | H   | B   |
| H   | I   | C   |
| *I  | A   | E   |

---

## a) Table of Distinguishabilities

### Step 1: Mark pairs of states where one is final and the other is not

Final states: C, F, I

Marked pairs at this step:
- AC, AF, AI
- BC, BF, BI
- DC, DF, DI
- EC, EF, EI
- GC, GF, GI
- HC, HF, HI

### Step 2: Propagate distinguishability

We use implication:  
If (p, q) → δ(p, x) and δ(q, x) already marked ⇒ mark (p, q)

The fully filled table after all propagation (✓ = distinguishable):

|     | A | B | C | D | E | F | G | H | I |
|-----|---|---|---|---|---|---|---|---|---|
| B   | ✓ |   |   |   |   |   |   |   |   |
| C   | ✓ | ✓ |   |   |   |   |   |   |   |
| D   | ✓ | ✓ | ✓ |   |   |   |   |   |   |
| E   | ✓ | ✓ | ✓ | ✓ |   |   |   |   |   |
| F   | ✓ | ✓ | ✓ | ✓ | ✓ |   |   |   |   |
| G   | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |   |   |   |
| H   | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |   |   |
| I   | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |   |

### Equivalent states (not marked):
- (C, F), (C, I), (F, I)

So: C, F, and I are **equivalent**.

---

## b) Construct the Minimum-State Equivalent DFA

### Step 1: Merge equivalent states

New state group:
- [C, F, I] → call it `CFI`

All other states stay as-is.

### Step 2: Create new transition table

| State | 0   | 1   | Accept? |
|-------|-----|-----|---------|
| →A    | B   | E   | No      |
| B     | CFI | CFI | No      |
| CFI   | D   | H   | **Yes** |
| D     | E   | CFI | No      |
| E     | CFI | H   | No      |
| G     | H   | B   | No      |
| H     | CFI | CFI | No      |

Transitions:
- B: 0 → C, 1 → F → now both → CFI
- D: 1 → I → now → CFI
- E: 0 → F → CFI
- H: 0 → I, 1 → C → both → CFI
- CFI: uses C’s transitions: 0 → D, 1 → H

---

### Final Minimized DFA

| State | 0   | 1   | Accept? |
|-------|-----|-----|---------|
| →A    | B   | E   | No      |
| B     | CFI | CFI | No      |
| CFI   | D   | H   | **Yes** |
| D     | E   | CFI | No      |
| E     | CFI | H   | No      |
| G     | H   | B   | No      |
| H     | CFI | CFI | No      |

- DFA minimized from **9 states → 7 states**
- Final states: CFI

---





