result=0

for i in range(1,101):
    if i % 3 == 0:
        result += i
        
print(f"3의 배수 합: {result}")