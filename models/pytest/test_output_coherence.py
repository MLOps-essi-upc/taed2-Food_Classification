import os
import torch
import pytest
from PIL import Image
import torchvision.models as models
from src.models.predict_model import predict_image

# set the working directory
os.chdir(r"C:\Users\wenli\OneDrive\Escritorio\taed2-Food_Classification")


# load the trained model obtained from kaggle
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("models/RESNET34", map_location=torch.device('cpu')))

# select multiples input samples to test the output
@pytest.mark.parametrize(
    "image_path",
    ['models/pytest/test_images/IMG_1.jpg', 'models/pytest/test_images/IMG_2.jpg'],
)

def test_prediction_output(image_path):
    image = Image.open(image_path)
    prob, target = predict_image(image, model=resnet34, topk=1)
    assert(target < 29 and target >= 0)

