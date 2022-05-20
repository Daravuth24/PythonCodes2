num = int(input("Input a number: "))
i = 0
num_str = ""
j = ""

while num > 0:
    print(num)
    i = int(num % 10)
    num = num // 10
    num_str += str(i)

print(num_str)
