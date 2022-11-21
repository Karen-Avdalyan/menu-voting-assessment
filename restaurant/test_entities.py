TEST_ENTITIES = {
    "users": {
        "admin": {
            "username": "adm",
            "password": "adm",
        },
        "employee": {
            "username": "employee",
            "password": "12345678",
        },
        "restaurant_worker": {
            "username": "restaurant_worker",
            "password": "12345678",
        },
    },
    "groups": [{"name": "employee"}, {"name": "restaurant"}],
    "restaurant": {
        "name": "Ramsey's",
    },
    "menu": {
        "items": [
            {"name": "Harisa", "description": "fabulous", "price": 101},
            {"name": "Khash", "description": "delicious", "price": 100},
            {"name": "Dolma", "description": "marvellous", "price": 102},
        ],
        "restaurant_name": "Ramsey's",
        "name": "menu",
    }
}
