#xlrd, xlutils and xlwt modules need to be installed.  
#Can be done via pip install <module>
from xlrd import open_workbook
import datetime
from xlutils.copy import copy

rb = open_workbook("src/external/template.xls", formatting_info=True, on_demand=True)
wb = copy(rb)
sheet = wb.get_sheet(0)

row = 1
col = 0


def write_single_line(line):
    global row
    global col
    for line_element in line:
        sheet.write(row, col, str(line_element))
        col += 1
    col = 0
    row += 1    


def close_workbook():
    wb.save(datetime.datetime.today().strftime('%Y-%m-%d') + ".xls")