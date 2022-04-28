#Programa que converte uma temperatura de graus Celsius e converta para graus Fahrenheit.

C = float(input('Informe a temperatura em °C: '))
F = 9 * C / 5 + 32
print('A temperatura de {}°C Corresponde a {}°F! '.format(C, F))
