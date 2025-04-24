import os


tabela = {
    (47, 47): 0.15, (47, 48): 0.25, (47, 49): 0.32,
    (48, 47): 0.28, (48, 48): 0.12, (48, 49): 0.28,
    (49, 47): 0.40, (49, 48): 0.25, (49, 49): 0.09
}

historico = []

def calcular_custo(ddd_origem, ddd_destino, minutos):
    chave = (ddd_origem, ddd_destino)
    if chave in tabela:
        custo = tabela[chave] * minutos
    else:
        custo = 0  # Caso não haja tarifa definida, o custo é zero.
    return custo

def registrar_consulta(ddd_origem, ddd_destino, minutos, custo):
    consulta = {
        "DDD origem:": ddd_origem,
        "DDD destino:": ddd_destino,
        "minutos:": minutos,
        "custo:": custo
    }
    if len(historico) >= 5:
        historico.pop(0)
    historico.append(consulta)

def exibir_historico():
    if len (historico) == 0:
        print("Histórico vazio.")
        
    for consulta in historico:
        print(consulta)

def main():
    print("""              ,---------------------------,            
              |  /---------------------\  |            
              | |                       | |            
              | |     Bem-Vindo(a)      | |            
              | |      ao Plano         | |            
              | |       Telefonico      | |            
              | |                       | |            
              |  \_____________________/  |            
              |___________________________|            
            ,---\_____     []     _______/------,      
          /         /______________\           /|      
        /___________________________________ /  | ___  
        |                                   |   |    ) 
        |  _ _ _                 [-------]  |   |   (  
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/ 
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /            
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                """)



    while True:
            
        input("Digite 'enter' para aparecer a próxima etapa.")
        os.system('cls')
        print("""
            +-----------------------------------------+
            |   1- Calcular o custo da ligação        |
            |   2- Consultar o histórico              |
            |   3- Sair                               |
            +-----------------------------------------+
        """)
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            ddd_origem = int(input("Digite o DDD de origem: "))
            ddd_destino = int(input("Digite o DDD de destino: "))
            minutos = float(input("Digite o tempo de ligação em minutos: "))

            custo = calcular_custo(ddd_origem, ddd_destino, minutos)
            registrar_consulta(ddd_origem, ddd_destino, minutos, custo)

            print(f"O custo da ligação é: R${custo:.2f}")
        
        elif escolha == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir_historico()
        
        elif escolha == '3':
            print("Programa encerrado.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()