my_dict = {"Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Diana": 92}
name = input("Enter the name of the student:")
if  name in my_dict:
    print("Marks of {} are:{}".format(name, my_dict[name]))
else:
    print("Student not found")
