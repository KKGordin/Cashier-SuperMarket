
# Supermarket Cashier

import os
import time

print("======= SuperMarket =======")
start = input("Pressione [Enter] para começar!")

Banco_De_Dados = [
    {"id":2627, "nome": "Arroz 5kg", "preco": 36.90},
    {"id":2923, "nome": "Feijão 1kg", "preco": 6.90},
    {"id":3001, "nome": "Macarrão", "preco": 3.40},
    {"id":3395, "nome": "Ovos 30un", "preco": 15.90},
    {"id":3680, "nome": "Leite", "preco": 6.50},
    {"id":5178, "nome": "Salgadinho", "preco": 8.20},
    {"id":5397, "nome": "Papel Higiênico", "preco": 19.90},
    {"id":7038, "nome": "Café 500g", "preco": 24.10},
    {"id":7552, "nome": "Papel Toalha", "preco": 7.40},
    {"id":9312, "nome": "Sabonete", "preco": 2.00}
]

cartao_debito = [
    {"id":63137858, "banco": "NuBank - Débito", "senha":5236},
]

cartao_credito = [
    {"id":82482567, "banco": "NuBank - Crédito", "senha":6137}
]


compras = []
soma_produtos = []
last_item = []

def pagamento_card(card):
    cont = 1
    while cont == 1:
    
        card_pag = int(input("Insira seu cartão | ID: "))
        
        for c in card:
            if c["id"] == card_pag:
                print("Selecionado: ", c["banco"])
                password = int(input("Digite sua senha: "))
                if password == c["senha"]:
                    print("Processando pagamento...")
                    time.sleep(5)
                    print("Compra finalizada com sucesso!") 
                    cont += 1
                else:
                    print("[ERROR] Senha incorreta!")
             
            else:
                print("[ERROR] Não autorizado!")
    
            
        
    
if start == "":
    print("""
    Opções:
    [1] Adicionar produtos às compras
    [2] Extrato do dia
    [3] Desligar caixa""")
    escolha = int(input(">>> "))
        
if escolha == 1:
    while True:
            
        # Mostrando a lista
        os.system("cls")
        
        if len(compras) > 0:
            for c in compras:
                print("Nome:",c["nome"], "| Preço: R$",c["preco"])
                
        # Finalizando:     
        ad_produto = int(input("[0]Finish [1]Remove | ID do produto: "))
        if ad_produto == 0:        
            break
        # Removendo itens da lista:   
        elif ad_produto == 1:
            remove = int(input("[0]Remove Last | Item number: "))
            if remove == 0:
                ad_produto = compras.pop()
                ad_produto = last_item.pop()
            
            else:
                ad_produto = compras.pop(remove - 1)
                ad_produto = last_item.pop(remove - 1)
        
        # Adicionando itens na lista:
        else:
            for produtos in Banco_De_Dados:
                if produtos["id"] == ad_produto:
                    compras.append({
                        "nome": produtos["nome"],
                        "preco": produtos["preco"]
                    })
            
            
            last_item.append(compras[-1])
    
    for select_prod in last_item:
        soma_produtos.append(select_prod["preco"])
                
    os.system("cls")
    
    # Forma de pagamento
    
    print("===== Forma de pagamento =====")
    soma = sum(soma_produtos)
    print("A compra ficou por: R${:.2f}".format(soma))
    print("""
    [1] Dinheiro
    [2] Pix
    [3] Cartão Débito
    [4] Cartão Crédito""")
    opc = int(input("Digite sua opção: "))
    
    if opc == 1:
        print("Processando pagamento...")
        time.sleep(5)
        print("Compra finalizada com sucesso!")
    
    elif opc == 2:
        print("Gerando QR Code...")
        time.sleep(2)
        print("Processando pagamento...")
        time.sleep(5)
        print("Compra finalizada com sucesso!")
        
    elif opc == 3:
        pagamento_card(cartao_debito)
        
        
    elif opc == 4:
        print("Você pode parcelar em até 6x sem juros!")
        parcela = int(input("Em quantas vezes você deseja parcelar: "))
        soma = sum(soma_produtos)
        res = soma / parcela
        print("Cada parcela ficou por {:.2f}".format(res))
        pagamento_card(cartao_credito)
        
else:
    print("[ERROR] Você deve pressionar [Enter] para começar!")
        

        







