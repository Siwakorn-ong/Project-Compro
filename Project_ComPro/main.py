import Modules as m
def main():
    product_txt = 'productfile.txt'
    sale_txt = 'salefile.txt'
    menu = ('_'*17 + '\n| Product Menu |\n' + '_'*17)
    menu += '\n1. Add Product Information\n2. Show Report\n'
    menu += '3. Exit\nChoose an option: '
    while True:
        choice = input(menu)
        if choice == '1':
            m.add_productinfo(product_txt, sale_txt)
        elif choice == '2':
            m.report_product(product_txt, sale_txt)
        elif choice == '3':
            break
        else:
            print('Not an option, pick again.')
    print('Exiting Program...')

if __name__ == '__main__':
    main()