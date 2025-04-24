import os
def cal(custo, margem):
    return custo + (custo * (margem/100))

prods = []
carrinho = []

def add():
    nome = input("Insira o nome do produto:")
    custo = float(input(f"Insira o custo do produto '{nome}' em R$:"))
    margem = float(input(f"Insira a margem de lucro (%) para o produto {nome}:"))
    venda = cal (custo, margem)

    prod = {
        'nome': nome,
        'custo': custo,
        'margem':margem,
        'venda': venda
        }
    
    prods.append(prod)   
    print(f"Produto '{nome}' adicionado ao carrinho com sucesso!\n")

def addcarrinho():
    nome = input("Insira o nome do produto que deseja adicionar ao carrinho:")

    for prod in prods:
        if prod['nome'] == nome:
            carrinho.append(prod)
            print(f"Produto '{nome}' adicionado ao carrinho de compras.\n")
            return
    print(f"Produto '{nome}' não encontrado.")

def totaluc():
    total = 0
    luctot = 0

    for prod in carrinho:
        total +=prod['venda']
        luctot += prod['venda'] - prod['custo']
    return total,luctot

def main():
    while True:
        input("Pressione 'enter' para continuar.")
        os.system('cls')
        print("""
                
                 _________________________________________________
                |                                                 |
                |                  MENU PRINCIPAL                 |
                |                                                 |
                |   1- Adicionar produto                          |
                |   2- Adicionar produto ao carrinho de compras   |
                |   3- Calcular total do carrinho e lucro         |
                |   4- Sair                                       |   
                |_________________________________________________|  
          
                     """)

        
        
        op = input("Escolha uma opção:")
    

        if op =='1':
            add()

        elif op == '2':
            addcarrinho()

        elif op == '3':
            total,luctot = totaluc ()
            print(f"Total do carrinho: R${total:.2f}")
            print(f"Lucro total: R${luctot:.2f}\n")
            
        elif op == '4':
            print("Programa encerrado.")
            break
        
        else:
            print("Opção Inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
        