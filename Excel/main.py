import openpyxl

wb = openpyxl.load_workbook('PGCE Maths Audit scores 2022(1-99).xlsx')
print(type(wb))  # returns <class 'openpyxl.workbook.workbook.Workbook'>  i.e. the datatype is workbook

sheet = wb['Sheet1']

print(sheet['D2'].value)  # returns

d = sheet['D2']

print(f'Row {d.row}, column {d.column} is {d.value}')  # d.column returns the column number
# the above returns: Row 2, column 4 is Hannah2.Sheehan@live.uwe.ac.uk

print(d.column_letter)  # use this to return the column letter

