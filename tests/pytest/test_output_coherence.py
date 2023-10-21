"""
Module Name: test_output_coherence.py

This module tests the output of the model for a given input image.
"""

import os

from PIL import Image
from torchvision import models
from src import ROOT_DIR
from tests.pytest.predict_model import predict_image

import torch
import pytest

os.chdir(ROOT_DIR)

# Load the trained model obtained from kaggle
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("models/RESNET34", map_location=torch.device('cpu')))

# Select multiples input samples to test the output
@pytest.mark.parametrize(
    "image_path",
    ['data/test/food_test_1/0.jpg', #'data/test/food_test_1/1.jpg',
     #'data/test/food_test_1/2.jpg', 'data/test/food_test_1/3.jpg',
     #'data/test/food_test_1/4.jpg',
     'data/test/food_test_1/5.jpg',
     #'data/test/food_test_1/6.jpg',
     'data/test/food_test_1/7.jpg',
     'data/test/food_test_1/8.jpg', 'data/test/food_test_1/9.jpg',
     'data/test/food_test_1/10.jpg', 'data/test/food_test_1/11.jpg',
     'data/test/food_test_1/12.jpg', 'data/test/food_test_1/13.jpg',
     'data/test/food_test_1/14.jpg', #'data/test/food_test_1/15.jpg',
     #'data/test/food_test_1/16.jpg',
     'data/test/food_test_1/17.jpg',
     #'data/test/food_test_1/18.jpg', 'data/test/food_test_1/19.jpg',
     'data/test/food_test_1/20.jpg', #'data/test/food_test_1/21.jpg',
     #'data/test/food_test_1/22.jpg',
     'data/test/food_test_1/23.jpg',
     'data/test/food_test_1/24.JPG', 'data/test/food_test_1/25.png',
     #'data/test/food_test_1/26.jpg',
     'data/test/food_test_1/27.jpg',
     'data/test/food_test_1/28.jpg', 'data/test/food_test_1/29.jpg'],
)

def test_prediction_output(image_path):
    """Tests the output of the model for a given input image."""

    image = Image.open(image_path)
    _, target = predict_image(image, model=resnet34, topk=1)
    assert 0 <= target < 29
