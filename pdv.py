historico = []
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

  #bonus quantidade de item
  quantidade = int(input("Digite a quantidade de itens: "))
  while quantidade < 1:
        print("Aviso: a quantidade deve ser pelo menos 1. Tente novamente.")
        quantidade = int(input("Digite a quantidade de itens: "))

  #bonus cupom
  cupom = input("Digite o cupom (ou Enter para pular): ").strip().upper()

  #aplicacao de desconto
  preco_final = valor_compra
  if idade_cliente >= 65:
    preco_final = valor_compra * (1 - (20 / 100))

  if preco_final > 100:
        preco_final = preco_final *(1 - (10 / 100))

  #aplicacao do desconto bonus
  if quantidade > 3:
        preco_final = preco_final * (1 - (5 / 100))
 
  #bonus cupom de fidelidade (10% extra)
  if cupom == "FIDELIDADE10":
        preco_final = preco_final * (1 - (10 / 100))
        print("Cupom FIDELIDADE10 aplicado!")
  elif cupom != "":
        print("Cupom inválido, ignorado.")
 

  print(f"o valor a pagar é: R${preco_final}")


  #quarda no histórico
  historico.append((valor_compra, preco_final))

#resumo do dia
total_bruto = 0
total_final = 0
for bruto, final in historico:
    total_bruto += bruto
    total_final += final

total_descontos = total_bruto - total_final

print("-----RESUMO DO DIA-----")
print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto:           R$ {total_bruto:.2f}")
print(f"Total de descontos:    R$ {total_descontos:.2f}")
print(f"Total final:           R$ {total_final:.2f}")



#bonus salvar o resumo em resumo.txt
arquivo = open("resumo.txt", "w", encoding="utf-8")
arquivo.write("-----RESUMO DO DIA-----")
arquivo.write("Compras:\n")
numero = 1
for bruto, final in historico:
    arquivo.write(f"Compra {numero}: bruto R$ {bruto:.2f} -> final R$ {final:.2f}\n")
    numero += 1
arquivo.write("\n")
arquivo.write(f"Quantidade de compras: {len(historico)}\n")
arquivo.write(f"Total bruto:           R$ {total_bruto:.2f}\n")
arquivo.write(f"Total de descontos:    R$ {total_descontos:.2f}\n")
arquivo.write(f"Total final:           R$ {total_final:.2f}\n")
arquivo.close()
 
print("\nResumo salvo em resumo.txt")