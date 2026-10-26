from Modules import *
def main():
    product_txt = 'productfile.txt'
    sale_txt = 'salefile.txt'
    menu = ('-'*16 + '\n| Product Menu |\n' + '-'*16)
    menu += f"\n 0. Exit Program\n 1. Add Product Information\n 2. Edit Product Information\n 3. Delete Product\n 4. Show Report\n 5. Add sale\n 6. Sale report\n 7. Daily sales summary\n 8. Sales summary by product"
    while True:
        print(menu)
        choice = input("\nChoose an Option: ")
        if choice == "0": break
        elif choice == "1": add_productinfo(product_txt, sale_txt)
        elif choice == "2": edit_productinfo(product_txt, sale_txt)
        elif choice == "3": del_productinfo(product_txt, sale_txt)
        elif choice == "4": report_productlist(product_txt)
        elif choice == "5": add_saleinfo(product_txt, sale_txt)
        elif choice == "6": report_sale(product_txt, sale_txt)
        elif choice == "7": report_daily(sale_txt)
        elif choice == "8": report_product(product_txt, sale_txt)
        else:
            print('Not an option, pick again.')
    print('Exiting Program...')

if __name__ == '__main__':
    main()
