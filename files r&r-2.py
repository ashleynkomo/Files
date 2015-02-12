with open("students.txt", mode="a", encoding="utf-8") as students:
    newStudent = ""
    while newStudent != "-1":
        newStudent = input("Please enter a name(-1 to end): ")
        if newStudent != "-1":
            students.write("{0}\n".format(newStudent))

count = 1            
with open("students.txt", mode="r", encoding="utf-8") as students:
    for name in students:
        print("{0}. {1}".format(count,name), end="")
        count += 1

