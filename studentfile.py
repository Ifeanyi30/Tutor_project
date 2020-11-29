
student_file = {}
endf_input = '1'

for x in iter(list, 1):

    name = input("Enter a student name: ")

    st_id = int(input("Enter a student id number: "))
    student_file[name] = st_id
    endf_input = input("Add more student to file (type 1 for yes and 0 to end): ")
    if endf_input == '0':
        break

print("Search for Student")
search = int(input("Enter student id: "))
if search == 0:
    print("Sorry, no student with id of zero.")
    quit()
for key, value in student_file.items():
    if value == search:
        print(f"Student name: {key}")