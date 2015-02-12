with open("students.txt", mode="r", encoding="utf-8") as students:
    count = 1
    for name in students:
        print("{0}. {1}".format(count,name), end="")
        count += 1

