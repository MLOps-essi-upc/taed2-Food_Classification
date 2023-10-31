# TAED2-Food Classification

This repository contains the project for "Advanced Data Science Topics II" course at Universitat Politècnica de Catalunya (UPC). The purpose of the project is to gain a deeper understanding of managing ML projects. To achieve this, we are encouraged to build and deploy an ML component.

With a strong emphasis on practical application, our project consists of an image classification tool. Specifically, a neural network capable of accurately classifying food images.

In addition to the core image classification task, our project encompasses a comprehensive documentation and reporting framework. This documentation will provide a holistic view of the ML project lifecycle, including critical aspects such as data acquisition, preprocessing, model selection, training, evaluation, and deployment strategies.

The ultimate aim of our project is to make a meaningful contribution to the field of food image classification. This contribution could have far-reaching implications, such as knowing meaningful information about dishes or aiding in dietary assessment. Moreover, this project offers invaluable hands-on experience in managing real-world ML projects, a skillset that holds immense importance in the dynamic field of data science.

**Project Insights: Dataset and Model Cards**

- [Dataset Card](https://github.com/MLOps-essi-upc/taed2-Food_Classification/blob/main/dataset_card.md)

- [Model Card](https://github.com/MLOps-essi-upc/taed2-Food_Classification/blob/main/model_card.md)

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── features       <- Two .csv files containing features of the data (image size, dynamic range...).
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   ├── raw            <- The original, immutable data dump.
    │   └── test           <- Images used in test stage.
    |       ├── beef_carpaccio <- 5 beef carpaccio images for testing.
    │       └── food_test_1    <- 30 images (one for each class) for testing.
    │
    ├── gx                 <- Great Expectations configuration.
    │   ├── checkpoints
    │   ├── expectations
    │   ├── plugins
    │   └── uncommitted
    |
    ├── metrics
    │   ├── metrics_evolution   <- Plots of the accuracy and loss evolution on train and evaluation stage.
    │   └── emissions.csv       <- C02 emissions.
    |
    ├── models
    │   ├── Output-Food-Dictionary.csv <- Dictionary with the correspondence between class id and class name.
    │   └── RESNET34       <- Trained model.
    │
    ├── notebooks          <- Jupyter notebooks.
    │   ├── mlruns
    │   └── 1.0-wp-resnet34-training.ipynb
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported.
    ├── src                <- Source code for use in this project.
    │   ├── app            <- Files and directories used for API development.
    │   │   ├── api.py
    │   │   ├── food_data.py
    │   │   ├── schemas.py
    │   │   └── script_test.py
    │   │
    │   ├── features       <- Scripts to download, preprocess and validate data for modeling
    │   │   ├── download_data.py
    │   │   ├── preprocess_data.py
    │   │   ├── torch_to_df_data.py
    │   │   └── validate.py
    │   │
    │   └── models         <- Scripts to evaluate models and use them for prediction
    │       ├── evaluate.py
    │       └── predict_model.py
    │
    ├── tests              <- PyTest scripts.
    │   └── pytest
    │       ├── test_api.py
    │       ├── test_output_coherence.py
    │       └── test_specific_class.py
    │ 
    ├── dataset_card.md
    │ 
    ├── model_card.md
    |
    ├── dvc.yaml
    │ 
    ├── test_environment.py
    │ 
    ├── dvc.look
    │ 
    ├── pyproject.toml
    │ 
    └── tox.ini            <- Tox file with settings for running tox.

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
