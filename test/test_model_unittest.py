# tests/test_model_unittest.py
import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model import WineModel

class TestWineModel(unittest.TestCase):

    def test_training(self):
        wine_model = WineModel()
        model = wine_model.train()
        self.assertIsNotNone(model)

    def test_accuracy(self):
        wine_model = WineModel()
        wine_model.train()
        acc = wine_model.evaluate()
        self.assertTrue(acc > 0.7)

if __name__ == "__main__":
    unittest.main()
