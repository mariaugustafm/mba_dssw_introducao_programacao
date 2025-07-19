# Dados do Cilindro

raio = float(input("Digite o Raio da base: "))
altura = float(input("Digite a Altura do Cilindro: "))
PI = 3.14

a_base = PI * (raio ** 2)
a_lat = 2 * PI * raio * altura
a_c = a_base + a_lat

# Problema
quan_lit = a_c / 3
qnt_lat = quan_lit /5
custo = qnt_lat * 50

print(f'Quantidade de Latas: {qnt_lat}')
print(f'Custo: {custo}')

