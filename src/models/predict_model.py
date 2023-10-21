from typing import Tuple, List
import torch
import torchvision.transforms as transforms

def predict_image(
        image: torch.tensor,
        model: torch.nn.Module,
        topk: int = 1,
        ) -> List[Tuple[str, float]]:
    """
    Predicts the top-k class probabilities and corresponding class
    indices for the input image using the provided model.

    Args:
        image (torch.tensor): The input image tensor.
        model (torch.nn.Module): The PyTorch model forimage classification.
        topk (int, optional): The number of top predictions to return. Defaults to 1.

    Returns:
        List[Tuple[str, float]]: A list of tuples, each containing
        a class label (as a string) and its associated probability.
    """
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
