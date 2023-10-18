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
    image = Image.open(image_path)
    prob, target = predict_image(image, model=resnet34, topk=1)
    assert(target < 29 and target >= 0)

