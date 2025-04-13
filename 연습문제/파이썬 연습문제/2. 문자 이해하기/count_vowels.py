# count_vowels.py

str = "Python is awesome"

result=0
for i in range(len(str)):
    if str[i]=='a' or \
        str[i]=='e' or \
            str[i]=='i' or \
                str[i]=='o' \
                    or str[i]=='u':
        result+=1
print(f"모음 개수: {result}")