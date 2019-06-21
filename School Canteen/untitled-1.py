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
        
    
food =    [
          Canteen("Sushi Roll pack", "sushdiggity.jpg", 5, "$10", 0),
          Canteen("Hot dog and Chips", "hotdiggity.jpg",  12, "$8", 0),          #Test Data
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

@route('/purchase-success/<item_id>', method = 'POST')    # This function will 
@view('purchase-success')                                 # minus one from the stock of a purchased
def purchase_success(item_id):                            # item and send my user to a 
    item_id = int(item_id)                                # success page
    found_item = None   
    for item in food:              # searches through my test data to match existing product 
        if item.id == item_id:       # to purchased product
            found_item  = item         
    data = dict(item = found_item)       
    found_item.stock -= 1   # minus 1 from the amount of items in stock
    found_item.total += 1    # adds one if the user wanted to restock
    return data 
    
@route('/picture/<filename>')                         # function exists so that I can 
def serve_picture(filename):                            # add pictures to my website 
    return static_file(filename, root = './Images')

@route("/restock")                               
@view("restock")                           # This function is used to create 
def restock():                              # A basic restock page for people adding stock
    data = dict (menu_list = food)
    return data

@route('/restock/<item_id>', method = 'POST')      
@view ('restock-success')
def restock_success(item_id):                #This function adds one to a chosen stock and sends        
    item_id = int(item_id)                    #users to a restock page
    found_item = None
    for item in food:
        if item.id == item_id:         # Matches chosen item to item in food list
            found_item = item            
    data = dict (item = found_item)
    quantity = request.forms.get('quantity')     # gets the quantity that is wanted to add to stock 
    quantity = int(quantity)                     # from a form in my html
    found_item.stock += quantity     # Adds users chosen quantity to stock
    
    return data

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)   # Creates localhost for website
