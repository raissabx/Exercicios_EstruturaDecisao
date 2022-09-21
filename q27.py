produto = input('O que você deseja comprar? Morango ou Maçã: ').capitalize()
total = 0

if produto == 'Morango':
    kg_morango = float(input('Digite a quantidade de morangos em kg: '))
    if kg_morango <= 5:
        preco_morango = float(2.50)
        total = float(kg_morango * preco_morango)
        print(f"O valor a ser pago de morangos é de R$ {round(total, 2)}")

    elif kg_morango > 5 and kg_morango <= 8:
        preco_morango = float(2.20)
        total = float(kg_morango * preco_morango)
        print(f"O valor a ser pago de morangos é de R$ {round(total, 2)}")
    
    elif kg_morango > 8 or total > 25:
        preco_morango = float(2.20)
        total = float(kg_morango * preco_morango)
        desconto = (total * 0.1)
        preco_desconto = total - desconto
        print(f"O valor a ser pago com desconto é de R$ {round(preco_desconto, 2)}")


if produto == 'Maçã':
    kg_maca = float(input('Digite a quantidade de morangos em kg: '))
    if kg_maca <= 5:
        preco_maca = float(1.80)
        total = kg_maca * preco_maca
        print(f"O valor a ser pago de maçãs é de R$ {round(total, 2)}")

    elif kg_maca > 5 and kg_maca <= 8:
        preco_maca = 1.50
        total = float(kg_maca * preco_maca)
        print(f"O valor a ser pago de maçãs é de R$ {round(total, 2)}")

    elif kg_maca > 8 or total > 25:
        preco_maca = 1.50
        total = float(kg_maca * preco_maca)
        desconto = (total * 0.1)
        preco_desconto = total - desconto
        print(f"O valor a ser pago com desconto é de R$ {round(preco_desconto, 2)}")






        
