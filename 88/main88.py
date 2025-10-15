n = int(input('введіть число: '))
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
result = a + b + c + d
print(result)