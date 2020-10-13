n = s = 0

while True:
    s += n
    n = int(input('diga um número: ou [999 para sair] '))
    if n == 999:
       break

print(s)
