\documentclass{article}
\usepackage{amsmath, amssymb}

\begin{document}

\section*{Solution to Homework 4}

\textbf{Step 1: Viewing DFA as an NFA}

A DFA is a special case of an NFA where each state has exactly one transition per input. Since NFAs allow multiple transitions but do not require them, any DFA can be viewed as an NFA where each transition set contains at most one state.

\textbf{Step 2: Constructing NFA $\mathcal{A}'$ from DFA $\mathcal{A}$}

Given the DFA:
- Start state: $1$
- Transitions:
  - $\delta(1, b) = 1$, $\delta(1, a) = 2$
  - $\delta(2, a) = 2$, $\delta(2, b) = 3$
  - $\delta(3, a) = 3$, $\delta(3, b) = 3$ (Final state)

Define the equivalent NFA:
\[
\mathcal{A}' = (Q', \Sigma, \delta': Q' \times \Sigma \to P(Q'), q_0', F')
\]
where:
- $Q' = Q = \{1,2,3\}$
- $\Sigma = \{a, b\}$
- $\delta'(q, x) = \{ \delta(q, x) \}$ (Each transition is treated as a singleton set)
- $q_0' = 1$
- $F' = F = \{3\}$

\textbf{Step 3: Justification}

Since $\mathcal{A}'$ follows the same transitions as $\mathcal{A}$ but in set notation, it recognizes the same language:
\[
L(\mathcal{A}) = L(\mathcal{A}')
\]
Thus, the construction is correct.

\section*{1. Language Accepted by $\mathcal{A}$}

The NFA $\mathcal{A}$ accepts all binary strings that contain at least one occurrence of the substring ``00'' or end in state $q_3$.

\section*{2. Specification of $\mathcal{A}$}

The NFA $\mathcal{A}$ is defined as:

\[
Q = \{q_0, q_1, q_2, q_3\}, \quad
\Sigma = \{0,1\}, \quad
q_0 = \text{start state}, \quad
F = \{q_3\}
\]

The transition function $\delta$ is:

\[
\begin{array}{c|cc}
    & 0 & 1  \\
\hline
q_0 & \{q_0\} & \{q_0, q_1\}  \\
q_1 & \emptyset & \{q_2\} \\
q_2 & \{q_1, q_3\} & \emptyset \\
q_3 & \{q_3\} & \{q_3\}
\end{array}
\]

\section*{3. Extended Transition Function $\hat{\delta}(q_0, 10110)$}

Step-by-step evaluation:

\[
\begin{aligned}
    \hat{\delta}(q_0, 1) &= \{q_0, q_1\} \\
    \hat{\delta}(\{q_0, q_1\}, 0) &= \{q_0\} \\
    \hat{\delta}(\{q_0\}, 1) &= \{q_0, q_1\} \\
    \hat{\delta}(\{q_0, q_1\}, 1) &= \{q_0, q_2\} \\
    \hat{\delta}(\{q_0, q_2\}, 0) &= \{q_0, q_1, q_3\}
\end{aligned}
\]

Final state: $\{q_0, q_1, q_3\}$ (accepting since $q_3 \in \hat{\delta}(q_0, 10110)$).

\section*{4. Paths for $v = 1100$ and $w = 1010$}

For $v = 1100$:
\[
q_0 \xrightarrow{1} \{q_0, q_1\} \xrightarrow{1} \{q_0, q_2\} \xrightarrow{0} \{q_0, q_1, q_3\} \xrightarrow{0} \{q_0, q_1, q_3\}
\]
Accepting since $q_3$ is reached.

For $w = 1010$:
\[
q_0 \xrightarrow{1} \{q_0, q_1\} \xrightarrow{0} \{q_0\} \xrightarrow{1} \{q_0, q_1\} \xrightarrow{0} \{q_0\}
\]
Not accepting since $q_3$ is not reached.

\section*{5. Determinization $\mathcal{A}^D$}

Using the power set construction, the DFA states are subsets of $\{q_0, q_1, q_2, q_3\}$:

\[
Q^D = \{\emptyset, \{q_0\}, \{q_0, q_1\}, \{q_0, q_2\}, \{q_0, q_1, q_3\}, \{q_3\}, \dots \}
\]

The transition table for $\mathcal{A}^D$ is derived by computing transitions for each subset. The accepting states in the DFA are those containing $q_3$.

\section*{6. Minimization of $\mathcal{A}^D$}

Since $L(\mathcal{A}) = L(\mathcal{A}^D)$, we check if there is a smaller DFA. By merging equivalent states, we can minimize $\mathcal{A}^D$ to a smaller DFA while preserving the language.

\end{document}
