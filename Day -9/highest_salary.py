def highest_salary(employee):
    if not employee:
        return None
    
    max_salary = employee[0]["salary"]
    max_salaried_emp = employee[0]
    
    for emp in employee:
        current_salary = emp["salary"]
        if current_salary > max_salary:
            max_salary = current_salary
            max_salaried_emp = emp
    return max_salaried_emp

employees = [
    {"name": "A", "salary": 1000},
    {"name": "B", "salary": 2000},
    {"name": "C", "salary": 1500}
]

result = highest_salary(employees)
print(result)