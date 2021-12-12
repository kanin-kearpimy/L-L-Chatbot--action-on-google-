import Shop
from fastapi import FastAPI, Request
from Shop.ShopCollection import ShopCollection

app = FastAPI()

CONFIGURATED = {
    "menu": ["noodle red water", "noodle blue water"],
    "taste": ["neutral", "spicy"],
    "size": ["big", "medium", "small"]
}

orders = {}

MENU = {
    'ITEM_1': {
        'name': 'Noddle Red Water',
        'price': 40
    },
    'ITEM_2': {
        'name': 'Noddle Blue Water',
        'price': 30
    }
}

@app.post('/')
async def main(request: Request):
    assistant_request =  await request.json()
    session_id = assistant_request['session']['id']
    handler_name = assistant_request['handler']['name']
    shop = ShopCollection(session_id)
    current_item = 0
    if(session_id in orders.keys()):
        current_item = len(orders[session_id]) - 1
    if(handler_name == "multipleitem"):
        init_menu = {'menu': {}, 'taste': '', 'size': '', 'status': 'pending'}
        extract_menu = queryAllSlot(assistant_request['scene']['slots']['multipleitem']['value'], init_menu)
        if(session_id in orders.keys()):
            orders[session_id].append(extract_menu)
        else:
            orders[session_id] = [extract_menu]
        return
    if(handler_name == "shop_item"):
        init_menu = {'menu': {}, 'taste': '', 'size': '', 'status': 'pending'}
        if(session_id in orders.keys()):
            orders[session_id].append(init_menu)
        else:
            orders[session_id] = [init_menu]
        return shop.generateCollection()
    elif(handler_name == "taste_handler"):
        taste_select = assistant_request['intent']['query']
        orders[session_id][current_item]['taste'] = taste_select
    elif(handler_name == "display_shop_item_result"):
        # item_select = assistant_request['intent']['query']
        item_key = assistant_request['scene']['slots']['NoodleType']['value']
        orders[session_id][current_item]['menu'] = MENU[item_key]
        # return shop.generateSimpleResponse(item_select)
    elif(handler_name == "size_handler"):
        size_select = assistant_request['intent']['query']
        orders[session_id][current_item]['size'] = size_select
    elif(handler_name == "placeholder_onenter_handler"):
        return shop.placeorderResponse(orders[session_id][current_item])
    elif(handler_name == "placeholder_handler"):
        answer = assistant_request['intent']['query']
        if("YES" in answer.upper()):
            orders[session_id][current_item]['status'] = 'completed'
        else:
            orders[session_id].pop(current_item)
            current_item = current_item - 1
        return shop.fadeEndResponse()
    else:
        return shop.errorResponse()

@app.get('/order')
async def order():
    return orders


def queryAllSlot(slot, init_menu):
    for key in CONFIGURATED.keys():
        for item in CONFIGURATED[key]:
            if item in slot:
                if(key == 'menu'):
                    init_menu['menu'] = MENU['ITEM_1' if item == 'noodle red water' else 'ITEM_2']
                else:
                    init_menu[key] = item
    return init_menu