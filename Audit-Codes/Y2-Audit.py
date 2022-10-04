import openpyxl
from openpyxl import Workbook
# from openpyxl.utils import column_index_from_string, get_column_letter   - this is useful to get the column number of e.g 'GA'

import pandas as pd

# ------------------------- Convert from xls to xlsx ----------------------------------------------------
# Copy the downloaded spreadsheet data from the original xls file and paste it into a new xlsx file

# --------------- Create the empty spreadsheet and Add the top row--------------------------------

wb_empty = Workbook()
ws_empty = wb_empty.active
ws_empty.title = 'Scores'
ws_empty.append(["Name", "Email", "P-Group", "Number & Calc", "Shape, Space & Measure", "Data Handling", "Total"])

# -------------------------- Using pandas gather data from the blackboard sheet---------------------------------------

ws_dataframe = pd.read_excel('./Original Audit Files/Y2 Maths Audit Download.xlsx')

for (index, row) in ws_dataframe.iterrows():
    row_info = []
    num_calc_score = 0
    for i in range(1, 15):
        num_calc_score += row[f'Auto Score {i}']
        num_calc_decimal_score = round(num_calc_score / 25, 2)

    shape_score = 0
    for i in range(15, 25):
        shape_score += row[f'Auto Score {i}']
        shape_decimal_score = round(shape_score / 18, 2)

    stats_score = 0
    for i in range(25, 31):
        stats_score += row[f'Auto Score {i}']
        stats_decimal_score = round(stats_score / 12, 2)

    total_score = 0
    for i in range(1, 31):
        total_score += row[f'Auto Score {i}']
        total_decimal_score = round(total_score / 55, 2)

    if row['Answer 31'] == '<Unanswered>':
        p_group = 'unknown'
        email = 'unknown'
    else:
        p_group = 'P' + row['Answer 31'].split(',')[0]
        email = row['Answer 31'].split(',')[1] + '@live.uwe.ac.uk'

    row_info = [(row['Last Name'] + ', ' + row['First Name']), email, p_group, num_calc_decimal_score,
                shape_decimal_score, stats_decimal_score, total_decimal_score]

    ws_empty.append(row_info)

wb_empty.save("./Cleaned Audit Files/Y2-Results-2022.xlsx")

