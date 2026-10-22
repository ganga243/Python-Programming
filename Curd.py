# names = ["Hethvik","Kithu"]
# while True:
#     choice = int(input("1. Add a name\n 2.Display name\n 3.Edit a name\n 4.Delete a name\n 5.Exit\n Enter your choice: "))
#     match choice:
#         case 1:
#             name = input("Enter a name:")
#             names.append(name)
#         case 2:
#             print(format("SI.No","<10"),format("Name"))
#             print('-'*25)
#             count = 1
#             for x in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#         case 3:
#             print(format("SI.No","<10"),format("Name"))
#             print('-'*25)
#             count = 1
#             for x in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#             edit_index = int(input("Enter the SI. no. of the name that you want to edit:"))-1
#             new_name = input("Enter the new name:")
#             names[edit_index] = new_name
#         case 4:
#              print(format("SI.No","<10"),format("Name"))
#              print('-'*25)
#              count = 1
#              for x in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#              delete_index = int(input("Enter the SI.no of the name that you want to edit: "))-1
#              names.pop(delete_index)
#         case 5:
#             break
#         case _:
#             print("Invalid entry")




names = ["Hethvik", "Kithu"]

while True:
    choice = int(input("1. Add a name\n2. Display name\n3. Edit a name\n4. Delete a name\n5. Exit\nEnter your choice: "))

    match choice:
        case 1:
            name = input("Enter a name: ")
            names.append(name)

        case 2:
            print(format("SI.No", "<10"), "Name")
            print("-" * 25)
            count = 1
            for x in names:
                print(format(count, "<10"), x)
                count += 1

        case 3:
            print(format("SI.No", "<10"), "Name")
            print("-" * 25)
            count = 1
            for x in names:
                print(format(count, "<10"), x)
                count += 1

            edit_index = int(input("Enter the SI. no. of the name that you want to edit: ")) - 1

            if 0 <= edit_index < len(names):
                new_name = input("Enter the new name: ")
                names[edit_index] = new_name
                print("Name updated successfully")
            else:
                print("Invalid SI.No")

        case 4:
            print(format("SI.No", "<10"), "Name")
            print("-" * 25)
            count = 1
            for x in names:
                print(format(count, "<10"), x)
                count += 1

            delete_index = int(input("Enter the SI.no of the name that you want to delete: ")) - 1

            if 0 <= delete_index < len(names):
                names.pop(delete_index)
                print("Name deleted successfully")
            else:
                print("Invalid SI.No")

        case 5:
            break

        case _:
            print("Invalid entry")
