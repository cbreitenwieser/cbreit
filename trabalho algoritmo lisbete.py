ano = int(input('Forneça o ano'))

g = (ano%19)+1
print(g)

seculo = ( ano//100 ) + 1 
print(seculo)

x = (3 * seculo // 4) - 12
print(x)

a = (8 * seculo) + 5
print(a)

z = (a // 25) - 5 
print(z)

e = (11*g + 20 + z - x) % 30 
print(e)

if e == 25 and g > 11 or e==24:
  e = e + 1 
  print(e)
n = 44 - e
print(n)
 
if n < 21:
  n = n + 30
  print(n)

d = 5*ano//4 #10
print(d)

d = d - (x+10) 
print (d)

h = (n + 7) - (d+n)%7
print(h)

if (h>31):
  diapascoa = h - 31
  mespascoa = 4
elif (h<=31):
  diapascoa = h
  mespascoa = 3

print(diapascoa,mespascoa)
