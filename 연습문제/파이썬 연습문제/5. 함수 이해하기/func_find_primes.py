def find_primes(start, end):
    arr = [i for i in range(start, end+1)]
    print(arr)
    
    result = []
    for i in range(len(arr)):
        if arr[i]==2: # 2는 소수라 추가
            result.append(arr[i])
            continue
        
        elif arr[i]<2: # 0, 1 고려 안하고 음수도 제외
            continue
        
        else:
            for j in range(2, arr[i]): # 어차피 arr 선언할 때 정렬되니까 현재 숫자보다 작은 수로만 나눔
                if arr[i] % j == 0:
                    break
            else:
                result.append(arr[i])
    return result
                




print(find_primes(9, 20))