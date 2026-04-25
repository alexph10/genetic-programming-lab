import random


class BitFlipMutation:
    def validate(self, chromosome, probability):
        if len(chromosome) == 0:
            raise ValueError("Chromosome must not be empty.")

        if any(gene not in (0, 1) for gene in chromosome):
            raise ValueError("Chromosome must contain only binary genes (0 or 1).")

        if not 0.0 <= probability <= 1.0:
            raise ValueError("Probability must be between 0 and 1.")

    def mutate(self, chromosome, probability):
        self.validate(chromosome, probability)

        mutated = chromosome[:]

        for i in range(len(mutated)):
            if random.random() < probability:
                mutated[i] = 1 - mutated[i]

        return mutated