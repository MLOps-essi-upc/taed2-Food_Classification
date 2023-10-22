import os
import torch
from PIL import Image
from torchvision import models
from src import ROOT_DIR
from src.models.predict_model import predict_image
import pytest


# set the working directory
print(ROOT_DIR)