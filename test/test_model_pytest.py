# tests/test_model_pytest.py
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model import WineModel

def test_model_training():
    wine_model = WineModel()
    model = wine_model.train()
    assert model is not None

def test_model_accuracy():
    wine_model = WineModel()
    wine_model.train()
    acc = wine_model.evaluate()
    assert acc > 0.7  # baseline accuracy check
