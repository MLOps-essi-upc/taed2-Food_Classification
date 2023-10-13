import torch
from prediction import predict_image
import torchvision.models as models
from PIL import Image

# load the trained model obtained from kaggle
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("RESNET50", map_location=torch.device('cpu')))

# select multiples input samples to test the output
@pytest.mark.parametrize(
    [
        (Image.open('test_images\IMG_1.jpg')),
    ],
)

def test_prediction_output(image):
    prob, target = predict_image(image, model=resnet34, topk=1)
    assert(target < 29 and target >= 0)



