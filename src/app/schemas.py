from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile


class ImageUploadPayload(BaseModel):
    file: UploadFile
    model_conf: dict = {}  # You can specify a default value or leave it as an empty dictionary


class FoodClass(str, Enum):
    baby_back_ribs = 0
    beef_carpaccio = 1
    bibimbap = 2
    carrot_cake = 3
    beet_salad = 4
    cannoli = 5
    clam_chowder = 6
    caprese_salad = 7
    croque_madame = 8
    bread_pudding = 9
    crab_cakes = 10
    cheesecake = 11
    cup_cakes = 12
    creme_brulee = 13
    chocolate_mousse = 14
    chicken_curry = 15
    caesar_salad = 16
    club_sandwich = 17
    churros = 18
    oubaklava = 19
    bruschetta = 20
    chicken_wings = 21
    chocolate_cake = 22
    breakfast_burrito = 23
    ceviche = 24
    beef_tartare = 25
    apple_pie = 26
    beignets = 27
    chicken_quesadilla = 28
    cheese_plate = 29
