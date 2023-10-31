"""
Module Name: schemas.py

This module contains the schemas for our API.
"""

from enum import Enum
from pydantic import BaseModel
from fastapi import UploadFile


class ImageUploadPayload(BaseModel):
    """Schema for the image upload endpoint."""

    file: UploadFile
    model_conf: dict = {}  # You can specify a default value or leave it as an empty dictionary


class FoodClass(str, Enum):
    """Schema for the food class endpoint."""

    BABY_BACK_RIBS = 0
    BEEF_CARPACCIO = 1
    BIBIMBAP = 2
    CARROT_CAKE = 3
    BEET_SALAD = 4
    CANNOLI = 5
    CLAM_CHOWDER = 6
    CAPRESE_SALAD = 7
    CROQUE_MADAME = 8
    BREAD_PUDDING = 9
    CRAB_CAKES = 10
    CHEESECAKE = 11
    CUP_CAKES = 12
    CREME_BRULEE = 13
    CHOCOLATE_MOUSSE = 14
    CHICKEN_CURRY = 15
    CAESAR_SALAD = 16
    CLUB_SANDWICH = 17
    CHURROS = 18
    BAKLAVA = 19
    BRUSCHETTA = 20
    CHICKEN_WINGS = 21
    CHOCOLATE_CAKE = 22
    BREAKFAST_BURRITO = 23
    CEVICHE = 24
    BEEF_TARTARE = 25
    APPLE_PIE = 26
    BEIGNETS = 27
    CHICKEN_QUESADILLA = 28
    CHEESE_PLATE = 29
