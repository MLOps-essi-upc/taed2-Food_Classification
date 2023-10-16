## Model Card

## Table of Contents
- [Model Details](#model-details)
    - [Model Description]
    - [Model Sources]
- [Uses]
    - [Direct Use]
    - [Out-of-Scope]
- [Bias, Risks, and Limitations]
    - [Recommendations]
- [How to Get Started with the Model]
- [Training Details]
    - [Training Data]
    - [Training Procedure]
        - [Preprocessing (optional)]
        - [Training Hyperparameters]
        - [Speeds, Sizes, Times]
- [Evaluation]
    - [Testing Data, Factors & Metrics]
        - [Testing Data]
        - [Factors]
        - [Metrics]
    - [Results]
        - [Summary]
- [Environmental Impact]
    - [Hardware Type]
    - [Hours used]
    - [Cloud Provider]
    - [Compute Region]
    - [Carbon Emitted]

## Model Details

### Model Description
**Residual Network** (a.k.a ResNet) is a convolutional neural network that was proposed in the 2015 paper “Deep Residual Learning for Image Recognition” by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. It was designed to address the limitations of VGG-styled CNNs. In the paper, the authors demonstrated that adding more layers of convolution does not necessarily lead to an increase in validation accuracy; in fact, in most cases, the metrics decrease. In other words, once a certain limit is reached, the model stops improving. As a result, RestNet is different from traditional neural networks in the sense that it takes residuals from each layer and uses them in the subsequent connected layers (similar to residual neural networks used for text prediction).

- **Developed by:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun
- **Model type:** Convolutional Neural Network
- **Language(s) (NLP):** More Information Needed
- **License:** Apache License for TensorFlow, BSD license for PyTorch, etc

![637f2e19aecf4c113421b8fa_image](https://github.com/MLOps-essi-upc/taed2-Food_Classification/assets/117642488/7095ab81-a3ff-4976-9518-2902b7edc4c9)

### Model Sources
- **Pytorch:** [https://blog.roboflow.com/custom-resnet34-classification-model/](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet34.html)
- **Paper:** https://www.researchgate.net/publication/348227673_ResNet_34
- **Demo:** https://blog.roboflow.com/custom-resnet34-classification-model/

## Uses
### Direct Use
The model can be used for image classification, feature map extraction, image embeddings and among others.
### Out of Scope Use
The model is not ideal for handling tasks that require **non-image data**. For instance:
- Natural Language Processing (NLP)
- Audio Signal Processing
- Time Series Analysis
- Graph Data Analysis

## Bias, Risks, and Limitations
- **Biases**: If the training data is biased towards a certain class, this may negatively influence the model's performance (especially for underrepresented groups)
- **Risks**: As a deep learning model with a significant number of parameters, ResNet-34 can be prone to overfitting, especially when trained on limited or noisy data.
- **Limitations**: It cannot handle well other types of data (text, recordings, ...). Non-Interpretable Features.
### Recomendations
It is advisable to maintain balanced training data and implement tracking during the model's training to analyze its progression.

## How to Get Started with the Model
In our case, we decided to use ResNet 34 from pytorch. The model is loaded in a very simple way:

import torch.models

model = models.resnet50()

## Training Details

### Training Data
The model was trained with a reduced version of **Food101** dataset. Initially, it consisted of 101 categories, each with 1000 training samples (images). Nevertheless, due to the lack of resources, we decided to simplify the problem by reducing the number of classes, that is, we preserved only the first 30 categories and samples. In this way, we managed to obtain a derived dataset with only 30,000 images for training.

We took **22,500 images** for the training.

### Training Procedure (FALTA)

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing
**Data augmentation** technique was applied, in particuar, we used rotation, contrast, etc.

### Training Hyperparameters
- Batch_size = 64
- Epochs = 20
- Optimizer = Adam
- Loss = CrossEntropyLoss
#### Times
It took 3 hours and 26 minutes to train the entire model.

## Evaluation
### Testing Data, Factors & Metrics
#### Testing Data
As we already mentioned, the reduced version of the dataset was split into training and testing sets. Therefore, **7,500 samples** are designated for testing.
#### Factors (FALTA)

#### Metrics
The metric employed to test the model is the **accuracy**, that is, the number of well-predicted images devided with the total number of images.

### Results
The resulting model has 55% of accuracy.

#### Summary (FALTA)

# Environmental Impact
- **Hardware Type:** GPU from Kaggle (GPU T4 x 2)
- **Hours used:** 3 hours and 26 minutes
- **Cloud Provider:** Kaggle
- **Compute Region:** Catalonia
- **Carbon Emitted:** 0.16253kg of CO2
