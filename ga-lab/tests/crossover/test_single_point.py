import pytest

from ga_lab.crossover.single_point import SinglePointCrossover


@pytest.fixture
def crossover():
    return SinglePointCrossover


def test_children_have_correct_length(crossover):
    parent1 = [1, 0, 1, 1, 0]
    parent2 = [0, 1, 0, 0, 1]

    child1, child2 = crossover.cross(parent1, parent2)

    assert len(child1) == len(parent1)
    assert len(child2) == len(parent2)


def test_childrent_are_composed_from_parents(crossover):
    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0, 0, 0]

    child1, child2 = crossover.cross(parent1, parent2)
    assert all(g in (0, 1) for g in child1)
    assert all(g in (0, 1) for g in child2)


def test_children_are_complement_of_each_other(crossover):
    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0, 0, 0]

    child1, child2 = crossover.cross(parent1, parent2)

    assert child1 == [1 - g for g in child2]


def test_returns_two_children(crossover):
    parent1 = [1, 0, 1]
    parent2 = [0, 1, 0]

    result = crossover.cross(parent1, parent2)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_parents_are_not_mutated(crossover):
    parent1 = [1, 0, 1, 1, 0]
    parent2 = [0, 1, 0, 0, 1]
    p1_copy = parent1.copy()
    p2_copy = parent2.copy()
    crossover.cross(parent1, parent2)
    assert parent1 == p1_copy
    assert parent2 == p2_copy


def test_validate_raises_on_unequal_length(crossover):
    with pytest.raises(ValueError):
        crossover.cross([1, 0, 1], [0, 1])


def test_validate_passes_on_equal_length(crossover):
    # should not raise
    crossover.cross([1, 0], [0, 1])
