def total_salary(employees):
    total = 0
    for emp in employees:
        total = total + emp["salary"]
    return total

employees = [
    {"name": "A", "salary": 1000},
    {"name": "B", "salary": 2000}
]

result = total_salary(employees)
print(result)