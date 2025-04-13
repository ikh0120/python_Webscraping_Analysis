#  email_validator.py

email = input("이메일 주소: ")
if '@' in email:
    user=email.split('@')[0]
    domain=email.split('@')[1]
    if '.' in domain:
        print("유효함")
    else:
        print("유효하지 않음")
else:
    print("유효하지 않음")