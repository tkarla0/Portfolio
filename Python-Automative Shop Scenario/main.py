def welcomeMessage():
  print("Please enter the corresponding number to perform the respective task, enter quit at anytime to end the program")
  print("1) Create an invoice\n2) Close an existing invoice that is not fully paid.\n3) make a product return \n4) make a quote on an item" )

from sales import Sale
from invoices import Invoice
from closingInvoices import CloseInvoice
from returns import Return

print("*************************************************Welcome to Cambrian`s Car Audio Inc**************************")
valid = True

while valid != False:
  welcomeMessage()
  user_task = input("Please enter the number \n")
  if user_task == 'quit':
    valid=False
    break
  else:
    if user_task == '1':
      invoice_generation = Invoice()
      status = invoice_generation.createProductLineItems()
      if status == False:
        valid = False
      else:
        client_info= invoice_generation.getClientInfo()
        if client_info == False:
          valid = False
        else:
          invoice_generation.getInvoiceNumber()
          invoice_generation.createInvoiceFile()
          invoice_generation.addToRegistry()
        print(invoice_generation.prod_ordered)
    elif  user_task == '2':
      closing_invoice = CloseInvoice()
      closing_invoice.loadData()
      inv_id = input("Please enter the Invoice Number (Number only)  of the invoice you would like to close: ")
      invoice_info = closing_invoice.locateProduct(inv_id)
      if invoice_info != 'Invoice not found':
        proceed =closing_invoice.balancingOwingPaid(invoice_info)
        if proceed == True:
          closing_invoice.updateObject()
          closing_invoice.updateJSONDoc()
        elif proceed == False :
          print("You don`t owe any money in this invoice")
      else:
        print("Invoice not found")    
    elif user_task == '3':
      newReturn = Return()
      newReturn.loadData()
      inv_id = input("Please enter the Invoice Number (Number only)  of the invoice you would like to process a return: ")
      return_info = newReturn.locateInvoice(inv_id)
      if return_info != 'Invoice not found':
        return_prod_id = input("Please enter the prod id of the product being returned:  ")
        return_qty = int(input("Please enter the quantity of the product being returned:  "))
        return_product_located = newReturn.prodReturns(return_prod_id,return_qty)
        if return_product_located == True:
          newReturn.updateObject()
          newReturn.updateJSONDoc()
        else:
          print("The product wasn`t sold as part of this order")
    elif user_task == '4':
      quoteReq = Sale()
      prod_id=quoteReq.getProductID()
      if prod_id != 'quit':
        prod_qty = quoteReq.getProductQuantity()
        if prod_qty != 'quit':
          prod_text = quoteReq.getProductInfo(prod_id,prod_qty)
          quoteReq.printQuoteInfo(prod_text)
        else:
          valid = False
          break
      else:
        valid = False
        break
        