# TAED2-Img_Classification

## Introduction
The purpose of the project is to gain a deeper understanding of managing ML projects. To achieve this, we are encouraged to build and deploy an ML component. With this goal in mind, our project consists of an image classification, in particular, a neural net that classifies accurately food images. The dataset used in all the simulations is sourced from (............).


## Dataset Card

The dataset consists of 101 food categories and 101.000 images (1.000 images of each class). For each class, 250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. All images were rescaled to have a maximum side length of 512 pixels.

Train split:

- Number of examples: 75750.

Test split:

- Number of examples: 25250.

Language: English.

### Downsizing of a Large Dataset

Due to the dataset's large size and significant weight in terms of data volume, we have undertaken a reduction process. Specifically, out of the initial 101,000 samples, we have retained 30,000 samples. Consequently, instead of the original 101 classes, we now have 30 classes, each comprising 1,000 images. This reduction was implemented to alleviate the challenges posed by the dataset's immense size.

## Model Card
The model we aimed to use is a neural network for image classification. There are a vast of architectures that we could use. 

#### The Model

#### Intended Use

#### Training Parameters

#### Evaluation Results



