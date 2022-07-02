import pandas as pd
import csv


def readExcel():
    df = pd.read_excel('Exemplo.xlsx')
    print(df)


def readExcelBySheetIndex(index):
    df_sheet_index = pd.read_excel('Exemplo.xlsx', sheet_name=index)
    print(df_sheet_index)


def getData():
    data = [
        ['Albania', 28748, 'AL'],
        ['Algeria', 2381741, 'DZ'],
        ['American Samoa', 199, 'AS'],
        ['Andorra', 468, 'AD'],
        ['Angola', 1246700, 'AO']
    ]
    return data


def readExcelBySheetIndexAndPrintColumn(sheetIndex, columnName):
    df_sheet_index = pd.read_excel('Exemplo.xlsx', sheet_name=sheetIndex)
    print(df_sheet_index[columnName].tolist())
    # df_sheet_index[columnName].to_csv("out.csv", sep=';', encoding='utf-8', index=False)
    header = df_sheet_index[columnName].tolist()
    with open('out.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter=';')

        # write the header
        writer.writerow(header)

        # write the data
        # writer.writerow(getData())
        writer.writerows(getData())
