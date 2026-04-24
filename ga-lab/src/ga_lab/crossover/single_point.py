import random

from .base import BaseCrossover


class SinglePointCrossover(BaseCrossover[list]):
    """
    Single-point crossover operator.

    A single cut point is chosen at random along the chromosome length.
    The two offspring are formed by swapping the tails of the two parents at that cut point.

    Example
    -------

    parent1 = [1, 0, 1 | 1, 0]
    parent2 = [0, 1, 0 | 0, 1]

    child1 = [1, 0, 1, 0, 1] (parent1 head + parent2 tail)
    child2 = [0, 1, 0, 1, 0] (parent1 tail + parent2 head)
    """

    def cross(self, parent1: list, parent2: list) -> tuple[list, list]:
        """
        Perform single-point crossover between two parent chromosome

        Parameters
        ----------
        parent1: list
            First parent chromosome
        parent2: list
            Second parent chromosome

        Returns
        -------

        tuple[list, list]
            A pair of offspring chromosomes of child1, child2
        """

        self.validate(parent1, parent2)

        cut = random.randint(1, len(parent1) - 1)

        child1 = parent1[:cut] + parent2[cut:]
        child2 = parent2[:cut] + parent1[cut:]

        return child1, child2
