students =[
    {"id":101,"name":"Anu","department":"CS"},
    {"id":102,"name":"Angel","department":"CS"},
    {"id":103,"name":"Anju","department":"CS"}
]

while True:
    choice = int(input("1. Add a student\n2. Display a student\n3. Edit a student\n4. Delete a student\n5. Exit\n6.Enter your choice:"))
    match choice :

        case  1:
            name =input("Enter a name:")
            std_id = int(input("Enter the id:"))
            department = (input("Enter department:"))
            students.append({"id":std_id, "name":name, "department":department})
        case 2:
            print(f'{"ID":^4}{"Name":^10}{"Department":^10}')
            print('-'*25)
            for student in students:
                print(f"{student['id']:<4}{student['name']:<10}{student['department']:<10}")
            print('-'*25)
            for student in students:
                print(f"Total Count: {len(students):>7}")
        case 3:
            print(f"{"ID":^4}{"Name":^10}{"Department":^10}")
            print('-'*25)
            for student in students:
                 print(f"{student['id']:<4:}{student['name']:<10}{student['department']:<10}")
            print('-'*25)   
            id = int(input("Enter the id of the student that you want to edit:"))
            edit_student = None
            for student in students:
                if student['id'] == id:
                   edit_student = student
            edit_student['name'] = input("Enter the new name: ")
            edit_student['department'] = input("Enter the new department: ")


