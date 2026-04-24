from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Chromosome = TypeVar("Chromosome", list, tuple)


class BaseCrossover(ABC, Generic[Chromosome]):
    """
    Abstract base class for all crossover operators.

    Every crossover operator must implement the 'cross' method, which
    accepts two parent chromosomes and returns two offspring.

    Type Parameters
    ---------------

    Chromosome : list | tuple
        The chromosome representation used by the operator
    """

    @abstractmethod
    def cross(
        self, parent1: Chromosome, parent2: Chromosome
    ) -> tuple[Chromosome, Chromosome]:
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

    def validate(self, parent1: Chromosome, parent2: Chromosome) -> None:
        """
        Validate that two parents are compatible for crossover/
        Raises ValueError if parents have different lengths.
        """

        if len(parent1) != len(parent2):
            raise ValueError(
                f"Parents must have equal lengthsGot {len(parent1)} and {len(parent2)}"
            )
