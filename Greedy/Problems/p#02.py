'''

#02 곱하기 혹은 더하기

입력 예시:
02984

567

출력 예시:
576

210

'''

input_list = list(map(int, input()))
print(input_list)

if input_list[0] == 0:
    result = 1
else:
    result = input_list[0]

for i in range(1, len(input_list)):

    if input_list[i] == 0:
        continue
    
    if (i+1) < len(input_list) and input_list[i+1] == 0:
        continue

    result *= input_list[i]

print(result)