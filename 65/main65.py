n = int(input('яку відстань проїде авто: '))
m = int(input('довжина: '))


x = m / n
f = int(x)
if x > f:
    print('стільки днів їхати', f + 1)
else:print('стільки днів їхати', f)
