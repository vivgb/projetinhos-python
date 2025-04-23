import os
import time 

#classe normie

class ambiente:
    def __init__(self, nome, temperatura, humidade, luz):
        self.nome = nome #vo coloca tipo deserto, ou pantanal, nome do ambiente em si
        self.temperatura = temperatura 
        self.humidade = humidade 
        self.luz = luz #se a luz é intensa de boa ou meio termo
        
    def desc_amb(self):
        return f"\nAmbiente: {self.nome} | Temperatura: {self.temperatura}, Humidade: {self.humidade}, Luz: {self.luz}"
    
    def veri_condi(self, planta):
        if planta.tankar_temp == self.temperatura and planta.tankar_humi == self.humidade and planta.need_luz == self.luz:
            return f"A planta {planta.nome} pode sobreviver nesse ambiente."
        else:
            return f'A planta {planta.nome} NÃO pode sobreviver nesse ambiente.'

#classe superpower pai de todos  
class planta:
    def __init__(self,nome, need_luz, tankar_temp, tankar_humi):
        self.nome = nome
        self.need_luz = need_luz
        self.tankar_temp = tankar_temp
        self.tankar_humi = tankar_humi
        
    def descricao_planta(self):
        return f"\nPlanta: {self.nome} | Luz: {self.need_luz}, Temperatura: {self.tankar_temp}, Humidade: {self.tankar_humi}"

#classe sudita 1
class briofitas(planta):
    def __init__(self, nome):
        super().__init__(nome, need_luz ='Baixa', tankar_temp ='Baixa',tankar_humi ='Alta')
        
    def cuidados(self):
        return (f"Cuidados com {self.nome} (Briófitas):\n"
                "1. Mantenha em locais sombreados.\n"
                "2. Regue frequentemente, mantendo o solo úmido.\n"
                "3. Evite exposição direta ao sol, pois são sensíveis à luz intensa.")

        
#classe sudita 2       
class pteridófitas(planta):
    def __init__ (self,nome):
        super().__init__(nome, need_luz = 'Moderada', tankar_temp = 'Média', tankar_humi = 'Alta')
        
    def cuidados(self):
        return (f"Cuidados com {self.nome} (Pteridófitas):\n"
                "1. Mantenha em ambientes com luz moderada.\n"
                "2. Regue regularmente, mas não deixe a água empoçar.\n"
                "3. Ideal para locais úmidos e quentes, como florestas tropicais.")

#classe sudita 3
class gimnospermas(planta):
    def __init__(self,nome):
        super().__init__ (nome, need_luz = 'Moderada', tankar_temp = 'Baixa', tankar_humi = 'Média')
    
    def cuidados(self):
        return (f"Cuidados com {self.nome} (Gimnospermas):\n"
                "1. Mantenha em ambientes com luz indireta.\n"
                "2. Regue moderadamente, deixando o solo secar entre regas.\n"
                "3. Adaptada a climas frios, mas não resiste a temperaturas extremas.")


#classe sudita 4
class angiospermas(planta):
    def __init__ (self,nome):
        super().__init__(nome, need_luz = 'Intensa', tankar_temp = 'Alta', tankar_humi = 'Média')
        
    def cuidados(self):
        return (f"Cuidados com {self.nome} (Angiospermas):\n"
                "1. Mantenha em locais com bastante luz solar.\n"
                "2. Regue moderadamente, evitando solo encharcado.\n"
                "3. Prefere ambientes quentes e com boa ventilação.")
          
            
def main():
    while True:
            input("Pressione 'enter' para continuar")
            os.system('cls')

            print("""
                        ===================================================================
                                                   Plantas
                        ===================================================================
                                                Menu Principal
                
                                1- Ver ambientes
                                2- Ver plantas e cuidados  
                                3- Cadastrar informações
                                4- Verificar se uma planta pode sobreviver em um ambiente
                                5- Sair
                        ===================================================================
                    """)

            
            escolha = input('->')
        
            if escolha =="1":
                 ver_ambientes(ambientes)
                 
            elif escolha == "2":
                 ver_plantas(plantas)
                 
            elif escolha == "3":
                 cadastrar_informacoes(ambientes,plantas)
                 
            elif escolha == "4":
                 verificar_sobrevivencia(plantas,ambientes)
                 
            elif escolha =="5":
                os.system('cls')
                
                for i in range(4):
                    
                    
                
                    print("""                                                                                                                                                                                                                                                                                                              
                                                                            %@@@@@                                                      
                                                                #@@@@@% %@@@#....@@#                                                    
                                                               @@%==+@@@@#........@@@                                                   
                                                              @@-------#@@........:@@@                                                  
                                                           #@@@@------=-=@@@@#-@@@@**@@@                                                
                                                        @@@@@%@=---+@@*@@@=--#@@=------@@                                               
                                          @@@@@@@@ %@@@@@....%@----%@-%@+------@@@@----%@                                               
                                        @@@=::-+@@@@@:.......#@-----*@@@=------@@-@*---@@                                               
                                       @@.....................@@-------@@=----@@@@@---%@@                                               
                                       @@......................@@@#@@@@#*@@@@@@+-----@@#@@%                                             
                                       @@.....................................%@@@@@@@...@@                                             
                                        @%................................................@@@@@@@@                                      
                                        @@=............................................*@@@@@                                           
                                         @@@@..............................................@@                                           
                                          @@:..................................@@@.........@@@@@@@                                      
                                          @@..................................@@@@@......@@@@@@#                                        
                                          @@...................................@@@@........@@                                           
                                          @@...............................................@@                                           
                                          @@.....................................-..-...+@@@@@@@@@                                      
                                          @@-.........=@..........:@=::@.........:.......@@@                                            
                                        +@@@@@%*....:@@@@@@........@@@@:...............=@@@                                             
                                     *@@@@@@@@.......=@..............................-@@#                                               
                                            @@@.*@:.......-........................@@@@   @@@                                           
                                            @@@@#.........:.....................@@@@@@@@@@@=@@@                                         
                                          @@@@ %@@#.@@.....................=@@@@#+@@::::+@...=@@@                                       
                                                 @@@@@..............-%@@@@@@@-----+@*:::@@......@@                                      
                                               .@@@ *@@@@@@@@@@@@@@%=-:::::@@------%@-::@@......@@                                      
                                              %@@        %@@@@----@@-:::::@@--------@@::@@....-@@                                       
                                                       @@@-:@@-==--*@@@@@@@--=@.@#--=@@@@@@@@@@%                                        
                                                     @@@@@::@@@#.@=---==------@@@=---@@%@@                                              
                                                    @@...+@@@@=@@#-------------------#@@                                                
                                                    @@=.....@@-----------------------=@@                                                
                                                     @@.....@@------------------------@@                                                
                                                     @@*....@@------------------------@@                                                
                                                      @@@@@@@@----------=+------------@@                                                
                                                            @@----------=@@----------*@@                                                
                                                            @@%+=-----=+#@@%#**+*@@@@@@@                                                
                                                           @@.:%@@@@@@@@@@=..::-:.....@@                                                
                                                          =@-...........@%............@@                                                
                                                           @@%.........+@@#.........%@@                                                 
                                                             @@@@@@@@@@@%*@@@@@@@@@@@                                                    """)
                    time.sleep(0.75)
                    os.system('cls')
                    print("""⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                     
                                                                            @@@@@@                                                      
                                                                %@@@@@# %@@@#....@@#                                                    
                                                               @@%==+%@@@#........@@@                                                   
                                                              @@-------#@@........:@@@                                                  
                                                           %@@@@------=-=@@@@#-@@@@**@@@-                                               
                                                        @@@@@%@=---+@@+@@@=--#@@=------@@                                               
                                          @@@@@@@@ %@@@@@....%@----%@-%@+------@@@@----%@                                               
                                        @@@=::-+@@@@@:.......#@-----*@@@=------@@-@*---@@                                               
                                       @@.....................@@-------@@=----@@@@@---%@@                                               
                                       @@......................@@@%@@@@#*@@@@@@+-----@@#@@@                                             
                                       @@.....................................%@@@@@@@...@@                                             
                                        @%................................................@@@@@@@@                                      
                                        @@=............................................*@@@@@                                           
                                         @@@@..............................................@@                                           
                                          @@:..................................@@@.........@@@@@@@                                      
                                          @@..................................@@@@@......@@@@@@*                                        
                                          @@...................................@@@@........@@                                           
                                          @@...............................................@@                                           
                                          @@.....................................-..-...+@@@@@@@@@                                      
                                          @@-.........=@..........:@-::@.........:....@@%@@@@                                           
                                        -@@@@@%*....:@@@@@@........@@@@:............%@=.*+..@@@                                         
                                     =@@@%@@@@.......=@.............................=@*......*@.                                        
                                            @@@.*@:.......-........................@@@@@.....-@@                                        
                                            @@@@#.........:.....................@@@*:::@@...:@@                                         
                                          @@@@ @@@#.@@.....................=@@@@#+@@::::+@@@@@                                          
                                                 @@@@@:.............-@@@@@@@@-----+@*::::=@@%                                           
                                               :@@@ +@@@@@@@@@@@@@@%=-:::::@@------%@--@@@@                                             
                                              %@@        %@@@@----@@-:::::@@--------@@@@                                                
                                                       @@@-:@@-==--+@@@@@@@--=@.@#--=@@                                                 
                                                     @@@@@::@@@#.@=---==------@@@----@@                                                 
                                                    @@...+@@@@=@@#-------------------#@@                                                
                                                    @@=.....@@-----------------------=@@                                                
                                                     @@.....@@------------------------@@                                                
                                                     @@*....@@------------------------@@                                                
                                                      @@@@@@@@----------=+------------@@                                                
                                                            @@----------=@@----------*@@                                                
                                                            @@%+=-----=+#@@%#****@@@@@@@                                                
                                                           @@.:%@@@@@@@%@@-..:::......@@                                                
                                                          =@-...........@%............@@                                                
                                                           @@%.........+@@#.........@@@                                                 
                                                             @@@@@@@@@@@##@@@@@@@@@@@                                                     """)
                    time.sleep(0.75)
                    os.system('cls')
                    break
            else:
                print("Escolha inválida, tente novamente.")
 

    
ambientes = [
    ambiente('Floresta Tropical', 'Alta', 'Alta', 'Moderada'),
    ambiente('Deserto', 'Alta', 'Baixa', 'Intensa'),
    ambiente('Tundra', 'Baixa', 'Baixa', 'Baixa')
]

plantas = [
    briofitas('Musgo'),
    pteridófitas('Samambaia'),
    gimnospermas('Pinheiro'),
    angiospermas('Rosa')
]


def ver_ambientes(ambientes):
    if len(ambientes) == 0:
        print("\nNenhum ambiente registrado.")
    else:
        print("\nAmbientes registrados:")
        for ambiente in ambientes:
            print(ambiente.desc_amb())


def ver_plantas(plantas):
    if len(plantas) == 0:
        print("\nNenhuma planta registrada.")
    else:
        print("\nPlantas registradas e seus cuidados:")
        for planta in plantas:
            print(planta.descricao_planta())
            print(planta.cuidados())


def ver_ambientes(ambientes):
    if len(ambientes) == 0:
        print("\nNenhum ambiente registrado.")
    else:
        print("\nAmbientes registrados:")
        for ambiente in ambientes:
            print(ambiente.desc_amb())


def ver_plantas(plantas):
    if len(plantas) == 0:
        print("\nNenhuma planta registrada.")
    else:
        print("\nPlantas registradas e seus cuidados:")
        for planta in plantas:
            print(planta.descricao_planta())
            print(planta.cuidados())
            
def verificar_sobrevivencia(plantas, ambientes):
    planta_nome = input("\nDigite o nome da planta: ").title()
    ambiente_nome = input("\nDigite o nome do ambiente: ").title()
    
    planta = next((pl for pl in plantas if pl.nome == planta_nome), None)
    ambiente = next((am for am in ambientes if am.nome == ambiente_nome), None)

    if planta and ambiente:
        print(ambiente.veri_condi(planta))
    else:
        print("Planta ou ambiente não encontrados.")

              
def cadastrar_ambiente(ambientes):
    nome = input("\nDigite o nome do ambiente: ").title()
    temperatura = input("Digite a temperatura (Alta, Média, Baixa): ").title()
    humidade = input("Digite a humidade (Alta, Média, Baixa): ").title()
    luz = input("Digite a quantidade de luz (Intensa, Moderada, Baixa): ").title()
    ambiente = ambiente(nome, temperatura, humidade, luz)
    ambientes.append(ambiente)
    print(f"\nO ambiente {nome} foi cadastrado com sucesso!")
 
           
def cadastrar_planta(plantas):
    nome = input("\nDigite o nome da planta: ").title()

    print("\nEscolha o tipo de planta:")
    print("1. Briófita")
    print("2. Pteridófita")
    print("3. Gimnosperma")
    print("4. Angiosperma")
    tipo = input("Escolha uma opção: ")

    if tipo == "1":
        planta = briofitas(nome)
    elif tipo == "2":
        planta = pteridófitas(nome)
    elif tipo == "3":
        planta = gimnospermas(nome)
    elif tipo == "4":
        planta = angiospermas(nome)
    else:
        print("Opção inválida. Planta não cadastrada.")
        return
    
    plantas.append(planta)
    print(f"\n{nome} foi cadastrada com sucesso!")
    
               
def cadastrar_informacoes(ambientes, plantas):
    os.system('cls')
    print("""
                 __________________________________
                |                                  |
                |      Cadastrar Informações       |
                |                                  |
                |   1- Cadastrar novo ambiente     |
                |   2- Cadastrar nova planta       |
                |__________________________________| 
          """)
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_ambiente(ambientes)
    elif escolha == "2":
        cadastrar_planta(plantas)
    else:
        print("Opção inválida.")
if __name__ == "__main__":
    main()
