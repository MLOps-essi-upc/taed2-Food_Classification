## Model Card

## Table of Contents
- [Model Details](#model-details)
    - [Model Description](#model-description)
    - [Model Sources](#model-sources)
- [Uses](#uses)
    - [Direct Use](#direct-use)
    - [Out-of-Scope](#out-of-scope)
- [Bias, Risks, and Limitations](#bias-risks-and-limitations)
    - [Recommendations](#recommendations)
- [How to Get Started with the Model](#how-to-get-started-with-the-model)
- [Training Details](#training-details)
    - [Training Data](#training-data)
    - [Training Procedure](#training-procedure)
        - [Preprocessing](#preprocessing)
        - [Training Hyperparameters](#training-hyperparameters)
        - [Speeds, Sizes, Times](#speeds-sizes-times)
- [Evaluation](#evaluation)
    - [Testing Data, Factors & Metrics](#testing-data-factors-&-metrics)
        - [Testing Data](#testing-data)
        - [Factors](#factors)
        - [Metrics](#metrics)
    - [Results](#results)
        - [Summary](#summary)
- [Environmental Impact](#environmental-impact)

## Model Details

### Model Description
**Residual Network** (a.k.a ResNet) is a convolutional neural network that was proposed in the 2015 paper “Deep Residual Learning for Image Recognition” by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. It was designed to address the limitations of VGG-styled CNNs. In the paper, the authors demonstrated that adding more layers of convolution does not necessarily lead to an increase in validation accuracy; in fact, in most cases, the metrics decrease. In other words, once a certain limit is reached, the model stops improving. As a result, RestNet is different from traditional neural networks in the sense that it takes residuals from each layer and uses them in the subsequent connected layers (similar to residual neural networks used for text prediction).

- **Developed by:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun
- **Model type:** Convolutional Neural Network
- **Language(s) (NLP):** More Information Needed
- **License:** Apache License for TensorFlow, BSD license for PyTorch, etc

Next, there is a architecture image of ResNet34.

![38371XTo6Q](https://github.com/MLOps-essi-upc/taed2-Food_Classification/assets/117642488/28c8d75f-be6a-411c-969d-da4d2fc9cf08)


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
### Recommendations
It is advisable to maintain balanced training data and implement tracking during the model's training to analyze its progression.

## How to Get Started with the Model
In our case, we decided to use ResNet 34 from pytorch (from scratch). The model can be loaded in a very simple way:

`import torch.models`

`model = models.resnet50()`


## Training Details

### Training Data
The model was trained with a reduced version of **Food101** dataset. Initially, it consisted of 101 categories, each with 1000 training samples (images). Nevertheless, due to the lack of resources, we decided to simplify the problem by reducing the number of classes, that is, we preserved only the first 30 categories and samples. In this way, we managed to obtain a derived dataset with only 30,000 images for training.

We took **22,500 images** for the training.

### Training Procedure
The training procedure for the ResNet34 model involved several key stages. A epoch-based approach was employed, where each epoch constitutes a complete iteration through the training dataset. During each epoch, the model adjusted its parameters using the Adam optimizer, which is known for its adaptivity and efficiency in optimizing deep learning models.

For each training step, the model predicted labels for the training samples and then compared these predictions with the actual labels. This discrepancy was measured using a loss function, in this case, cross-entropy loss. Subsequently, the Adam optimizer fine-tuned the model's weights to minimize this loss.

In addition to the training set, a validation set was also utilized to assess the model's performance after each epoch. This provided valuable insights into how well the model was generalizing to previously unseen data.

Throughout the epochs, metrics like accuracy, loss, and possibly other problem-specific metrics were monitored. Consideration was also given to regularization strategies, such as employing techniques like data augmentation to enhance the model's generalization capabilities.

#### Preprocessing
Data augmentation technique was applied, for instance, rotation, contrast, etc.

#### Training Hyperparameters
- Batch_size = 64
- Epochs = 20
- Optimizer = Adam
- Learning Rate = 0.001
- Loss = CrossEntropyLoss
#### Times
It took 2 hours and 56 minutes to train the entire model.

## Evaluation
### Testing Data, Factors & Metrics
#### Testing Data
We set aside a small portion of data in order to test the model with previously unseen images.
#### Factors
The trained model takes a tensor image as input.
#### Metrics
The metric employed to test the model is the **accuracy**, that is, the number of well-predicted images devided with the total number of images.

### Results
The resulting model has 59% of accuracy in training and and 55% in testing.

#### Summary
The model has obtained fairly good results (better than classifiying randomly). Our hypothesis is that since the same dish can have many different appearances, it is really difficult to recognize them, even for humans. By adding more data, or applying transfer learning, the model's invariance can be notably improved.

# Environmental Impact
- **Hardware Type:** GPU from Kaggle (NVIDIA T4 x 2)
- **Hours used:** 2 hours and 56 minutes
- **Cloud Provider:** -
- **Compute Region:** Catalonia
- **Carbon Emitted:** 0.092769kg of CO2
