"""
Module Name: predict_model.py

The predict_model.py module contains a function, predict_image, for making image classification predictions using a RESNET34.
"""


import torch
import torchvision.transforms as transforms
from torchvision.transforms.functional import to_pil_image
from typing import Tuple, List

def predict_image(
        image: torch.tensor, 
        model: torch.nn.Module, 
        topk: int = 1,
        ) -> List[Tuple[str, float]]:
    
    # x = torch_image.to(device) # move image to GPU
    preprocess = transforms.Compose([transforms.ToTensor()])
    torch_image = preprocess(image)

    x = torch_image
    x = x.unsqueeze(0) # add batch dimension
    
    # predict raw outputs
    output = model(x)

    output = torch.softmax(output, dim=1)  #Compute the softmax to get probabilities
    probs, idxs = output.topk(topk)  # Get the top k predicitons
    #return [(labels[i.item()], p.item()*100) for p, i in zip(probs[0], idxs[0])]
    
    return probs[0], idxs[0]