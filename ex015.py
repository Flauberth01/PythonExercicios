#Programa que pergunte a quantidade de Km por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado e calcule.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2F}'.format(pago))
