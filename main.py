soma =0
multiplicacao = 1
total = []
n=1
for x in range(5):
    num = int(input('digite o {}° numero:  '.format(n)))
    total.append(num)
    multiplicacao *= num
    soma += num
    n +=1
    
print('''
      a soma é {}
      a multiplicação é {}
      e os numeros são {}'''.format(soma,multiplicacao,total))