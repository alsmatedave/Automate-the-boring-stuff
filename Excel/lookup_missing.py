import openpyxl

wb = openpyxl.load_workbook('python lookup sheet.xlsx')

sheet = wb['Sheet1']

done_audit_list = []
full_student_list = []

# enter C range
for cellObject in sheet['C2': 'C3']:
    for email in cellObject:
        done_audit_list.append(email.value)

# enter A range
for cellObject in sheet['A2': 'A6']:
    for email in cellObject:
        full_student_list.append(email.value)

not_done_audit = []

for student in full_student_list:
    if student not in done_audit_list:
        not_done_audit.append(student)

formatted_email_string = ''

for email in not_done_audit:
    formatted_email_string += f'{email}; '

print(formatted_email_string)






