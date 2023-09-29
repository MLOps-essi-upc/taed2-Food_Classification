## Model Card

### ResNet-50
We are going to use a ResNet architecture to handle image classification tasks. To be more specific, we opted to apply a ResNet-50, which comes from Residual Network. It is a convolutional neural network that can be really useful for power computer vision tasks. This type of CNN was proposed in the 2015 paper “Deep Residual Learning for Image Recognition” by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.

#### Model Details
In a summarized manner, ResNet-50 consists of 48 convolutional layers, one MaxPool layer, and one average pool layer. Residual Network takes part of the artificial neural network (ANN) that forms networks by stacking residual blocks.

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
You can use the raw model for image classification, feature map extraction, image embeddings, among others.

In our project, the model will be destined to learn image classification task.


#### Training Parameters
- Params (M): 25.6
- GMACs: 4.1
- Activations (M): 11.1
- Image size: 


#### Evaluation Results



