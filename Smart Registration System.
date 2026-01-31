stuID = input("enter your student ID")
Email = input("enter your Email ID")
password = input("enter your Password")
refer = input("enter your Referral code")

valid_student = True
valid_email = True
valid_password = True
valid_referral_code = True

#student ID validation
if stuID == "" or stuID[0:3] != "CSE" or stuID[3] != "-" or not stuID[4:7].isdigit() or len(stuID) != 7:
    valid_student = False


#Email id validation
if not len(Email) or " " in Email or Email[0] == "." or Email[0] == "@" or "@" not in Email or "." not in Email or Email[-4:] != ".edu" :
    valid_email = False

#password validation
if len(password) < 8 or password == "" or password[0] != password[0].upper() or not("0" in password or "1" in password or "2" in password or
            "3" in password or "4" in password or "5" in password or
            "6" in password or "7" in password or "8" in password or "9" in password):
    valid_password =False
#REFERAl code
if refer[0:3] != "REF" or not refer[3:5].isdigit() or len(refer) != 6 or refer[5] != "@":
    valid_referral_code = False

if valid_student and valid_email and valid_password and valid_referral_code:
    print("ACCEPTED")
else :
    print("REJECTED")

