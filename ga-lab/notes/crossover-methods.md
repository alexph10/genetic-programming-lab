# Crossover Methods

This note summarizes the main crossover methods studied while learning genetic algorithms from *Hands-On Genetic Algorithms with Python* by Eyal Wirsansky.

The purpose of this document is to organize crossover operators by chromosome representation and practical use case. In genetic algorithms, crossover is not chosen arbitrarily; it must match the structure of the chromosome so that offspring remain meaningful and, when necessary, valid.

## Core Idea

Crossover, also called recombination, combines the genetic information of two parent individuals to produce offspring. In most genetic algorithms, crossover is applied with a relatively high probability. If crossover is not applied, the parent individuals may simply be cloned into the next generation.

The main principle is:

- Binary and simple fixed-length encodings can use standard point-based crossover methods.
- Permutation or ordered-list encodings require specialized operators that preserve validity.
- Real-coded chromosomes require crossover operators designed for continuous parameter spaces.

## Quick Comparison

| Method | Chromosome Type | Main Idea | Typical Use |
|--------|------------------|-----------|-------------|
| Single-point crossover | Binary, simple integer strings | Swap chromosome tails after one cut point | Introductory GA problems, OneMax-style tasks |
| Two-point crossover | Binary, simple integer strings | Swap the middle section between two cut points | General fixed-length string recombination |
| K-point crossover | Binary, simple integer strings | Generalization of multi-cut recombination | More aggressive segment mixing |
| Uniform crossover | Binary, integer strings | Choose each gene independently from either parent | Higher diversity, gene-level mixing |
| Ordered crossover (OX) | Permutations, ordered lists | Preserve relative ordering while filling missing genes | TSP, sequencing, route optimization |
| Partially matched crossover (PMX) | Permutations, ordered lists | Use value mapping to keep valid permutations | Permutation-based combinatorial optimization |
| Blend crossover (BLX) | Real-valued vectors | Sample offspring values from a parent-defined interval | Continuous optimization |
| Simulated binary crossover (SBX) | Real-valued vectors | Create real-valued offspring that mimic binary crossover behavior | Continuous parameter search |

## Single-Point Crossover

### Definition
A single crossover point is selected randomly on both parent chromosomes. All genes to the right of that point are swapped between the two parents.

### Suitable Representation
- Binary chromosomes
- Simple fixed-length integer chromosomes

### Typical Uses
- Introductory genetic algorithm experiments
- Problems where exchanging a suffix still yields a valid chromosome
- OneMax-style examples

### Strengths
- Very simple to understand and implement
- Preserves large contiguous gene segments
- Good first crossover method for learning

### Limitations
- Can be too rigid in some problems
- Not suitable for permutation-based chromosomes
- May provide less diverse recombination than other methods

## Two-Point Crossover

### Definition
Two crossover points are selected randomly. The genes between those two points are swapped between the parents.

### Suitable Representation
- Binary chromosomes
- Simple integer chromosomes

### Typical Uses
- General fixed-length chromosome recombination
- Problems where more flexible exchange than single-point is desired

### Strengths
- More versatile than single-point crossover
- Preserves structure while allowing more mixing
- Often performs well on binary string problems

### Limitations
- Still not valid for ordered-list representations
- Can disrupt useful structures if cut points are poorly placed

## K-Point Crossover

### Definition
A generalization of point-based crossover in which \(k\) crossover points are chosen and multiple chromosome segments are alternated between the parents.

### Suitable Representation
- Binary chromosomes
- Fixed-length integer chromosomes

### Typical Uses
- Experimental comparison with one-point and two-point methods
- Problems that benefit from stronger recombination

### Strengths
- Increases mixing of parental information
- More flexible than one-point and two-point crossover

### Limitations
- Can become disruptive when too many cut points are used
- Still unsuitable for permutation encodings

## Uniform Crossover

### Definition
Each gene in the offspring is chosen independently from either parent, usually with equal probability.

### Suitable Representation
- Binary chromosomes
- Integer-based fixed-length chromosomes

### Typical Uses
- Problems where gene independence matters more than preserving long segments
- Cases where diversity is especially important

### Strengths
- Produces high diversity
- Recombines information at the individual-gene level
- Less biased toward preserving large contiguous blocks

### Limitations
- Can destroy useful gene groupings
- Not valid for permutation-based chromosomes without modification

## Ordered Crossover (OX)

### Definition
Ordered crossover is designed for chromosomes that represent ordered lists. After copying a segment from one parent, the remaining positions are filled using the order of genes from the other parent, skipping duplicates.

### Suitable Representation
- Permutations
- Ordered-list chromosomes

### Typical Uses
- Traveling salesman problem
- Route planning
- Sequencing problems
- Any problem where each item must appear exactly once

### Strengths
- Produces valid offspring for ordered-list problems
- Preserves relative ordering information
- Standard operator for permutation-based optimization

### Limitations
- More complex than point-based crossover
- Only appropriate when chromosome validity depends on unique ordering

## Partially Matched Crossover (PMX)

### Definition
PMX is a permutation-preserving crossover method that swaps a segment between parents and uses a mapping process to resolve duplicates and preserve valid permutations.

### Suitable Representation
- Permutations
- Ordered-list chromosomes

### Typical Uses
- Routing and sequencing problems
- Comparative studies with ordered crossover
- Permutation-based combinatorial optimization

### Strengths
- Maintains valid permutations
- Useful benchmark operator for permutation problems
- Preserves some positional relationships

### Limitations
- More complex to implement than standard crossover
- Can be less intuitive than OX when first learning permutation operators

## Blend Crossover (BLX)

### Definition
For each real-valued gene, offspring values are sampled from an interval determined by the two parent values. The width of the interval is controlled by the parameter \(\alpha\).

### Suitable Representation
- Real-coded chromosomes
- Continuous parameter vectors

### Typical Uses
- Continuous optimization
- Parameter tuning
- Numerical search over real values

### Strengths
- Natural fit for real-valued search spaces
- Can explore both inside and beyond the parental range
- Simple and effective for continuous domains

### Limitations
- Not suitable for binary or permutation encodings
- Behavior depends on the choice of \(\alpha\)

## Simulated Binary Crossover (SBX)

### Definition
SBX is a real-coded crossover operator designed to imitate some properties of binary single-point crossover. It generates offspring around the parents while preserving the parent-offspring average.

### Suitable Representation
- Real-coded chromosomes
- Continuous optimization problems

### Typical Uses
- Function optimization
- Real-valued engineering parameter search
- Evolutionary optimization in continuous spaces

### Strengths
- Well-suited for continuous optimization
- Produces controlled offspring variation
- Distribution index \(\eta\) gives control over similarity to parents

### Limitations
- More mathematically involved than BLX
- Requires parameter tuning for good behavior

## Choosing the Right Crossover

A useful rule is to choose crossover according to chromosome type:

- Use **single-point, two-point, k-point, or uniform crossover** for binary or simple fixed-length chromosomes.
- Use **ordered crossover or PMX** for permutation-based chromosomes.
- Use **BLX or SBX** for real-coded chromosomes.

If a standard crossover operator breaks the meaning or validity of the chromosome, a custom problem-specific crossover method may be required.

## Study Priority

For this repository, the recommended learning order is:

1. Single-point crossover
2. Two-point crossover
3. K-point crossover
4. Uniform crossover
5. Ordered crossover
6. PMX
7. Blend crossover
8. Simulated binary crossover

This order moves from the simplest operators to more specialized ones tied to permutation and continuous optimization problems.

## Source

Primary reference: Eyal Wirsansky, *Hands-On Genetic Algorithms with Python*.