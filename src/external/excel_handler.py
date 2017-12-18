from shutil import copyfile
import xlsxwriter
import datetime


def create_docs():
    todays_date = "'" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + '.xlsx' + "'"
    workbook = xlsxwriter.Workbook(todays_date)
    worksheet = workbook.add_worksheet()
    return todays_date


def copy_template_content():
    copyfile("template.xlsx", create_docs())
