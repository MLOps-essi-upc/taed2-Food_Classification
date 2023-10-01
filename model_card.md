## Model Card

### ResNet-50
We are going to use a ResNet architecture to handle image classification tasks. To be more specific, we opted to apply a ResNet-50, which comes from Residual Network. It is a convolutional neural network that can be really useful for power computer vision tasks. This type of CNN was proposed in the 2015 paper “Deep Residual Learning for Image Recognition” by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.

ResNet was designed to address the limitations of VGG-styled CNNs. In their paper, the authors demonstrated that adding more layers of convolution does not necessarily lead to an increase in validation accuracy; in fact, in most cases, the metrics decrease. In other words, once a certain limit is reached, the model stops improving. This is why they introduced "skip connections" as a solution proposal.


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
ResNet has achieved state-of-the-art results on various computer vision tasks, including image classification, object detection, and semantic segmentation. In the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2015, the ResNet-152 architecture achieved a top-5 error rate of 3.57%, significantly better than the previous state-of-the-art error rate of 3.57%

TThe reasons why we opt for using this network for image classification are:
- Deeper networks can be built with Resnet.
- Performance metrics improvement
- Faster training and better convergence to the optimal solution.
- Transfer learning


#### Potential limitations

The model also presents limitations:
- Complexity: The presence of hop connections makes ResNets more complex than traditional deep neural networks, which can lead to higher computational demands and memory requirements.
- Susceptibility to overfitting
- Limited interpretability.
- Implementation of Batch normalization layers since ResNet heavily depends on it. 


#### Training Parameters
- Params (M): 25.6
- GMACs: 4.1
- Activations (M): 11.1


#### Datasets

The dataset we pretend to feed the model is a reduced version of the original one ("Food101"). Initially, it consists of 101 categories, each with 1000 training samples (images). Nevertheless, due to the lack of resources, we decided to simplify the problem by reducing the number of classes, that is, we preserved only the first 30 categories and samples. In this way, we managed to obtain a derived dataset with only 30,000 images for training. Despite this incise, the model is perfectly scalable: if we feed the model with more categories, it will be able to learn from them and recognize more types of food.

##### Training-Validation Data
Since we have a uniquely reduced version of the dataset, we have decided to split it into Training and Validation Data, with sizes of 20,000 and 10,000 images respectively.


#### Evaluation Results
Model settings:
- batch_size: 64
- epochs: 20
- Optimizer: Adam
- Loss Function: Cross Entropy
- Transfer Learning: No

Model metrics (of the last epoch):
- Training Loss: 1.447
- Evaluation Loss: 1.801
- Training Accuracy: 57.94
- Evaluation Accuracy: 47.39

Finally, in terms of the model's performance, it achieves a validation accuracy of 47% using images without applying any form of data augmentation. Consequently, implementing this approach is expected to enhance the robustness and accuracy of machine learning models, enabling them to perform effectively even with limited and inadequately representative data.




