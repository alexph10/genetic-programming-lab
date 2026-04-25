import random
import pytest


from ga_lab.crossover.two_point import TwoPointCrossover

@pytest.fixture
def crossover():
    return TwoPointCrossover()

def test_returns_two_children(crossover, monkeypatch):
    monkeypatch.setattr(random, "sample", lambda population, k: [1, 4])

    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0 ,0, 0]

    children = crossover.cross(parent1, parent2)

    assert isinstance(children, tuple)
    assert len(children) == 2


def test_children_have_correct_length(crossover, monkeypatch):
    monkeypatch.setattr(random, "sample", lambda population, k: [1, 4])

    parent1 = [1, 2, 3, 4, 5]
    parent2 = [6, 7, 8, 9, 0]

    child1 ,child2 = crossover.cross(parent1, parent2)

    assert len(child1) == len(parent1)
    assert len(child2) == len(parent2)


def test_swaps_middle_segment(crossover, monkeypatch):
    monkeypatch.setattr(random, "sample", lambda population, k: [1, 4])

    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0, 0, 0]

    child1, child2 = crossover.cross(parent1, parent2)


    assert child1 = [1, 0, 0, 0, 1]
    assert child2 = [0, 1, 1, 1, 0]


def test_children_are_composed_from_parents(crossover, monkeypatch):
    monkeypatch.setattr(random, "sample", lambda population, k: [1, 4])

    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0, 0, 0]

    child1, child2 = crossover.cross(parent1, parent2)

    assert all(gene in {0, 1} for gene in child1)
    assert all(gene in {0, 1} for gene in child2)


def test_parents_are_not_mutated(crossover, monkeypatch):
    monkeypatch.setattr(random, "sample", lambda population, k [1, 4])

    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0, 0, 0]


    original_parent1 = parent1[:]
    original_parent2 = parent2[:]

    crossover.cross(parent1, parent2)

    assert parent1 == original_parent1
    assert parent2 == original_parent2

def test_validate_raises_on_unequal_length(crossover):
    with pytest.raises(ValueError, match="same length"):
        crossover.validate([1, 2, 3], [4, 5])

def test_validate_raises_on_too_short(crossover):
    with pytest.raises(ValueError, match= "at least 3"):
        crossover.validate([1, 2], [3, 4])
