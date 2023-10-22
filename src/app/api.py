"""Main script: it includes our API initialization and (3) endpoints."""
# '/' is the root endpoint.
# '/models' returns the list of available models and their metrics. (Optional: use 'type' to filter the models).
# '/models/{type}' returns the prediction of the model specified in the path parameter.

import pickle
import numpy as np
import os

from PIL import Image
from datetime import datetime
from functools import wraps
from http import HTTPStatus
from typing import List
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from pathlib import Path
from src.app.schemas import FoodClass, ImageUploadPayload
from src.app.food_data import class_id_to_class_name, food_class_info

# Define application
app = FastAPI(
    title="Food Classification API",
    description="This API lets you make predictions on the Food101 dataset using a ResNet-34 model.",
    version="1.0",
)


# Create 2 extra functions: `construct_response()` and `_load_models()`.
# `construct_response()` will be used as a wrapper to return the response in a JSON format.
# `_load_models()` will be used to load all the models found in `models/` directory.



def construct_response(f):
    """Construct a JSON response for an endpoint's results."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs):
        results = f(request, *args, **kwargs)

        # Construct response
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }

        # Add data
        if "data" in results:
            response["data"] = results["data"]

        return response

    return wrap



@app.on_event("startup")
def _load_models():
    # Loads all pickled models found in `MODELS_DIR` and adds them to `models_list`

    # model_paths = [
    #    filename
    #    for filename in MODELS_DIR.iterdir()
    #    if filename.suffix == ".pkl" #and filename.stem.startswith("iris")
    # ]
    # model_paths = [model_dir]

    # for path in model_paths:
    # with open(path, "rb") as file:
    #     model_wrapper = pickle.load(file)
    #     model_wrappers_list.append(model_wrapper)
    
    # Path to the models folder
    path = os.path.dirname(os.path.abspath("__file__"))
    ROOT_DIR = Path(Path(path).resolve())
    MODELS_FOLDER_PATH = Path(ROOT_DIR, "models", "RESNET34")

    resnet34_model = models.resnet34()
    resnet34_model.load_state_dict(torch.load(MODELS_FOLDER_PATH, map_location=torch.device('cpu')))
    ##with open(MODELS_FOLDER_PATH / "RESNET34", "rb") as pickled_model:
        ##resnet34_model = pickle.load(pickled_model)

    return resnet34_model



@app.get("/", tags=["General"])  # path operation decorator
@construct_response
def _index(request: Request):
    """Root endpoint."""

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"message": "Welcome to Food classifier! Please, read the `/docs`!"},
    }

    return response



#@app.post("/predict", tags=["Prediction"])
#@construct_response
def process_uploaded_image(payload: ImageUploadPayload):
    # Access the uploaded image using payload.file
    uploaded_image = payload.file

    # Perform any necessary preprocessing on the uploaded image
    image = Image.open(uploaded_image)

    # To-Do 1: Check dimensions.
    # Resize the input image to (224, 224) dimensions.
    # Retain only the first three channels (R, G, B) using [..., :3].
    # Expands the dimensions by adding an extra dimension at the beginning (converts it to a 4D array).

    preprocess = transforms.Compose([transforms.ToTensor()])
    image = preprocess(image)

    # To-Do 2: Check if normalization is needed (pixel values not in the range of 0 to 1).
    if (torch.min(image) < 0 or torch.max(image) > 1):
        # Normalize the image to the range 0 to 1.
        image = image / 255.0

    # To-Do 3: Convert the data type of the image to float32 if it's not already.
    image = image.float()
    """
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"image": image},
    }"""

    return image



def get_class_name(class_id):
    """Convert a label ID to its corresponding name."""
    if class_id[0].item() in class_id_to_class_name:
        return class_id_to_class_name[class_id[0].item()]
    else:
        return "Unknown"



@app.post("/models/{type}", tags=["Prediction"])
@construct_response
def _predict(request: Request, file: UploadFile):  # Change payload to accept image file
    """Classifies food images based on model type."""

    # Load the image and perform any necessary preprocessing
    image = process_uploaded_image(file)

    # Compute predictions using the model
    image = image.unsqueeze(0) # add batch dimension

    model = _load_models()

    # predict raw outputs
    output = model(image)

    #Compute the softmax to get probabilities
    output = torch.softmax(output, dim=1)  
    probs, idxs = output.topk(1) 
    prediction_name = get_class_name(idxs)

    # Access extra information for the predicted food class
    if prediction_name in food_class_info:
        extra_info = food_class_info[prediction_name]
    else:
        extra_info = {
            "message": "No extra information available for this class."}

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {
            "predicted_class_id": idxs[0].item(),
            "predicted_class": prediction_name,
            "extra_info": extra_info,
        },
    }

    return response