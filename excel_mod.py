import xlsxwriter
import datetime


todays_date = "'" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + '.xlsx' + "'"
workbook = xlsxwriter.Workbook(todays_date)
worksheet = workbook.add_worksheet()

worksheet.set_column('A:M', 10)
worksheet.set_row(0, 100)

format = workbook.add_format({'bg_color': 'yellow', 'bold': True})
format.set_align('vjustify')

worksheet.write_string(0, 0, 'Bajnokság', format)
worksheet.write_string(0, 1, 'Meccs', format)
worksheet.write_string(0, 9,'Egymás ellen legutóbbi 5 meccs döntetlen', format)
worksheet.write_string(0, 10, 'Egymás ellen legutóbbi 5 meccs nem döntetlen',    format)

format = workbook.add_format({'bg_color': 'blue', 'bold': True})
format.set_align('vjustify')

worksheet.write_string(0, 2, 'H/V', format)
worksheet.write_string(0, 3, 'Meccsszám', format)
worksheet.write_string(0, 4,'Haza legutóbbi 5 meccs döntetlen' ,    format)
worksheet.write_string(0, 5, 'Haza legutóbbi 5 meccs nem döntetlen',    format)

format = workbook.add_format({'bg_color': 'green', 'bold': True})
format.set_align('vjustify')

worksheet.write_string(0, 6, 'Meccsszám', format)
worksheet.write_string(0, 7,'Vendég legutóbbi 5 meccs döntetlen' ,    format)
worksheet.write_string(0, 8, 'Vendég legutóbbi 5 meccs nem döntetlen',    format)
worksheet.write_string(0, 11, 'Százalék', format)

workbook.close()
