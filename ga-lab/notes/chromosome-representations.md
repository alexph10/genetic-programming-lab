# Chromosome Representations

This note summarizes the main chromosome representations used in genetic algorithms while studying *Hands-On Genetic Algorithms with Python* by Eyal Wirsansky.

In genetic algorithms, a chromosome is the encoded form of a candidate solution. Choosing the chromosome representation is one of the most important design decisions in the entire algorithm, because the representation determines how individuals are initialized, how crossover and mutation can be applied, and how solutions are interpreted by the fitness function.

## Core Idea

A chromosome representation should match the structure of the problem being solved.

The book emphasizes that chromosome encoding is chosen according to the parameters passed to the fitness function. Once the encoding is chosen, the crossover and mutation operators must also be chosen so that they are compatible with that representation.

In practice, this means:

- binary encodings are useful for yes/no choices,
- integer encodings are useful for discrete assignments,
- ordered-list encodings are useful for permutations,
- real-coded encodings are useful for continuous optimization.

## Why Representation Matters

A poor chromosome representation can make a problem unnecessarily difficult to solve.

The same genetic algorithm framework may work very differently depending on how the solution is encoded. In particular, some crossover and mutation operators only make sense for certain encodings. For example, ordinary point-based crossover may work for binary strings, but can produce invalid solutions when used on permutations.

For that reason, chromosome design should always come before operator selection.

## Main Representations

| Representation | Structure | Typical Use | Notes |
|----------------|-----------|-------------|-------|
| Binary chromosome | List of 0s and 1s | Selection, inclusion, yes/no decisions | Simple and common for classic GA examples |
| Integer chromosome | List of integers | Discrete categories, assignments, graph coloring | Values usually come from a bounded discrete set |
| Ordered-list chromosome | Permutation of unique values | TSP, routing, sequencing | Validity requires no duplicates and no missing values |
| Real-coded chromosome | List of floating-point numbers | Continuous optimization, parameter tuning | Requires specialized real-valued operators |

## Binary Representation

### Definition
A binary chromosome is a sequence of bits, usually represented as a list of 0s and 1s.

### Typical Uses
- Knapsack 0-1 problems
- Feature inclusion or exclusion
- Boolean decision variables
- Introductory problems such as OneMax

### Strengths
- Simple to generate and manipulate
- Easy to use with standard crossover and mutation operators
- Efficient for yes/no decisions

### Limitations
- Not natural for ordered or continuous problems
- Can be inefficient when trying to encode real numbers
- Precision depends on bit-length if real values are encoded indirectly

### Example
A knapsack chromosome might be:

```text
[1]
```

where each bit indicates whether an item is selected.

## Integer Representation

### Definition
An integer chromosome is a sequence of integers, where each position stores a discrete value from an allowed set.

### Typical Uses
- Discrete parameter settings
- Category assignment
- Graph coloring
- Problems where each variable takes one value from a fixed range

### Strengths
- More expressive than binary when multiple discrete values are needed
- Natural for many constrained combinatorial problems
- Often easy to interpret directly

### Limitations
- Standard binary mutation operators are not always appropriate
- May still produce invalid or low-quality solutions if the value range is not well chosen

### Example
A graph coloring chromosome might be:

```text
[2][3][1]
```

where each integer represents the color assigned to one node.

## Ordered-List Representation

### Definition
An ordered-list chromosome is a permutation of values, where the order itself is the solution.

### Typical Uses
- Traveling salesman problem
- Vehicle routing
- Scheduling and sequencing problems
- Any problem where each element must appear exactly once

### Strengths
- Natural representation for ordering problems
- Preserves direct interpretation of sequence-based solutions
- Avoids the need for indirect decoding

### Limitations
- Standard crossover and mutation can create invalid offspring
- Specialized operators are required to preserve permutations
- Duplicate or missing values make the solution invalid

### Example
A TSP route for five cities might be:

```text
[3][4][2][1]
```

This means the cities are visited in that order.

An invalid chromosome would be:

```text
[2][3][1]
```

because one city is duplicated and another is missing.

## Real-Coded Representation

### Definition
A real-coded chromosome is a list or array of floating-point numbers.

### Typical Uses
- Continuous function optimization
- Engineering parameter search
- Hyperparameter tuning
- Any search space made of real-valued variables

### Strengths
- Natural representation for continuous domains
- Avoids the limitations of binary encodings for real numbers
- Usually simpler and more precise than binary approximation

### Limitations
- Standard binary and integer operators are not suitable
- Requires specialized crossover and mutation operators such as BLX, SBX, or Gaussian mutation

### Example
A chromosome for three real-valued parameters might be:

```text
[1.23, 7.2134, -25.309]
```

## Why Binary Encoding Is Not Ideal for Real Numbers

Historically, genetic algorithms often used binary strings to represent real numbers. The book explains why this is not ideal.

First, the precision of the represented real number depends on the bit-string length chosen in advance. If the string is too short, precision is poor. If it is too long, the representation becomes unnecessarily large.

Second, the significance of bits depends on their location. The most significant bit has much more influence than the least significant bit, which can create imbalance in the search behavior.

For these reasons, arrays of real-valued numbers are generally a better representation for continuous optimization problems.

## Representation and Operators

The chromosome representation determines which crossover and mutation operators are appropriate.

| Representation | Suitable Crossover | Suitable Mutation |
|----------------|-------------------|------------------|
| Binary | Single-point, two-point, k-point, uniform | Flip bit |
| Integer | Two-point, uniform, problem-dependent | Uniform integer mutation |
| Ordered list | Ordered crossover, PMX | Swap, inversion, scramble |
| Real-coded | BLX, SBX | Gaussian mutation |

This is one of the central practical rules in genetic algorithms: operators must fit the representation.

## Genotype and Phenotype

The chromosome is the **genotype**, meaning the encoded candidate solution. The actual interpreted solution is the **phenotype**.

In some problems, the genotype does not map directly and perfectly to the phenotype. The book demonstrates this in the knapsack problem, where a chromosome may mark certain items as selected, but some of them may later be ignored during evaluation because they would violate the weight constraint.

This is called **genotype-to-phenotype mapping**.

## Choosing a Representation

When starting a new problem, a useful decision process is:

1. Identify the actual variables of the solution.
2. Decide whether the variables are binary, discrete, ordered, or continuous.
3. Choose the simplest chromosome representation that matches those variables.
4. Ensure that crossover and mutation operators are compatible with that encoding.
5. If necessary, create a custom representation for the problem.

## Practical Heuristics

- Use binary encoding for yes/no decisions.
- Use integer encoding for discrete assignments.
- Use ordered lists when the order of unique items matters.
- Use real-coded chromosomes for continuous variables.
- If validity is fragile, choose or design operators that preserve it.
- If the representation needs heavy repair after every operation, it is probably not the best representation.

## Study Priority

For this repository, the most useful order for studying representations is:

1. Binary representation
2. Integer representation
3. Ordered-list representation
4. Real-coded representation

This follows the natural progression from simple discrete encodings to specialized permutation and continuous representations.

## Source

Primary reference: Eyal Wirsansky, *Hands-On Genetic Algorithms with Python*.
