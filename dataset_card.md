## Dataset Card

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

### Dataset Description
The dataset that we have used has been extracted from [Hugging Face - Food 101](https://huggingface.co/datasets/food101).

We have also use 30 extenal images to evaluate the model's performance on different and unknown data. Also because including external images can reduce the risk of bias in the model by exposing it to a broader range of images. 

#### Dataset Summary
This dataset contains 101,000 food images in total, each one belonging to one of 101 possible classes. That is a large and significant weight in terms of data volume. Thus, we have undertaken a reduction process to simplify the problem, but maintaining the same structure and final goal. 

The reduced dataset consists of 30 food categories and 30.000 images in total (1.000 images of each class). For each class, 250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. All images were rescaled to have a maximum side length of 512 pixels.

#### Languages
The laanguage used in the dataset is English.


### Dataset Structure
#### Data Instances
A data instance refers to an image that is categorized within one of the 30 distinct classes. Each individual image is inside a directory whose name aligns with the corresponding class it represents.

Example: 
```
{
  'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=384x512 at 0x276021C5EB8>,
  'label': 23
}
```

#### Data fields
The data instances have the following fields:

- image: A PIL.Image.Image object containing the image. Note that when accessing the image column: dataset[0]["image"] the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the "image" column, i.e. dataset[0]["image"] should always be preferred over dataset["image"][0].
- label: an int classification label.


#### Data Splits
|                         | Train split | Test split |
|-------------------------|------------:|------------|
| Number of examples      |   22,500    |   7,500    |


### Considerations for Using the Data

#### Social Impact of Dataset
The implications of this project are far-reaching, such as knowing meaningful information about dishes or aiding in dietary assessment. 

#### Discussion of Biases
The dataset must contain a similar number of samples for each category of food image in order to handle the bias. In this case, the balance is achieved.


#### Other Known Limitations
Some limitations that this dataset has are the following:

- Images may contain distracting background elements or objects that are not relevant to the food item, which can make classification more challenging.

- Food portion sizes can vary significantly, and the dataset may not capture this variability well. For example, if the model has been trained with images of "cakes", it maight struggle to identify a cake when the input image is a pice of it.

- The appearance of a dish can vary based on how it's plated and presented. 


### Addtional Information

#### Data curators 
The people involved in the data discorery, data organization, data quality and validation are [Alexandra González](https://github.com/alexandraglz), [Wenli Pan](https://github.com/wenlipan7) and [Violeta Sànchez](https://github.com/violeta51).

#### Licensing Information
The Food-101 data set consists of images from [Foodspotting](http://www.foodspotting.com/) which are not property of the Federal Institute of Technology Zurich (ETHZ). Any use beyond scientific fair use must be negociated with the respective picture owners according to the [Foodspotting terms of use](http://www.foodspotting.com/terms/).


#### Citation Information
```
@inproceedings{bossard14,
  title = {Food-101 -- Mining Discriminative Components with Random Forests},
  author = {Bossard, Lukas and Guillaumin, Matthieu and Van Gool, Luc},
  booktitle = {European Conference on Computer Vision},
  year = {2014}
}
```

#### Contributions
Thanks to @nateraw for adding this dataset.
