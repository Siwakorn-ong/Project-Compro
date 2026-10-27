import datetime

def add_productinfo(productfile, salefile):
    product_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    print("\n< Enter product information >")
    prod_id = input('Product ID: ')
    check_id = [i[0] for i in product_data]
    if prod_id not in check_id:
        prod_name = input('Product Name: ')
        prod_price = input('Product Price: ')
        confirm = input("confirm (Y/N): ").lower()
        if confirm == "y":
            with open(productfile,"a",encoding="utf-8") as fin:
                fin.write("|".join((prod_id,prod_name,prod_price))+"\n")
            print("Product & sale information saved.")
        elif confirm == "n":
            print("Cancel")
        else: print("No Choice")
    else:
        print('\nProduct ID already exists in the file.')
    prodFile.close()

def edit_productinfo(productfile):
    product_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    print("\n< Edit Product >")
    prod_id = input('Product ID: ')
    for i, prod in enumerate(product_data):
        if prod_id == prod[0]:
            prod_name = input('New Product Name: ')
            prod_price = input('New Product Price: ')
            print("< Enter sale information >")
            sale_amount = input(f"Sale amount of {prod_id} ({prod_name}): ")
            sale_income = str(float(prod_price) * float(sale_amount))
            confirm = input("confirm (Y/N): ").lower()
            if confirm == "y":
                product_data[i] = [prod_id, prod_name, prod_price]
                with open(productfile, "w", encoding = 'UTF_8') as prodFile:
                    for p in product_data:
                        prodFile.write('|'.join(p) + '\n')
                print("\nEdit product & sale information saved.")
            elif confirm == "n":
                print("Cancel")
            else: print("No Choice")
            break
    else:
        print('Product ID not found in the file.')

def del_productinfo(productfile, salefile):
    product_data = []
    sale_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    with open(salefile, "r", encoding = 'UTF_8') as saleFile:
        for a in saleFile:
            sale_data.append(a.strip('\n').split('|'))
    print("\n< Delete Product >")
    prod_id = input('Product ID: ')
    for i, prod in enumerate(product_data):
        if prod_id == prod[0]:
            count = len([s for s in sale_data if s[1] == prod_id])
            print(f"Delete No.{i + 1} : {prod[0]} {prod[1]} (and {count} sale record(s) of this product)")
            confirm = input("confirm (Y/N): ").lower()
            if confirm == "y":
                del product_data[i]                         
                sale_data = [s for s in sale_data if s[1] != prod_id]
                with open(productfile, "w", encoding = 'UTF_8') as prodFile:
                    for p in product_data:
                        prodFile.write('|'.join(p) + '\n')
                with open(salefile, "w", encoding = 'UTF_8') as saleFile:
                    for s in sale_data:
                        saleFile.write('|'.join(s) + '\n')
                print("Delete product information complete.")
            elif confirm == "n":
                print("Cancel")
            else: print("No Choice")
            break
    else:
        print('Product ID not found in the file.')

def report_product(productfile, salefile):
    product_data = []
    sale_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            if i.strip() != '':
                product_data.append(i.strip('\n').split('|'))
    with open(salefile, "r", encoding = 'UTF_8') as saleFile:
        for a in saleFile:
            if a.strip() != '':
                sale_data.append(a.strip('\n').split('|'))
    sold = {}                                                   
    for sale in sale_data:
        row = sold.setdefault(sale[1], [0.0, 0.0])
        row[0] += float(sale[2])
        row[1] += float(sale[3])
    title = f"\n{'Product & Sale Report':^51}"
    head = ('-'*51 + '\n')
    head += '|No.|  ID   |      Name        |  Sold |   Total  |\n'
    head += ('-'*51 )

    body = ''
    n = 1
    alltotal = 0

    for prod in product_data:
        price = float(prod[2])
        qty, prod_total = sold.get(prod[0], [0.0, 0.0])
        body += f'|{n:^3}| {prod[0]:^5} | {prod[1]:<16} | {qty:^5.0f} |'
        body += f' {prod_total:^8,.2f} |\n'
        n += 1
        alltotal += prod_total
    body += '-'*51 + '\n'
    body += f'\nTotal income of all sales: {alltotal:,.2f} Baht.\n'
    print(title)
    print(head)
    print(body)

def report_productlist(productfile):
    product_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            if i.strip() != '':
                product_data.append(i.strip('\n').split('|'))
    title = f"\n{'Product Report':^45}"
    head = ('-'*45 + '\n')
    head += '|No.|  ID   |      Name        |    Price   |\n'
    head += ('-'*45 )
    body = ''
    n = 1
    for prod in product_data:
        price = float(prod[2])
        body += f'|{n:^3}| {prod[0]:^5} | {prod[1]:<16} |  {price:^9,.2f} |\n'
        n += 1
    body += '-'*45 + '\n'
    body += f'\nTotal products: {len(product_data)}\n'
    print(title)
    print(head)
    print(body)

def add_saleinfo(productfile, salefile):
    product_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    print("\nEnter sale information")
    prod_id = input("Product ID: ")
    for prod in product_data:
        if prod_id == prod[0]:
            sale_date = input("Sale date (YYYY-MM-DD, ให้ Enter ถ้าเป็นวันนี้): ")
            if sale_date == "":
                sale_date = datetime.now().strptime("%Y-%m-%d")
                sale_amount = input(f"Sale amount of {prod_id} ({prod[1]}): ")
            sale_income = str(float(prod[2]) * float(sale_amount))
            confirm = input("confirm (Y/N): ").lower()
            if confirm == "y":
                with open(salefile, "a", encoding = 'UTF_8') as saleFile:
                    saleFile.write(sale_date + '|' + prod_id + '|' + sale_amount + '|' + sale_income + '\n')
                print("Sale information saved.")
            elif confirm == "n":
                print("Cancel")
            else: print("No Choice")
            break
    else:
        print("Prodeuct ID not found in the file.")

def report_sale(productfile, salefile):
    product_data = []
    sale_data = []
    with open(productfile, "r", encoding = 'UTF_8') as prodFile:
        for i in prodFile:
            product_data.append(i.strip('\n').split('|'))
    with open(salefile, "r", encoding = 'UTF_8') as saleFile:
        for a in saleFile:
            sale_data.append(a.strip('\n').split('|'))
    names = {}
    for prod in product_data:
        names[prod[0]] = prod[1]
    title = f"\n{'Sale Report':^66}"
    head = ('-'*66 + '\n')
    head += '|No.|    Date    |  ID   |      Name        |  Sold |   Total    |\n'
    head += ('-'*66 )
    body = ''
    n = 1
    alltotal = 0
    for sale in sale_data:
        qty = float(sale[2])
        sale_total = float(sale[3])
        body += f'|{n:^3}| {sale[0]:^10} | {sale[1]:^5} | {names.get(sale[1], "-"):<16} | {qty:^5.0f} | {sale_total:^10,.2f} |\n'
        n += 1
        alltotal += sale_total
    body += '-'*66 + '\n'
    body += f'\nTotal sale records: {len(sale_data)}, total income: {alltotal:,.2f} Baht.\n'
    print(title)
    print(head)
    print(body)

def report_daily(salefile):
    sale_data = []
    with open(salefile, "r", encoding = 'UTF_8') as saleFile:
        for a in saleFile:
            sale_data.append(a.strip("\n").split("|"))
    daily = {}
    for sale in sale_data:
        row = daily.setdefault(sale[0], [0, 0.0, 0.0])
        row[0] += 1
        row[1] += float(sale[2])
        row[2] += float(sale[3])
    title = f"\n{'Daily Sales Summary':^45}"
    head = ('-'*45 + '\n')
    head += '|    Date    | Sales | Items |    Income    |\n'
    head += ('-'*45 )
    body = ''
    t_count = 0
    t_items = 0
    alltotal = 0
    for day in sorted(daily):
        count, items, income = daily[day]
        body += f'| {day:^10} | {count:^5} | {items:^5.0f} | {income:^12,.2f} |\n'
        t_count += count
        t_items += items
        alltotal += income
    body += '-'*45 + '\n'
    body += f"| {'Total':^10} | {t_count:^5} | {t_items:^5.0f} | {alltotal:^12,.2f} |\n"
    body += '-'*45 + '\n'
    body += f'\nTotal income of all days: {alltotal:,.2f} Baht.\n'
    print(title)
    print(head)
    print(body)
