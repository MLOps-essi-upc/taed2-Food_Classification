# TAED2-Img_Classification

## Introduction
The purpose of the project is to gain a deeper understanding of managing ML projects. To achieve this, we are encouraged to build and deploy an ML component. With this goal in mind, our project consists of an image classification, in particular, a neural net that classifies accurately food images. The dataset used in all the simulations is sourced from Hugging Face\: https://huggingface.co/datasets/food101.


## Dataset Card

The dataset consists of 30 food categories and 30.000 images (1.000 images of each class). For each class, 250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. All images were rescaled to have a maximum side length of 512 pixels.

Train split:

- Number of examples: 22.500.

Test split:

- Number of examples: 7.500.

Language: English.

### Downsizing of a Large Dataset

The dataset that we have used has been extracted from "Food 101", which has a large and significant weight in terms of data volume. Thus, we have undertaken a reduction process to simplify the problem, but maintaining the same structure and final goal. Consequently, instead of the original 101 classes, we now have 30 classes, each comprising 1,000 images. 

## Model Card
The model we aimed to use is a neural network for image classification. There are a vast of architectures that we could use. 

#### The Model

#### Intended Use

#### Training Parameters

#### Evaluation Results



