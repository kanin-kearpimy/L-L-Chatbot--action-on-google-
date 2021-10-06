class ShopCollection:

    def __init__(self, session_id):
        self.session_id = session_id
    
    def generateCollection(self):
        return {
            "session": {
            "id": self.session_id,
            "params": {},
        "typeOverrides": [
            {
            "name": "item_option",
            "synonym": {
                "entries": [
                {
                    "name": "ITEM_1",
                    "synonyms": [
                        "Item 1",
                        "First item",
                        "Red Water",
                        "Noddle Red Water"
                    ],
                    "display": {
                    "title": "Noddle Red Water",
                    "description": "Noddle Red Water Description",
                    "image": {
                        "alt": "Google Assistant logo",
                        "height": 0,
                        "url": "https://storage.thaipost.net/main/uploads/photos/big/20190617/image_big_5d073fa5c5e36.jpg",
                        "width": 0
                        }
                    }
                },
                {
                    "name": "ITEM_2",
                    "synonyms": [
                        "Item 2",
                        "Second item",
                        "Blue Water",
                        "Noddle Blue Water"
                    ],
                    "display": {
                    "title": "Noddle Blue Water",
                    "description": "Description of Noddle Blue Water",
                    "image": {
                        "alt": "Google Assistant logo",
                        "height": 0,
                        "url": "https://bottomlineis.co/uploads/images/image_750x_5d691a8d5f2f9.jpg",
                        "width": 0
                        }
                    }
                },
                ]
            },
            "typeOverrideMode": "TYPE_REPLACE"
            }
        ]
        },
        "prompt": {
        "override": False,
        "content": {
            "collection": {
            "imageFill": "UNSPECIFIED",
            "items": [
                {
                "key": "ITEM_1"
                },
                {
                "key": "ITEM_2"
                }
            ],
            "subtitle": "Please choose what you want",
            "title": "James Shop Menu"
            }
        },
        "firstSimple": {
            "speech": "This is James shop menu. please choose what you want.",
            "text": "This is James shop menu. please choose what you want."
            }
        }
    }

    def generateSimpleResponse(self, item_selected):
        return {
            "session": {
                "id": self.session_id,
                "params": {}
            },
            "prompt": {
                "override": False,
                "firstSimple": {
                    "speech": "You've selected {}. Shop is handling with it.".format(item_selected),
                    "text": "You've selected {}. Shop is handling with it.".format(item_selected)
                },
            }
        }
    
    def errorResponse(self):
        return {
            "session": {
                "id": self.session_id,
                "params": {}
            },
            "prompt": {
                "override": False,
                "firstSimple": {
                    "speech": "Sorry, We are unable to get. Please try again.",
                    "text": "orry, We are unable to get. Please try again."
                },
            }
        }
    
    def fadeEndResponse(self):
        return {
            "session": {
                "id": self.session_id,
                "params": {}
            },
            "prompt": {
                "override": False,
                "firstSimple": {
                    "speech": "Thank you.",
                    "text": "Thank you."
                },
            }
        }

    def placeorderResponse(self, item):
        return {
        "session": {
            "id": self.session_id,
            "params": {}
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": "You selected {} with {} size, and {} taste. Total price is {}. Would you like to confirm your order?".format(item['menu']['name'], item['size'], item['taste'], item['menu']['price']),
                "text": "You selected {} with {} size, and {} taste. Total price is {}. Would you like to confirm your order?".format(item['menu']['name'], item['size'], item['taste'], item['menu']['price'])
            },
            "suggestions": [
                {
                    "title": "Yes, I do"
                }, 
                {
                    "title": "No, No I don't"
                }
            ]
        }
    }