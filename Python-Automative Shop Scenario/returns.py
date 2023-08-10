import json 

from sales import Sale
class Return:
  #Initial function which sets number of sides to 6 by default
  def __init__(self): 
    self.sales = {} #Registry Data
    self.invoice_num=0
    self.invoice_record={} #Record to be modified



  def loadData(self):
   f = open('registry_data.json')
   data = json.load(f)
   self.sales=data['orders']
   f.close()


  def locateInvoice(self,invoice_id):
    found = False
    found_data = {}
    for i in self.sales:
      if i["invoice_num"] == invoice_id:
        self.invoice_num = invoice_id
        found = True
        found_data = i 

    if found == False:
      return "Invoice not found"
    elif found == True:
       self.invoice_record=found_data
       return found_data


  def prodReturns(self,prod_id,qty):
    prods_sold = self.invoice_record["items_ordered"]
    newqty=0   
    total_before_tax = 0.00
    total_after_tax = 0.00
    deposits = round(float(self.invoice_record["deposit"]),2)
    item_found = False
    for key,x in prods_sold.items():
        if x[5] == prod_id:
          if x[3] >= qty:
            newqty = x[3] - qty
            updatedObj = Sale()
            newSalesData=updatedObj.getProductInfo(prod_id,newqty)
            prods_sold[key] = newSalesData
            self.invoice_record["returns"][key] = newSalesData
            self.invoice_record["items_ordered"] = prods_sold
            item_found = True
            total_before_tax = round(float(newSalesData[1]),2) + round(total_before_tax,2)
            total_after_tax = float(newSalesData[2]) + total_after_tax
        else:
          total_before_tax = round(float(x[1]),2) + round(total_before_tax,2)
          total_after_tax = float(x[2]) + total_after_tax
                
    
    balance_owe= round(total_after_tax,2) - round(deposits,2)
    if balance_owe >  0 :
      print(f"The new balance owing is {balance_owe}")
    elif balance_owe == 0:
        print("Your balance is paid in full ")
    else:
      print(f"A refund of ${round(abs(balance_owe),2)} will be returned to your account")
      balance_owe = 0
    self.invoice_record["invoice_total"] = total_after_tax
    self.invoice_record["invoice_subtotal"] = total_before_tax
    self.invoice_record["balance_owe"] = balance_owe
    self.invoice_record["status"] = "R"
    return item_found



  def updateObject(self):
    inv_n = str(self.invoice_num)
    temp_obj = self.sales
    for i in range(len(temp_obj)):
      if  temp_obj[i]["invoice_num"] == inv_n:
        del temp_obj[i]
        temp_obj.append(self.invoice_record)
        self.sales = temp_obj



  def updateJSONDoc(self):
    salesData = {
    "orders": self.sales
    }
    with open('registry_data.json', 'w') as json_file:
      json.dump(salesData, json_file)
        
    
   
  