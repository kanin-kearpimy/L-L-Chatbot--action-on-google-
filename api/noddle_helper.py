import Shop
from fastapi import FastAPI, Request
from Shop.ShopCollection import ShopCollection

app = FastAPI()

orders = {}

menu = {
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
    if(handler_name == "shop_item"):
        init_menu = {'menu': {}, 'taste': '', 'status': 'pending'}
        if(session_id in orders.keys()):
            orders[session_id].append(init_menu)
        else:
            orders[session_id] = [init_menu]
        return shop.generateCollection()
    elif(handler_name == "taste_handler"):
        print(current_item)
        taste_select = assistant_request['intent']['query']
        orders[session_id][current_item]['taste'] = taste_select
    elif(handler_name == "display_shop_item_result"):
        item_select = assistant_request['intent']['query']
        item_key = assistant_request['intent']['params']['item_option']['resolved']
        orders[session_id][current_item]['menu'] = menu[item_key]
        orders[session_id][current_item]['status'] = 'completed'
        return shop.generateSimpleResponse(item_select)

@app.get('/order')
async def order():
    return orders