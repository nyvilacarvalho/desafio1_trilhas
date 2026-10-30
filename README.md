# Desafio Nível 1 — PDV com Descontos (Python)

## O que o código faz

Este programa simula um PDV (Ponto de Venda) de uma loja. Ele registra várias compras seguidas, aplica descontos progressivos de acordo com a idade do cliente e com o valor da compra, mostra o valor final a pagar em reais e, quando o operador encerra o dia, exibe um resumo com a quantidade de compras, o total bruto, o total de descontos concedidos e o total final.

## Como ele faz

1. O código cria uma lista vazia (`historico`) para guardar as compras do dia.
2. Entra em um loop `while True` e pede o **valor da compra**. Se o valor for negativo, exibe um aviso e pede de novo.
3. Se o valor digitado for `0`, o loop é encerrado com `break`.
4. Pede a **idade do cliente**. Se for negativa, exibe um aviso e pede de novo.
5. Começa com `preco_final` igual ao valor da compra. Se a idade for maior ou igual a 65, aplica 20% de desconto (`* 0.80`).
6. Depois verifica se o valor **já descontado pela idade** é maior que 100. Se for, aplica mais 10% de desconto sobre esse valor (`* 0.90`).
7. Exibe o valor a pagar com duas casas decimais (exemplo: `R$ 144.00`).
8. Guarda a compra na lista com `.append()`, no formato `(valor_bruto, valor_final)`.
9. Volta ao passo 2 para a próxima compra.
10. Ao sair do loop, percorre a lista com um `for`, soma os valores brutos e os valores finais, calcula o total de descontos (`total_bruto - total_final`) e mostra o resumo do dia.

## Como rodar

```bash
python pdv.py
```

Requer Python 3.6 ou superior. Não usa bibliotecas externas. Para encerrar o programa, digite `0` no valor da compra.

## Tabela de exemplos

Casos de teste usados para validar o programa (todos conferidos na execução):

| Caso | Valor da compra | Idade | Valor final esperado | Observação |
|------|-----------------|-------|----------------------|------------|
| 1 | 50.00 | 30 | R$ 50.00 | Nenhum desconto |
| 2 | 100.00 | 30 | R$ 100.00 | Não é maior que 100, sem desconto |
| 3 | 200.00 | 70 | R$ 144.00 | 200 × 0.8 = 160, depois 160 × 0.9 |
| 4 | 80.00 | 65 | R$ 64.00 | Só desconto de idade (idade = 65 conta) |
| 5 | 125.00 | 70 | R$ 100.00 | 125 × 0.8 = 100, não passa de 100 |
| 6 | 150.00 | 30 | R$ 135.00 | Só desconto de valor (10%) |
| 7 | 101.00 | 30 | R$ 90.90 | 101 × 0.9 = 90.90 |
| 8 | 130.00 | 65 | R$ 93.60 | 130 × 0.8 = 104, depois 104 × 0.9 |
| 9 | 60.00 | 64 | R$ 60.00 | Idade 64, sem desconto de idade |
| 10 | 200.00 | 64 | R$ 180.00 | Só desconto de valor (10%) |

### Exemplo de resumo do dia

Para as 10 compras acima:

```
=== RESUMO DO DIA ===
Quantidade de compras: 10
Total bruto:           R$ 1196.00
Total de descontos:    R$ 178.50
Total final:           R$ 1017.50
```

o readme sera atualizado apos adicionar o bonus