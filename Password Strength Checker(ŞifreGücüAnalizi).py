import string   

password = input("Enter your password: ")

upper_case  = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case  = any([1 if c in string.ascii_lowercase else 0 for c in password])
digit       = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, digit]

length = len(password)

score = 0

#Google password common.txt
with open("common.txt", "r") as f:
    common_passwords = f.read().splitlines()

if password in common_passwords:
    print("Password was found in common passwords list. Choose a different password. Score: 0 / 7")
    exit


    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 17:
        score += 1
    if length >= 20:
        score += 1
print(f"Password length is {str(length)}, adding {str(score)} points!")      

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters)-1)} points!")    

if score < 4:
    print(f"Password is weak. Score: {str(score)} / 7")
elif score == 4:
    print(f"Password is okay. Score: {str(score)} / 7")
elif score == 5:
    print(f"Password is decent. Score: {str(score)} / 7")
elif score > 6:    
    print(f"Password is strong. Score: {str(score)} / 7")
    