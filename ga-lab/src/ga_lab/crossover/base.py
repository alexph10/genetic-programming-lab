from abc import ABC, abstractmethod
from typing import TypeVar

Chromosome = TypeVar("Chromosome")


class BaseCrossover(ABC):
    """
    Abstract base class for all crossover operators.

    Every crossover operator must implement the 'cross' method, which
    accepts two parent chromosomes and returns two offspring.
    """

    @abstractmethod
    def cross(self, parent1: list, parent2: list) -> tuple[list, list]:
        """
        Perform crossover between two parent chromosomes.

        Parameters
        ----------
        parent1: list
            First parent chromosome.
        parent2: list
            Second

        Returns
        -------
        tuple[list, list]
            A pair of offspring chromosomes (child1, child2),
        """
        ...

    def validate(self, parent1: list, parent2: list) -> None:
        """
        Validate that two parents are compatible for crossover/
        Raises ValueError if parents have different lengths.
        """

        if len(parent1) != len(parent2):
            raise ValueError(
                f"Parents must have equal lengthsGot {len(parent1)} and {len(parent2)}"
            )
