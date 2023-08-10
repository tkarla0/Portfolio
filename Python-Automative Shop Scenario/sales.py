import csv


class Sale:
  #Initial function which sets number of sides to 6 by default
  def __init__(self): 
    file = open("inventory.csv")
    reader = csv.reader(file)
    self.inventory = list(reader)

  def printProducts(self):
      print (self.inventory[1:])
    
  #A method which rolls a die and prints the number returned
  def getProductInfo(self,prod_id,qty):
    exists = False
    for products in self.inventory[1:]:
      if products[0].strip() == prod_id.upper():
        exists= True
        costs = products[7]

    if exists == True:
      total_pre_tax = float(costs) * float(qty) 
      total_post_tax = float(total_pre_tax) * float(1.13)
      pre = round(total_pre_tax,2)
      post = round(total_post_tax,2)
      output_text = [products[5],pre,post,qty,costs,prod_id]
    else:
      output_text = "The product doesn`t exists"

    return output_text


  def printQuoteInfo(self,val):
    if isinstance(val,str):
      print (val)
    else:
      print(f"The total cost of {val[0]} is ${round(val[2],2)}.\nThe costs before tax is ${round(val[1],2)}")



  def getProductID(self):
    prod_id = input("Please enter the product ID of the item you would like to look up\n")
    if prod_id == 'quit':
      return False
    else: 
      return prod_id


  def getProductQuantity(self):
    while True:
      quantity_req = input("Please enter the quantity of items you require\n")
      try:
        qty = int(quantity_req)
        return qty
      except:
        print("You`ve entered an invalid number")

  