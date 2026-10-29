print("Para encerrar o progama, pro favor digite 0 (zero)")

# inicio do loop
while True:

  #valor compra
  valor_compra = float(input("Digite o valor da compra (R$): "))
  while valor_compra < 0:
     print("O valor que vc digitou é negativo, tente novamente.")
     valor_compra = float(input("Digite o valor da compra (R$): "))

  if valor_compra == 0:
       break
   #idade
  idade_cliente = int(input("Digite a idade do cliente: "))
  while idade_cliente < 0:
      print("Sua idade é invalida, tente novamente.")
      idade_cliente = int(input("Digite a idade do cliente: "))

  #aplicacao de desconto
  preco_final = valor_compra
  if idade_cliente >= 65:
    preco_final = valor_compra * (1 - (20 / 100))

  if preco_final > 100:
        preco_final = preco_final *(1 - (10 / 100))

  print(f"o valor a pagar é: R${preco_final}")


print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Idade do cliente: {idade_cliente} anos")