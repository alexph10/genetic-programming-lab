import random
import unittest

from src.ga_lab.crossover.k_point import KPointCrossover


class TestKPointCrossover(unittest.TestCase):
    def setUp(self):
        self.crossover = KPointCrossover()
        self.parent1 = [1, 1, 1, 1, 1, 1]
        self.parent2 = [0, 0, 0, 0, 0, 0]

    def test_children_have_same_length_as_parents(self):
        random.seed(42)
        child1, child2 = self.crossover.cross(self.parent1, self.parent2, k=2)

        self.assertEqual(len(child1), len(self.parent1))
        self.assertEqual(len(child2), len(self.parent2))

    def test_children_only_contain_genes_from_parents(self):
        random.seed(42)
        child1, child2 = self.crossover.cross(self.parent1, self.parent2, k=2)

        for gene in child1:
            self.assertIn(gene, {0, 1})

        for gene in child2:
            self.assertIn(gene, {0, 1})

    def test_identical_parents_produce_identical_children(self):
        random.seed(42)

        parent = [5, 5, 5, 5, 5, 5]

        child1, child2 = self.crossover.cross(parent, parent, k=3)

        self.assertEqual(child1, child2)
        self.assertEqual(child2, parent)

    def test_k_one_still_work(self):
        random.seed(42)
        child1, child2 = self.crossover.cross(self.parent1, self.parent2, k=1)

        self.assertEqual(len(child1), len(self.parent1))
        self.assertEqual(len(child2), len(self.parent2))

    def test_asymmetrical_segments_still_valid(self):
        random.seed(7)
        parent1 = [1] * 10
        parent2 = [0] * 10

        child1, child2 = self.crossover.cross(parent1, parent2, k=3)

        self.assertEqual(len(child1), 10)
        self.assertEqual(len(child2), 10)

        self.assertTrue(all(gene in {0, 1} for gene in child1))
        self.assertTrue(all(gene in {0, 1} for gene in child2))

    def test_invalid_k_zero_raises(self):
        with self.assertRaises(ValueError):
            self.crossover.cross(self.parent1, self.parent2, k=0)

    def test_invalid_k_too_large_raises(self):
        with self.assertRaises(ValueError):
            self.crossover.cross(self.parent1, self.parent2, k=len(self.parent1))

    def test_different_parent_lengths_raise(self):
        with self.assertRaises(ValueError):
            self.crossover.cross([1, 1, 1], [0, 0], k=1)


if __name__ == "__main__":
    unittest.main()
