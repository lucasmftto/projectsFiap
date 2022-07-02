import excel.readExcel as read


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def soma(number1, number2):
    print(number1 + number2)


def subtrai(number1, number2):
    print(number1 - number2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Excel')
    read.readExcel()
    read.readExcelBySheetIndex(1)
    read.readExcelBySheetIndexAndPrintColumn(1, "Aa")
