import random


class TwoPointCrossover:
    def validate(self, parent1, parent2):
        if len(parent1) != len(parent2):
            raise ValueError("Parents must have the same length")
        if len(parent1) < 2:
            raise ValueError("Parents must have length at least 2")

    def cross(self, parent1, parent2):
        self.validate(parent1, parent2)

        point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))

        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

        return child1, child2
