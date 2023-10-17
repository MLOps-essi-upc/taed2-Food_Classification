import os
import torch
import pytest
from PIL import Image
import torchvision.models as models
from src.models.predict_model import predict_image


# set the working directory
os.chdir("/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification")


# load the trained model obtained from kaggle
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("models/RESNET34", map_location=torch.device('cpu')))

# select multiples input samples to test the output
@pytest.mark.parametrize(
    "image_path, food_id",
    [('data/test/beef_carpaccio/bc1.jpg', 1), ('data/test/beef_carpaccio/bc2.jpg', 1)]
)

def test_model_bias(image_path, food_id):
    image = Image.open(image_path)
    prob, target = predict_image(image, model=resnet34, topk=1)
    assert(target == food_id)