import random

import pytest

from ga_lab.mutation.bit_flip import BitFlipMutation
from src.ga_lab.crossover.base import Chromosome


@pytest.fixture
def mutation():
    return BitFlipMutation()


def test_probability_zero_flips_nothing(mutation):
    chromosome = [1, 0, 1, 1, 0]

    mutated = mutation.mutate(chromosome, 0.0)

    assert mutated == chromosome


def test_probability_one_flips_everything(mutation):
    chromosome = [1, 1, 0, 0, 1]
    mutated = mutation.mutate(chromosome, 1.0)

    assert mutated == [0, 0, 1, 1, 0]


def test_original_chromosome_is_not_mutated(mutation):
    chromosome = [1, 1, 0, 0, 1]
    original = chromosome[:]

    mutation.mutate(chromosome, 1.0)

    assert chromosome == original


def test_invalid_probability_raises(mutation):
    chromosome = [1, 0, 1, 1, 0]

    with pytest.raises(ValueError, match="between 0 and 1"):
        mutation.mutate(chromosome, 1.5)

    with pytest.raises(ValueError, match="between 0 and 1"):
        mutation.mutate(chromosome, 1.5)


def test_flips_only_expected_bits(mutation, monkeypatch):
    values = iter([0.2, 0.8, 0.1, 0.9])
    monkeypatch.setattr(random, "random", lambda: next(values))

    chromosome = [1, 0, 1, 0]

    mutated = mutation.mutate(chromosome, 0.5)

    assert mutated == [0, 0, 0, 0]


def test_invalid_chromosomes_values_raise(mutation):
    chromosome = [1, 0, 2, 1, 0]

    with pytest.raises(ValueError, match="binary genes"):
        mutation.mutate(chromosome, 0.5)


def test_empty_chromosome_raises(mutation):
    with pytest.raises(ValueError, match="must not be empty"):
        mutation.mutate([], 0.5)
