# usando format

a = 'A'
b = 'B'
c = 1.1

formato_1 = 'a={} b={} c={:.2f}'
print(formato_1.format(a,b,c))

formato_2 = 'a={0} b={1} c={2:.2f} d={1} e={0}'
print(formato_2.format(a,b,c))

formato_2 = 'a={valor_1} b={valor_2} c={valor_3:.2f} d={valor_2} e={valor_1}'
print(formato_2.format(valor_1=a,valor_2=b,valor_3=c))