#xlrd, xlutils and xlwt modules need to be installed.  
#Can be done via pip install <module>
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("src/external/template.xlsx")
wb = copy(rb)

s = wb.get_sheet(0)
s.write(0,0,'A1')
wb.save('names.xls')