valor_compra = float(input("Digite o valor da compra (R$): "))

idade_cliente = int(input("Digite a idade do cliente: "))

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Idade do cliente: {idade_cliente} anos")

if idade_cliente >= 65:
    preco_final = valor_compra * (1 - (20 / 100))
    if preco_final > 100:
        preco_final = preco_final *(1 - (10 / 100))
print(f"o valor a pagar é: R${preco_final}")