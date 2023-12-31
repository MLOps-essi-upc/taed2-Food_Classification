"""
Module Name: food_data.py

This script contains the data for the Food101 dataset. 
It includes the class names and extra information for each class.
"""

# Define a dictionary to store the class names for the id's.
class_id_to_class_name = {
    0: "baby_back_ribs",
    1: "beef_carpaccio",
    2: "bibimbap",
    3: "carrot_cake",
    4: "beet_salad",
    5: "cannoli",
    6: "clam_chowder",
    7: "caprese_salad",
    8: "croque_madame",
    9: "bread_pudding",
    10: "crab_cakes",
    11: "cheesecake",
    12: "cup_cakes",
    13: "creme_brulee",
    14: "chocolate_mousse",
    15: "chicken_curry",
    16: "caesar_salad",
    17: "club_sandwich",
    18: "churros",
    19: "baklava",
    20: "bruschetta",
    21: "chicken_wings",
    22: "chocolate_cake",
    23: "breakfast_burrito",
    24: "ceviche",
    25: "beef_tartare",
    26: "apple_pie",
    27: "beignets",
    28: "chicken_quesadilla",
    29: "cheese_plate"
}

# Define a dictionary to store extra information for food classes
food_class_info = {
    "baby_back_ribs": {
        "description": ("Baby back ribs are a popular American dish made from pork ribs, "
                        "typically from the top of the rib cage. They are often seasoned "
                        "with a dry rub or barbecue sauce and slow-cooked until tender."),
        "origin": "American",
        "type": "Savory",
        "ingredients": ["pork ribs", "seasonings", "dry rub or barbecue sauce"],
    },
    "beef_carpaccio": {
        "description": ("Beef carpaccio is a classic Italian dish made from thinly sliced "
                        "raw beef. It's often served as an appetizer and topped with "
                        "ingredients like arugula, olive oil, and lemon juice."),
        "origin": "Italian",
        "type": "Savory",
        "ingredients": ["raw beef", "arugula", "olive oil", "lemon juice"],
    },
    "bibimbap": {
        "description": ("Bibimbap is a popular Korean dish that combines steamed rice with "
                        "an array of sautéed and seasoned vegetables, often topped with a "
                        "choice of protein (such as beef, chicken, or tofu) and a spicy "
                        "gochujang sauce."),
        "origin": "Korean",
        "type": "Savory",
        "ingredients": ["rice", 
                        "sauteed vegetables", 
                        "protein (beef, chicken, tofu)", 
                        "gochujang sauce"],
    },
    "carrot_cake": {
        "description": ("Carrot cake is a moist and flavorful dessert made from grated carrots,"
                        "often topped with cream cheese frosting. It's known for its sweet and "
                        "tangy flavor."),
        "origin": "Global, with variations in American and British cuisines",
        "type": "Sweet",
        "ingredients": ["carrots", "flour", "eggs", "leavening agents", 
                        "nuts and raisins (optional)", "cream cheese", "butter"],
    },
    "beet_salad": {
        "description": ("Beet salad is a colorful and healthy dish made from roasted or "
                        "boiled beets, often mixed with ingredients like goat cheese, arugula, "
                        "and vinaigrette dressing. It's known for its sweet and earthy flavors."),
        "origin": "Global, with variations in Mediterranean and Eastern European cuisines",
        "type": "Savory",
        "ingredients": ["beets", "goat cheese", "arugula", "vinaigrette dressing"],
    },
    "cannoli": {
        "description": ("Cannoli are a classic Italian dessert made from fried pastry dough "
                        "filled with a sweet ricotta filling. They are often topped with "
                        "ingredients like chocolate chips, pistachios, or candied fruit."),
        "origin": "Italian",
        "type": "Sweet",
        "ingredients": ["flour", "cocoa pwder (optional)", "butter", "marsala wine", 
                        "ricotta cheese", "powdered sugar", "chocolate chips", 
                        "pistachios", "candied fruit"],
    },
    "clam_chowder": {
        "description": ("Clam chowder is a hearty soup made from clams, potatoes, "
                        "onions, and celery. It's known for its creamy texture "
                        "and rich flavor."),
        "origin": "American, New England",
        "type": "Savory",
        "ingredients": ["clams", "potatoes", "onions", "celery", "molk or cream", 
                        "flour", "butter"],
    },
    "caprese_salad": {
        "description": ("Caprese salad is a simple Italian salad made from sliced "
                        "tomatoes, mozzarella, and basil. It's known for its fresh "
                        "and vibrant flavors."),
        "origin": "Italian",
        "type": "Savory",
        "ingredients": ["tomatoes", "mozzarella", "basil"],
    },
    "croque_madame": {
        "description": ("Croque madame is a mouthwatering French sandwich made with "
                        "ham and cheese, often topped with a fried or poached egg. "
                        "It's a perfect blend of savory and rich flavors."),
        "origin": "French",
        "type": "Savory",
        "ingredients": ["ham", "cheese", "bread", "egg"],
    },
    "bread_pudding": {
        "description": ("Bread pudding is a comforting dessert made from stale bread, "
                        "milk, eggs, sugar, and spices. It's known for its soft and "
                        "custardy texture."),
        "origin": "Global, with variations in European and American cuisines",
        "type": "Sweet",
        "ingredients": ["stale bread", "milk", "eggs", ],
    },
    "crab_cakes": {
        "description": ("Crab cakes are a popular American dish made from crab meat, "
                        "bread crumbs, and seasonings. They are often served with a "
                        "creamy sauce for dipping."),
        "origin": "American",
        "type": "Savory",
        "ingredients": ["crab meat", "bread crumbs", "eggs", "mayonnaise", 
                        "mustard", "seasonings", "sauce"],
    },
    "cheesecake": {
        "description": ("Cheesecake is a rich and creamy dessert made from a mixture "
                        "of cream cheese, eggs, and sugar on a graham cracker crust. "
                        "It's known for its decadent flavor and texture."),
        "origin": "Global, with variations in European and American cuisines",
        "type": "Sweet",
        "ingredients": ["cream cheese", "eggs", "sugar", "graham cracker crust", 
                        "butter", "toppings (optional)"],
    },
    "cup_cakes": {
        "description": ("Cupcakes are small cakes made from cake batter and baked "
                        "in a cupcake pan. They are often topped with frosting and "
                        "other decorations."),
        "origin": "Global, with variations in European and American cuisines",
        "type": "Sweet",
        "ingredients": ["cake batter", "frosting", "decorations"],
    },
    "creme_brulee": {
        "description": ("Crème brûlée is a classic French dessert featuring a "
                        "creamy custard base topped with a layer of caramelized sugar. "
                        "It's known for its luscious, creamy texture and the satisfying "
                        "crack of the caramelized top."),
        "origin": "French",
        "type": "Sweet",
        "ingredients": ["custard", "caramelized sugar"],
    },
    "chocolate_mousse": {
        "description": ("Chocolate mousse is a light and airy dessert made from whipped "
                        "cream and melted chocolate. It's known for its rich chocolate "
                        "flavor and creamy texture."),
        "origin": "French",
        "type": "Sweet",
        "ingredients": ["whipped cream", "chocolate"],
    },
    "chicken_curry": {
        "description": ("Chicken curry is a savory and aromatic dish made by simmering "
                        "chicken in a rich and flavorful sauce created from a blend of "
                        "spices, tomatoes, and sometimes coconut milk. It's a staple in "
                        "cuisines like Indian and Thai."),
        "origin": "Indian, Thai, and various Asian cuisines",
        "type": "Savory",
        "ingredients": ["chicken", "spices", "tomatoes", "coconut milk"],
    },
    "caesar_salad": {
        "description": ("Caesar salad is a popular salad made from romaine lettuce, "
                        "croutons, and a creamy dressing made from ingredients like lemon juice, "
                        "olive oil, and anchovies. It's often topped with ingredients like "
                        "chicken or shrimp."),
        "origin": "Mexican",
        "type": "Savory",
        "ingredients": ["romaine lettuce", "croutons",
                        "dressing (lemon juice, olive oil, anchovies)"],
    },
    "club_sandwich": {
        "description": ("A club sandwich is a classic American sandwich made with layers of "
                        "sliced turkey, bacon, lettuce, tomato, and mayonnaise. "
                        "It's often served with a side of french fries."),
        "origin": "American",
        "type": "Savory",
        "ingredients": ["turkey", "bacon", "lettuce", "tomato", "mayonnaise", "bread"],
    },
    "churros": {
        "description": ("Churros are a popular Spanish dessert made from fried dough that is "
                        "often rolled in cinnamon sugar. They are known for their crispy exterior "
                        "and soft interior."),
        "origin": "Spanish",
        "type": "Sweet",
        "ingredients": ["dough", "cinnamon sugar"],
    },
    "baklava": {
        "description": ("Baklava is a sweet pastry made from layers of filo dough filled with "
                        "chopped nuts and held together with a sweet syrup or honey. "
                        "It's known for its flaky texture and rich flavor."),
        "origin": "Turkish",
        "type": "Sweet",
        "ingredients": ["filo dough", "nuts", "syrup or honey"],
    },
    "bruschetta": {
        "description": ("Bruschetta is an Italian appetizer made from grilled bread topped "
                        "with ingredients like tomatoes, basil, and olive oil. It's known for "
                        "its fresh and vibrant flavors."),
        "origin": "Italian",
        "type": "Savory",
        "ingredients": ["grilled bread", "tomatoes", "basil", "olive oil"],
    },
    "chicken_wings": {
        "description":("Chicken wings are a popular American dish made from chicken wings "
                       "that are fried and coated in a spicy sauce. They are often served "
                       "with celery and blue cheese or ranch dressing."),
        "origin": "American",
        "type": "Savory",
        "ingredients": ["chicken wings", "spicy sauce", "celery", "blue cheese or ranch dressing"],
    },
    "chocolate_cake": {
        "description": ("Chocolate cake is a rich and decadent dessert made from chocolate "
                        "cake layers and chocolate frosting. It's known for its intense "
                        "chocolate flavor."),
        "origin": "Global, with variations in European and American cuisines",
        "type": "Sweet",
        "ingredients": ["chocolate cake layers", "chocolate frosting"],
    },
    "breakfast_burrito": {
        "description": ("A breakfast burrito is a hearty breakfast dish made from a flour "
                        "tortilla filled with ingredients like scrambled eggs, potatoes, "
                        "and cheese. It's often served with salsa or hot sauce."),
        "origin": "Mexican",
        "type": "Savory",
        "ingredients": ["flour tortilla", "scrambled eggs", "potatoes", "cheese", 
                        "salsa or hot sauce"],
    },
    "ceviche": {
        "description": ("Ceviche is a refreshing South American dish featuring fresh raw "
                        "seafood, typically fish or shrimp, that is marinated in citrus juices, "
                        "often lime or lemon. It's mixed with ingredients like onions, cilantro, "
                        "and chili peppers for a zesty flavor."),
        "origin": "Peruvian and Latin American",
        "type": "Savory",
        "ingredients": ["fresh seafood (fish, shrimp)", "citrus juices (lime, lemon)", 
                        "onions", "cilantro", "chili peppers"],
    },
    "beef_tartare": {
        "description": ("Beef tartare is a French dish made from finely chopped or "
                        "minced raw beef. It's often served with ingredients like "
                        "onions, capers, and egg yolk."),
        "origin": "French",
        "type": "Savory",
        "ingredients": ["raw beef", "onions", "capers", "egg yolk"],
    },
    "apple_pie": {
        "description": ("Apple pie is a classic American dessert made from a pastry crust filled "
                        "with sliced apples and spices. It's known for its sweet and "
                        "comforting flavors."),
        "origin": "American",
        "type": "Sweet",
        "ingredients": ["pastry crust", "apples", "spices"],
    },
    "beignets": {
        "description": ("Beignets are a French dessert made from fried choux pastry that is "
                        "often dusted with powdered sugar. They are known for their light and "
                        "airy texture."),
        "origin": "French",
        "type": "Sweet",
        "ingredients": ["choux pastry", "powdered sugar"],
    },
    "chicken_quesadilla": {
        "description": ("A chicken quesadilla is a Mexican favorite made by filling a tortilla "
                        "with seasoned chicken, cheese, and various toppings. It's often served "
                        "with salsa or sour cream for added flavor."),
        "origin": "Mexican",
        "type": "Savory",
        "ingredients": ["tortilla", "seasoned chicken", "cheese", "salsa", "sour cream"],
    },
    "cheese_plate": {
        "description": ("A cheese plate is a delightful appetizer or dessert option that offers "
                        "a variety of cheeses, often accompanied by fruits, nuts, and an "
                        "assortment of bread or crackers. It's a perfect combination of "
                        "flavors and textures."),
        "origin": "Global, with variations in European and Mediterranean cuisines",
        "type": "Savory",
        "ingredients": ["assorted cheeses", "fruits", "nuts", "bread or crackers"],
    },
}
