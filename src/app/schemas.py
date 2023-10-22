from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile


class ImageUploadPayload(BaseModel):
    file: UploadFile
    model_conf: dict = {}  # You can specify a default value or leave it as an empty dictionary

    
class FoodClass(str, Enum):
    beet_salad = 0
    bibimbap = 1
    ceviche = 2
    cheese_plate = 3
    chicken_curry = 4
    chicken_quesadilla = 5
    creme_brulee = 6
    croque_madame = 7
    donuts = 8
    dumplings = 9
    escargots = 10
    fish_and_chips = 11
    french_fries = 12
    fried_rice = 13
    frozen_yogurt = 14
    gnocchi = 15
    guacamole = 16
    lasagna = 17
    lobster_roll_sandwich = 18
    output = 19
    pancakes = 20
    poutine = 21
    pulled_pork_sandwich = 22
    ramen = 23
    red_velvet_cake = 24
    samosa = 25
    sashimi = 26
    seaweed_salad = 27
    spring_rolls = 28
    tacos = 29
