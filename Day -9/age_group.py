def age_group(employee_data):
    young = 0
    adult = 0
    senior = 0
    for emp in employee_data:
        if emp["age"] < 25:
            young += 1
        elif emp["age"] <= 59:
            adult += 1
        else:
            senior += 1

    return {"young":young,"adult":adult,"senior":senior}


employees = [
    {"name": "A", "age": 22},
    {"name": "B", "age": 25},
    {"name": "C", "age": 35},
    {"name": "D", "age": 59},
    {"name": "E", "age": 60},
    {"name": "F", "age": 70}
]

result = age_group(employees)
print(result)