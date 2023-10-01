## Dataset Card

### Dataset Summary
The dataset that we have used has been extracted from ["Hugging Face - Food 101"](https://huggingface.co/datasets/food101). The remarkable fact about this dataset is that it has a large and significant weight in terms of data volume, as it contains 101 classes (101,000 images in total). Thus, we have undertaken a reduction process to simplify the problem, but maintaining the same structure and final goal. 

The reduced dataset consists of 30 food categories and 30.000 images in total (1.000 images of each class). For each class, 250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. All images were rescaled to have a maximum side length of 512 pixels.

Language: English.


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
Train split: 

- Number of examples: 22.500.

Test split:

- Number of examples: 7.500.


### Addtional Information

#### LICENSE AGREEMENT

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
