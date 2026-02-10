n = int(input("enter no of students "))
marks = [0] * n
valid_num = 0
failed_num = 0
for i in range(n):
    marks[i] = int(input("enter marks of each student "))

for i in range(n):
    if marks[i] < 0 or marks[i] > 100:
        print(marks[i],"-->invalid ")

    elif marks[i] >= 90 and marks[i] <= 100:
        print(marks[i], "--> EXCELLENT")
        valid_num += 1

    elif marks[i] >= 75 and marks[i] <= 89:
        print(marks[i], "--> VERY GOOD")
        valid_num += 1
    elif marks[i] >= 60 and marks[i] <= 74:
        print(marks[i], "--> GOOD")
        valid_num += 1
    elif marks[i] >= 40 and marks[i] <= 59:
        print(marks[i], "--> AVERAGE")
        valid_num += 1
    elif marks[i] >= 0 and marks[i] <= 39:
        print(marks[i], "--> FAIL")
        valid_num += 1
        failed_num +=1


print("Total valid students :", valid_num)
print("Total failed students:",failed_num)
