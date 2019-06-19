from bottle import run, route, view, get, post, request, static_file
from itertools import count


class Canteen:

    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)

    def __init__(self, food_name, food_image, food_stock, food_price, food_total ):
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = food_name
        self.image = food_image
        self.stock = food_stock               # these variables are coming from out list
        self.price = food_price               # to create objects that are easily referenced
        self.total = food_total
        
    #Test Data
food =    [
          Canteen("Sushi Roll pack", "sushdiggity.jpg", 5, "$10", 0),
          Canteen("Hot dog and Chips", "hotdiggity.jpg",  12, "$8", 0),
          Canteen("Ham and Cheese Sandwiches", "hamdiggity.jpg", 4, "$5", 0)
          ]

@route("/")     #My Websites index
@view("index")
def index():
    #need this function to attach the decorators.
    pass

@route("/menu")   # Creates a menu for my page.
@view("menu")
def Canteen():
    data = dict (menu_list = food)     #Creates a dictionary for the list of food I need in my menu
    return data

@route('/purchase-success/<item_id>', method = 'POST')    #This function will 
@view('purchase-success')                                 #
def purchase_success(item_id):
    item_id = int(item_id)
    found_item = None   
    for item in food: 
        if item.id == item_id:
            found_item  = item
    data = dict(item = found_item)
    found_item.stock -= 1   #minus 1 from the amount of items in stock
    found_item.total += 1
    return data 
    
@route('/picture/<filename>')
def serve_picture(filename):
    return static_file(filename, root = './Images')

@route("/restock")
@view("restock")
def restock():
    data = dict (menu_list = food)
    return data

@route('/restock/<item_id>', method = 'POST')
@view ('restock-success')
def restock_success(item_id):
    item_id = int(item_id)
    found_item = None
    for item in food:
        if item.id == item_id:
            found_item = item
    data = dict (item = found_item)
    quantity = request.forms.get('quantity')
    quantity = int(quantity)
    found_item.stock += quantity
    
    return data

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)
