"""
This shows a pythonic way to use get_sheet to go through a single
page spreadsheet and load data into a Django model as a standalone django script
"""
import os
import sys
import pyexcel as pe

# load settings.py
proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoexcel.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application

# In essence you are actually loading up all the django components and settings
# so we gain access to djangos ORM
application = get_wsgi_application()
from sales.models import SaleSumary


def main(base_dir):
	# "example.csv","example.ods","example.xls", "example.xlsm"
	spreadsheet = pe.get_sheet(file_name=os.path.join(base_dir, "example.xlsx"))

	# columns() returns column based iterator, meaning it can be iterated
	# column by columz

	number_of_excel_rows = spreadsheet.number_of_rows() - 1
	print('number_of_rows {rows}'.format(rows=number_of_excel_rows))

	number_of_db_rows = 0
	# row_range() gives [0 .. number of rows]
	for r in spreadsheet.row_range():
		# column_range() gives [0 .. number of ranges

		if r == 0:
			continue

		# in the event a record already exists just update it
		salesRecord = SaleSumary.objects.update_or_create(
			order_date=spreadsheet.cell_value(r, 0), region=spreadsheet.cell_value(r, 1),
			rep=spreadsheet.cell_value(r, 2), item=spreadsheet.cell_value(r, 3),
			units=spreadsheet.cell_value(r, 4), unit_cost=spreadsheet.cell_value(r, 5), total=spreadsheet.cell_value(r, 6))
		if salesRecord:
			print(salesRecord)
			number_of_db_rows += 1

	# lets run a sanity check here and ensure excel count and db count match
	if number_of_excel_rows != number_of_db_rows:
		raise ValueError('number_of_excel_rows={excel_rows} inconsistent with db_rows={db_rows}'.format(
			excel_rows=number_of_excel_rows, db_rows=number_of_db_rows))


if __name__ == '__main__':
	main(os.getcwd())
