import torch
import pytest
from PIL import Image
from prediction.prediction import predict_image
import torchvision.models as models

# load the trained model obtained from kaggle
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("prediction/pytest/RESNET34", map_location=torch.device('cpu')))

# select multiples input samples to test the output
@pytest.mark.parametrize(
    "image_path, food_id",
    [('prediction/test_images/IMG_1.jpg', 26), ('prediction/test_images/IMG_2.jpg', 20)],
)

def test_model_bias(image_path, food_id):
    image = Image.open(image_path)
    prob, target = predict_image(image, model=resnet34, topk=1)

    assert(target == food_id)