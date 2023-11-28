command = input()
companies = {}
while command != 'End':
    company_name, employee_id = command.split('->')
    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(employee_id)
    else:
        for item in companies.items():
            if employee_id in companies[company_name]:
                break
            else:
                companies[company_name].append(employee_id)

    command = input()

for company, id in companies.items():
    print(company)
    for value in id:
        print(f'--{value}')