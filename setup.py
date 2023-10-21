"""
Setup script for the Food Image Classification project.

This script is used to configure and install the 'src' package. 
The project is a part of the Advanced Data Science Topics II course 
at Universitat Politècnica de Catalunya (UPC) and focuses on 
classifying food images using deep learning.

Authors: Alexandra González, Wenli Pan, and Violeta Sànchez
License: MIT
"""

from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description="""This repository contains the project
    for Advanced Data Science Topics II course at Universitat
    Politècnica de Catalunya (UPC). It classifies food images
    using deep learning.""",
    author='Alexandra González, Wenli Pan & Violeta Sànchez',
    license='MIT',
)
