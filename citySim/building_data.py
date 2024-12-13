# building_data.py
BUILDING_DATA = {
    "house": {
        "name": "House",
        "shape": [
            [1, 1],    # Simple 2x1 rectangular shape
        ],
        "image": "assets/images/buildings/house.png",
        "cost": {"wood": 10, "money": 50},
        "description": "A small residential building."
    },
    "shop": {
        "name": "Shop",
        "shape": [
            [1, 1, 1],    # 1x3 rectangle
        ],
        "image": "assets/images/buildings/shop.png",
        "cost": {"wood": 20, "money": 100},
        "description": "A place to trade goods."
    },
    "l_shape_building": {
        "name": "L-shape Building",
        "shape": [
            [1, 1, 1],  # Bottom row
            [1, 0, 0],  # Top-left corner
        ],
        "image": "assets/images/buildings/l_shape.png",
        "cost": {"steel": 50, "money": 200},
        "description": "An L-shaped building."
    },
    # More buildings with irregular shapes...
}
