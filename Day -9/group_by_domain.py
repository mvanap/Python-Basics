def group_by_department(employee_details):
    result = {}
    for emp in employee_details:

        dept = emp["dept"]
        name = emp["name"]
        if dept not in result:
            result[dept] = []
        result[dept].append(name)
    return result


employees = [
    {"name": "A", "dept": "IT"},
    {"name": "B", "dept": "HR"},
    {"name": "C", "dept": "IT"}
]

result = group_by_department(employees)
print(result)