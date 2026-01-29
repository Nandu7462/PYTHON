Fullname = input("Enter your FullName:")
Email = input("Enter your Email ID:")
number = input("Enter your Mobile Number:")
age = int(input("Enter your age:"))

valid_name = True
valid_email = True
valid_num = True
valid_Age = True

# Full Name validation
if Fullname[0] == " " or Fullname[len(Fullname) - 1] == " ":
    valid_name = False
elif Fullname.count(" ") == 0:
    valid_name = False

# Email validation
if not len(Email) or " " in Email or Email[0] == "." or Email[0] == "@" or "@" not in Email or "." not in Email:
    valid_email = False

# Mobile number validation
if len(number) != 10 or not number.isdigit() or number[0] == "0":
    valid_num = False

# Age validation
if age < 18 or age > 60:
    valid_Age = False

# Final output
if valid_name and valid_email and valid_num and valid_Age:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
