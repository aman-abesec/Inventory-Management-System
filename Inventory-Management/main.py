#importig json package
import json
#Function to Create Line
def line():
    print("===========================================================================")

#Function to create heading
def heading(str):
    print("                            "+str)


line()
heading("INVENTARY MANAGEMENT")
line()
while(1):
    print("\n\t\tEnter 1 for See the Products")
    print("\t\tEnter 2 for Update the Products")
    print("\t\tEnter 3 for Puchase the Products")
    print("\t\tEnter 4 for See Sales Products")
    print("\t\tEnter 5 for Exit")
    choice=input("\n\t\tEnter Your Choice : ")

    #For See the Product
    if(choice=='1'):
        record_file = open("record.json",'r')
        record_data = record_file.read()
        records= json.loads(record_data)
        heading("         PRODUCTS LIST")
        print("\n\t\t%-15s %-20s %-15s %-10s"% ("Product Id." ,"Product Name","Price", "Quantity"))
        for i in records.keys():
            print("\t\t%-15s %-20s %-15f %-10d"% (i,records[i]['name'],records[i]['pr'],records[i]['qn']))
        record_file.close()

    elif(choice=='2'):
        record_file = open("record.json",'r')
        record_data = record_file.read()
        record_file.close()
        records= json.loads(record_data)
        prod_id =input("\t\tEnter product id : ")
        product_name = input("\t\tEnter name : ")
        product_pr = float(input("\t\tEnter price : "))
        product_qn = int(input("\t\tEnter quantity : "))
        records[prod_id] = {'name': product_name, 'pr': product_pr, 'qn': product_qn}
        all_data = json.dumps(records)
        record_file = open("record.json",'w')
        record_file.write(all_data)
        record_file.close()

    elif(choice=='3'):
        record_file = open("record.json",'r')
        record_data = record_file.read()
        record_file.close()
        records= json.loads(record_data)
        ui_prod  = input("\t\tEnter the product_Id: ")
        ui_quant = int(input("\t\tEnter the quantity: "))
        #For validating the number of product is more or not
        if(records[ui_prod]['qn']>=ui_quant):
            print("\n\t\t\t|Product: ", records[ui_prod]['name'])
            print("\t\t\t|Price: ", records[ui_prod]['pr'])
            print("\t\t\t|Billing Amount: ", records[ui_prod]['pr'] * ui_quant)
            print("\t\t\t|Please Visit Again (*_*) ")
            records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant

            record_file = open("record.json",'w')
            all_data = json.dumps(records)
            record_file.write(all_data)
            record_file.close()

            #Opening sales.json data in read mode
            sales_file = open("sales.json",'r')
            sales_data= sales_file.read()
            sales_file.close()
            record= json.loads(sales_data)
            record[len(record)+1] = {'name':records[ui_prod]['name'], 'pr':records[ui_prod]['pr'], 'qn':ui_quant}
            #Opening sales.json file in writing mode to update the sales product
            sales_file = open("sales.json",'w')
            all_data_sales = json.dumps(record)
            sales_file.write(all_data_sales)
            sales_file.close()
        else:
            print("\n\t\t Sorry!! We have only "+str(records[ui_prod]['qn'])+" Product!!")

    #To see the sale.json data
    elif(choice=='4'):
        sales_file = open("sales.json",'r')
        sales_data = sales_file.read()
        records= json.loads(sales_data)
        heading("SELL PRODUCTS LIST")
        print("\n\t\t%-15s %-20s %-15s %-10s"% ("Product Id." ,"Product Name","Price", "Quantity"))
        for i in records.keys():
            print("\t\t%-15s %-20s %-15f %-10d"% (i,records[i]['name'],records[i]['pr'],records[i]['qn']))
        sales_file.close()

    #To Exit
    elif(choice=='5'):
        break

    #Invalid Choice
    else:
        print("Invalid Choice!!")
