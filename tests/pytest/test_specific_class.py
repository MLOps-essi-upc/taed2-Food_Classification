"""This module tests the output of the model for a given input image."""

import os
import torch
from PIL import Image
from torchvision import models
from src import ROOT_DIR
from tests.pytest.predict_model import predict_image
import pytest

# set the working directory
os.chdir(ROOT_DIR)


# load the trained model obtained from kaggle
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("models/RESNET34", map_location=torch.device('cpu')))

TARGET_CLASS = 1

# select multiples input samples to test the output
@pytest.mark.parametrize(
    "image_path, food_id",
    [('data/test/beef_carpaccio/bc1.jpg', TARGET_CLASS),
     ('data/test/beef_carpaccio/bc2.jpg', TARGET_CLASS),
     ('data/test/beef_carpaccio/bc3.jpg', TARGET_CLASS),
     ('data/test/beef_carpaccio/bc4.jpg', TARGET_CLASS),
     ('data/test/beef_carpaccio/bc5.jpg', TARGET_CLASS)],
)

def test_model_bias(image_path, food_id):
    """Tests the output of the model for a given input image."""
    image = Image.open(image_path)
    _, target = predict_image(image, model=resnet34, topk=1)
    assert target == food_id
