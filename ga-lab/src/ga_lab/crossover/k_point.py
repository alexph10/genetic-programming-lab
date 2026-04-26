import random


class KPointCrossover:
    def validate(self, parent1, parent2, k):
        if len(parent1) == 0 or len(parent2) == 0:
            raise ValueError("Parents must not be empty")

        if len(parent1) != len(parent1):
            raise ValueError("Parents must have the same length")

        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be a positive integer")

        if k >= len(parent1):
            raise ValueError("k must be less than the chromosome length")

    def cross(self, parent1, parent2, k):
        self.validate(parent1, parent2, k)

        points = sorted(random.sample(range(1, len(parent1)), k))
        boundaries = [0] + points + [len(parent1)]

        child1 = []
        child2 = []

        for i in range(len(boundaries) - 1):
            start = boundaries[i]
            end = boundaries[i + 1]

            if i % 2 == 0:
                child1.extend(parent1[start:end])
                child2.extend(parent2[start:end])
            else:
                child1.extend(parent2[start:end])
                child2.extend(parent1[start:end])

        return child1, child2
