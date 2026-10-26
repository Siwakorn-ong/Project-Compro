def add_productinfo(productfile, salefile):
    product_data = []
    sale_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    with open(salefile, "r", encoding = 'UTF_8') as saleFile:
        for a in saleFile:
            sale_data.append(a.strip('\n').split('|'))
    print("VVV Enter product information VVV")
    prod_id = input('Product ID: ')
    
    with open(productfile, "a", encoding = 'UTF_8') as prodFile:
        check_id = [i for i in product_data[0]]
        if prod_id not in check_id:
            prod_name = input('Product Name: ')
            prod_price = input('Product Price: ')
            prodFile.write(prod_id+ '|' +prod_name+ '|' +prod_price+ '\n')
            with open(productfile, "r", encoding = 'UTF_8') as prodFile:
                for i in prodFile:
                    product_data.append(i.strip('\n').split('|'))
            print("VVV Enter sale information VVV")
            sale_amount = input(f"Sale amount of {prod_id} ({prod_name}): ")
            sale_income = str(float(prod_price) * float(sale_amount))
            with open(salefile, "a", encoding = 'UTF_8') as saleFile:
                saleFile.write(sale_amount+ '|' +sale_income+ '\n')
            with open(salefile, "r", encoding = 'UTF_8') as saleFile:
                for a in saleFile:
                    sale_data.append(a.strip('\n').split('|'))
                saleFile.close()
        else:
            print('Product ID already exists in the file.')
        prodFile.close()
    
    print("Product & sale information saved.")



def report_product(productfile, salefile):
    product_data = []
    sale_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    with open(salefile, "r", encoding = 'UTF_8') as saleFile:
        for a in saleFile:
            sale_data.append(a.strip('\n').split('|'))
    title = f'{'\nProduct & Sale Report'}'
    head = ('-'*66 + '\n')
    head += '|No.|  ID   |      Name        |    Price   |  Sold |   Total    |\n'
    head += ('-'*66 )
    
    body = ''
    n = 1
    list_number = 0
    alltotal = 0
    
    for i in product_data , a in sale_data:
        price = float(product_data[list_number][2])
        qty = float(sale_data[list_number][0])
        prod_total = float(sale_data[list_number][1])
        body += f'| {n} | {product_data[list_number][0]:^5} | {product_data[list_number][1]:<16} | {price:^10,.2f} | {qty:^5.0f} |'
        body += f' {prod_total:^10,.2f} |\n'
        list_number += 1
        n += 1
        alltotal += prod_total
    body += '-'*66 + '\n'
    body += f'\nTotal income for the day: {alltotal:,.2f} Baht.\n'
    print(title)
    print(head)
    print(body)    
