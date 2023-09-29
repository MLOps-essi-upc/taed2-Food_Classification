## Model Card

### ResNet-50
We are going to use a ResNet architecture to handle image classification tasks. To be more specific, we opted to apply a ResNet-50, which comes from Residual Network. It is a convolutional neural network that can be really useful for power computer vision tasks. This type of CNN was proposed in the 2015 paper “Deep Residual Learning for Image Recognition” by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.

#### Model Details
In a summarized manner, ResNet-50 consists of 48 convolutional layers, one MaxPool layer, and one average pool layer. Residual Network takes part in the artificial neural network (ANN) that forms networks by stacking residual blocks.

Technical specifications:
- Developed by: Microsoft Research (Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun)
- Model type: Image classification / feature backbone (Convolutional Neural Network)
- Language(s): -
- License: Apache License for TensorFlow, BSD license for PyTorch, etc.
- Parent Model: ResNet-50 is a variant of the original ResNet architecture
- Papers:
    - ResNet strikes back: An improved training procedure in timm: https://arxiv.org/abs/2110.00476
    - Deep Residual Learning for Image Recognition: https://arxiv.org/abs/1512.03385
    

#### Model Usage
The model can be used for image classification, feature map extraction, image embeddings and among others.

In our project, it will be destinated to learn image classification tasks.

#### Potential limitations
Despite the strengths of the model, it also has limitations, such as complexity, susceptibility to overfitting, and limited interpretability.

#### Training Parameters
- Params (M): 25.6
- GMACs: 4.1
- Activations (M): 11.1


#### Training Data
The dataset we pretend to feed the model is a reduced version of the original one ("Food101"). Initially, it consists of 101 categories, each with 1000 training samples (images). Nevertheless, due to the lack of resources, we decided to simplify the problem by reducing the number of classes, that is, we preserved only the first 30 categories and samples. In this way, we managed to obtain a derived dataset with only 30,000 images for training. Despite this incise, the model is perfectly scalable: if we feed the model with more categories, it will be able to learn from them and recognize more types of food.



#### Evaluation Results



