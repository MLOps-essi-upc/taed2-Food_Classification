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
    "image_path",
    ['/data/test/food_test_1/1.jpeg', 'data/test/food_test_1/2.JPG']
)

def test_prediction_output(image_path):
    image = Image.open(image_path)
    prob, target = predict_image(image, model=resnet34, topk=1)
    assert(target < 29 and target >= 0)