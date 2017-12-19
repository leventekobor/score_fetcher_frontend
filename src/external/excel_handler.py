from shutil import copyfile
import xlsxwriter
import datetime

sheet = None
row = 1
col = 0


def create_docs():
    todays_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + '.xlsx'
    workbook = xlsxwriter.Workbook(todays_date)
    worksheet = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet()

    worksheet.set_column('A:M', 10)
    worksheet.set_row(1, 100)

    return worksheet, todays_date


def copy_template_content(doc_name):
    copyfile("src/external/template.xlsx", doc_name)


def get_sheet():
    copy_template_content("temp")
    sheet, doc_name = create_docs()
    return sheet

sheet = get_sheet()
workbook = xlsxwriter.Workbook("temp")


def write_single_line(params, row):
    print("pm: " + str(params) + str(row))
    col = 0
    if sheet:
        row += 1
        for index, data in enumerate(params):
            print(index, data)
            sheet.write(row + 1, index, data)
    else:
        print("baj")

def close_workbook():
    workbook.close()
