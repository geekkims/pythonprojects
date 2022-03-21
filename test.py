import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

supersecretdata = [34, 123, 4, 1234, 12, 34, 12, 41, 234, 123, 3, 56]

for i, e in enumerate(supersecretdata):
    sheet1.write(i, 1, e)

name = "random.xls"
