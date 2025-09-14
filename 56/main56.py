n = int(input('введіть число: '))


if n > 0 and n % 1 == 0:
    print((n // 10) % 10)
else:
    print('потрібно натуральне число')