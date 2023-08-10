from sales import Sale
from dateInfo import DateInformation
import json
import os
from datetime import datetime


class Invoice:
  #Initial function which sets number of sides to 6 by default
  def __init__(self): 
    self.prod_ordered ={}
    self.name = ""
    self.phone=""
    self.postal_code=""
    self.date=datetime.now()
    self.payment_method = 'Cash'
    self.total_costs=0.00
    self.cost_pre_tax=0.00
    self.deposits=0.00
    self.invoice_number = 0
    self.total_before_tax = 0.00
    self.total_after_tax = 0.00
    self.total_taxes = 0.00
    self.balance_owe=0.00

  def createProductLineItems(self):
    x=1
    while True:
      lineItems = Sale()
      prod_id=lineItems.getProductID()
      if prod_id != 'quit':
        prod_qty = lineItems.getProductQuantity()
        if prod_qty != 'quit':
          item = lineItems.getProductInfo(prod_id,prod_qty)
          if item != "The product doesn`t exists":
            self.prod_ordered[x] = item
            x = x + 1 
        else:
          return False
      else:
        return False

      add_more = input("Would you like to add another item y/n \n")
      if add_more == 'n':
        return 'proceed'
      elif add_more == 'quit':
        return False
      elif add_more == 'y':
        print("\n")


  def getClientInfo(self):
    name = input("Please enter the client`s name: ")
    if name != 'quit':
      self.name = name
      number = input("Please enter the client`s contact number: ")
      if number != 'quit':
        self.number = number
        postal = input("Please enter the client`s postal code: ")
        if postal != 'quit':
          self.postal_code = postal
          deposit_paid = input("Please enter the deposit paid: ")
          if deposit_paid != 'quit':
            self.deposits = float(deposit_paid)
            pay_meth = input("Please enter your method of payment: ")
            if pay_meth != 'quit':
              self.payment_method = pay_meth
              return 'proceed'
            else:
              return False
          else:
            return False
        else:
          return False
      else:
        return False
    else:
      return False


  

  def getInvoiceNumber(self):
    try:
      i_file = open("latest_invoice.txt","r")
      num = i_file.read()
      num = int(num) + 1
      string_num = str(num)
      i_file = open("latest_invoice.txt","w")
      i_file.write(string_num)
      self.invoice_number = str(num)
    except:
      i_file = open("latest_invoice.txt","x")
      i_file.write("1")
      self.invoice_number = '1'


  def addToRegistry(self):
    lineItems = DateInformation()
    registry_info = {
      "name":self.name,
      "number":self.number,
      "postal":self.postal_code,
      "items_ordered":self.prod_ordered,
      "invoice_subtotal":self.total_before_tax,
      "payment_method":self.payment_method,
      "deposit":self.deposits,
      "invoice_total":self.total_after_tax,
      "balance_owe":self.balance_owe,
      "date": lineItems.formatDate,
      "invoice_num": self.invoice_number,
      "status":"I",
      "returns":{}
    }
    
    self.updateJSONFile(registry_info)
    #print(registry_info)

  
  def updateJSONFile(self,registry_info):
      isExisting = os.path.exists("registry_data.json")
      f = { "orders": []}
      if isExisting == False:
        with open("registry_data.json",'w+') as fl:
          json.dump(f,fl)
          
      with open("registry_data.json",'r+') as file:
        file_data = json.load(file)
        file_data["orders"].append(registry_info)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
 



    
  def createInvoiceFile(self):
    lineItems = DateInformation()
    i_num = "I-"+self.invoice_number
    i_fn = i_num +".txt"
    total_before_tax = 0.00
    total_after_tax = 0.00
    f = open(i_fn,"a")
    f.write("#############################################################################################\n")
    f.write("##############################################Cambrian's Car Audio Inc.######################\n")
    f.write("#############################################################################################\n")
    f.write("#############INVOICE NUMBER:"+ i_num + "#############################################################\n")
    f.write("Date: \t" + lineItems.formatDate+ "\n")
    f.write("\n\n")
    f.write("Name:" + str(self.name) + "\n")
    f.write("Number:" + str(self.number) + "\n")
    f.write("Postal Code:" + str(self.postal_code) + "\n")
    f.write("#############################################################################################\n")
    f.write("Model# \tDescription \t\tUnits\tCost Per Unit\tAmount\n")
    for x in self.prod_ordered.values():
         val_1 = str(x[3])
         val_2 = str(x[4] )
         val_3 = str(x[1])
         f.write(x[5]+"\t"+ x[0] + "\t\t"+ val_1 +"\t$"+ val_2 + "\t$"+ val_3 + "\n")
         total_before_tax = round(float(x[1]),2) + round(total_before_tax,2)
         total_after_tax = float(x[2]) + total_after_tax
    f.write("#############################################################################################\n")
    bf_tax = str(total_before_tax)
    f.write("Invoice Subtotal\t\t\t\t\t\t$" + bf_tax + "\n")
    f.write("Tax Rate\t\t\t\t\t\t 13%" "\n")
    sales_tax = round(total_after_tax,2) - round(total_before_tax,2)
    balance_owe= round(total_after_tax,2) - round(float(self.deposits),2)
    st = str(round(sales_tax,2))
    f.write("Sales Tax \t\t\t\t\t\t$" + st + "\n")
    f.write("Payment Method\t\t\t\t\t\t" + self.payment_method +  "\n")
    dept = str(self.deposits)
    f.write("Deposit Received\t\t\t\t\t\t$" + dept +  "\n")
    f.write("#############################################################################################\n")
    tat = str(round(total_after_tax,2))
    f.write("INVOICE TOTAL\t\t\t\t\t\t\t$" + tat +  "\n")
    f.write("#############################################################################################\n")
    bo = str(round(balance_owe,2))
    f.write("BALANCING OWING\t\t\t\t\t\t\t$" + bo +  "\n")
    f.write("#############################################################################################\n")
    
    self.total_after_tax = total_after_tax
    self.total_before_tax = total_before_tax
    self.balance_owe = balance_owe



