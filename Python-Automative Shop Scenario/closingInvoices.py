import json

class CloseInvoice:
  #Initial function which sets number of sides to 6 by default
  def __init__(self): 
    self.invoice_num=0
    self.amt_paid = 0.00
    self.sales=[]
    self.remove_i = 0
    self.found_record = {}

  def loadData(self):
   f = open('registry_data.json')
   data = json.load(f)
   self.sales=data['orders']
   f.close()

  def locateProduct(self,invoice_id):
    found = False
    found_data = {}
    for i in self.sales:
      if i["invoice_num"] == invoice_id:
        self.remove_i = invoice_id
        self.invoice_num = invoice_id
        found = True
        found_data = i 

    if found == False:
      return "Invoice not found"
    elif found == True:
       self.found_record=found_data
       return found_data


  def balancingOwingPaid(self,found_data):
    balance = round(found_data["balance_owe"],2)
    if balance > 0 :
      print(f"Your balance owing is ${balance}")
      payment_amt = float(input("Please enter the amount you would like to pay: "))
      if payment_amt > balance:
        print (f"You`ve overpaid ${payment_amt-balance} will be returned to you")
        found_data["balance_owe"] = 0.00
        found_data["deposit"] = balance
        found_data["status"] = "C"
      elif balance > payment_amt:
        print (f"The balance on the invoice is  ${balance - payment_amt} ")
        new_bal = balance - payment_amt
        prev_deposit =  round(found_data["deposit"],2)
        new_deposit = prev_deposit + payment_amt
        found_data["deposit"] = balance = new_deposit
        found_data["balance_owe"] = new_bal
      elif balance == payment_amt:
        print("You bil is paid in full")
        prev_deposit =  round(found_data["deposit"],2)
        new_deposit = prev_deposit + payment_amt
        found_data["deposit"] = balance = new_deposit
        found_data["balance_owe"] = 0
        found_data["status"] = "C"
      self.found_data=found_data  
      return True
    else:
      return False
    


  def updateObject(self):
    inv_n = str(self.invoice_num)
    temp_obj = self.sales
    for i in range(len(temp_obj)):
      if temp_obj[i]["invoice_num"] == inv_n:
        del temp_obj[i]
        temp_obj.append(self.found_data)
        self.sales = temp_obj



  def updateJSONDoc(self):
    salesData = {
    "orders": self.sales
    }
    with open('registry_data.json', 'w') as json_file:
      json.dump(salesData, json_file)
        
    
    