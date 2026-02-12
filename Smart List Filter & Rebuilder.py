n = int(input("Enter number of elements: "))
data = [""] * n

for i in range(n):
    data[i] = input("Enter element: ")

number_list = [0] * n
string_list = [""] * n

num_index = 0
str_index = 0

for i in range(n):
    if data[i].isdigit():
        number_list[num_index] = int(data[i])
        num_index += 1
    elif data[i] != "":
        string_list[str_index] = data[i]
        str_index += 1

if num_index > 0:
    for i in range(1, num_index):
        number_list[i - 1] = number_list[i]
    num_index -= 1

if str_index > 0:
    for i in range(1, str_index):
        string_list[i - 1] = string_list[i]
    str_index -= 1

print("Numbers List:", number_list[:num_index])
print("Strings List:", string_list[:str_index])
print("Total Numbers:", num_index + 1)
print("Total Strings:", str_index + 1)
