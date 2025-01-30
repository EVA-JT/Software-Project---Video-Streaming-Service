import os

profile_list = []
user_data = {}
logged_user = "sample"
choosen_profile = "sample"

movie_catalog = {
    "ação": ["filme de ação1", "filme de ação2", "filme de ação3"],
    "comédia": ["filme de comedia1", "filme de comedia2", "filme de comedia3"],
    "romance": ["filme de romance1", "filme de romance2", "filme de romance3"]
}

show_catalog = {
    "ação": ["show de ação1", "show de ação2", "show de ação3"],
    "comédia": ["show de comedia1", "show de comedia2", "show de comedia3"],
    "romance": ["show de romance1", "show de romance2", "show de romance3"]
}

def create_a_user():
    while(1): # Loop até um email novo ser digitado      
        email = input("Digite seu e-mail: ")
        if email in user_data:
            print("Este e-mail já foi cadastrado, tente novamente.")
        else:
            break
    
    while(1): # Loop até as senhas baterem
        password = input("Digite sua senha: ")
        rpt_password = input("Digite sua senha novamente: ")
        if password != rpt_password:
            print("As duas senhas não são iguais, tente novamente")
        else:
            break
            

    print("Após seu teste de graça de 7 dias, qual tipo de plano de pagamento você gostaria?\n1 - Mensal\n2 - Trimestral\n3 - Anual")
    payment_plan = int(input())

    user_data[email] = {
        'password': password,
        'payment_plan': payment_plan
    }

def user_login():
    email = input("Digite seu e-mail: ")
    password = input("Digite sua senha: ")
    
    if email in user_data and user_data[email]['password'] == password:
        global logged_user
        logged_user = email

        input("Login efetuado, pressione qualquer tecla para continuar.")
        return 1
    else:
        input("Email ou senha errados, tente novamente ou crie uma conta.")
        return 0

#Imprime todos os perfis criados no momento
def print_profiles():
    for i in range(len(profile_list)):
        print(i, " - ", profile_list[i]["first"], profile_list[i]['last'])

# Constroi um dicionario com as informações do perfil desejado do usuario
def user_profile(first_name, last_name, user_age):
    profile = {'first': first_name, 'last': last_name, 'age':user_age}
    return profile

#Pede as informações nescessárias do usuario para criar um perfil
def create_profile():
    os.system('cls')
    print("Crie um perfil!")
    first_name = input("Primeiro nome: ")
    last_name = input("Sobrenome: ")
    age = input("Idade: ")

    profile = user_profile(first_name, last_name, age)
    profile_list.append(profile)
    return profile

#Exclui o perfil que o usuario pedir   
def delete_profile():
    print_profiles()
    opt = int(input("Qual perfil você gostaria deletar?\n"))
    assurance = str(input("Você tem certeza? Y/N\n"))

    if assurance == "Y" or assurance == "y":
        profile_list.pop(opt)

#Escolhe o perfil
def choose_profile():
    print("Qual perfil você gostaria de usar?")
    print_profiles()
    user_choice = int(input())

    global choosen_profile 
    choosen_profile = profile_list[user_choice]

# Menu de login, 
def login_menu():
    while(1):
        os.system('cls')

        print("Boas Vindas ao [nome do site], gostaria de:\n1 - Fazer login\n2 - criar uma conta\n3 - Sair")

        opt = int(input())
        if opt == 1:
            if user_login():
                initial_menu()
        elif opt == 2:
            create_a_user()
        elif opt == 3:
            break

def account_management():
    while(1):
        global logged_user
        os.system('cls')
        print("Olá usuário", logged_user, ". O que gostaria de alterar na sua conta?")
        print("1 - Alterar e-mail\n2 - Alterar Senha\n3 - Alterar plano de pagamento\n4 - Excluir Conta\n5 - Sair deste menu")

        opt = int(input())
        if opt == 1:
            while(1): # Loop até um email novo ser digitado      
                email = input("Digite seu e-mail novo ou digite 'Sair' para cancelar: ")
                if email in user_data:
                    print("Este e-mail já foi cadastrado, tente novamente.")
                elif email == "sair" or email == "Sair":
                    break
                else:
                    user_data[email] = user_data.pop(logged_user)
                    logged_user = email
                    input("E-mail novo cadastrado com sucesso. Pressione enter para sair.")
                    break
        elif opt == 2:
            while(1): # Loop até as senhas baterem
                password = input("Digite sua senha nova ou digite 'sair' para cancelar: ")
                if password == "sair" or password == "Sair":
                    break
                rpt_password = input("Digite a senha novamente: ")
                if password != rpt_password:
                    print("As duas senhas não são iguais, tente novamente")
                else:
                    user_data[logged_user]['password'] = password
                    input("Senha alterada com sucesso. Pressione enter para sair")
                    break
        elif opt == 3:
            print("Ainda faltam 7 dias para a proxima cobrança.")
            print("Qual tipo de plano de pagamento você gostaria?\n1 - Mensal\n2 - Trimestral\n3 - Anual\n4 - Cancelar")
            opt = int(input())
            if opt == 4:
                break
            else:
                user_data[logged_user]['payment_plan'] = opt
                input("Plano de pagamento alterado com sucesso. Pressione enter tecla para sair.")
        elif opt == 4:
            con = input("Tem certeza que quer excluir sua conta? Y/N\n")
            if con == "y" or con == "Y":
                user_data.pop(logged_user)
                return 0
        elif opt == 5:
            return 1
    
# Menu para seleção de perfis
def initial_menu():
    while(1):
        if len(profile_list) == 0: #Inicio do programa, nenhum perfil criado
            create_profile()

        else:
            os.system('cls') #Limpa a tela
            print("Olá, Gostaria de acessar algum perfil ou criar um novo?")
            option = int(input("1 - Acessar perfil\n2 - Criar um novo\n3 - Excluir um perfil\n4 - Configurar conta\n5 - Sair\n"))

            if option == 1:
                choose_profile()
                main_menu()
            elif option == 2:
                create_profile()
            elif option == 3:
                delete_profile()
            elif option == 4:
                res = account_management()
                if res == 0:
                    return               
            elif option == 5:
                print("Deseja sair? Y/N")
                assurance = str(input())
                if assurance == "Y":
                    break

# Menu inicial onde será mostrado o catálogo de filmes e séries
def main_menu():
    os.system('cls')
    print("Olá", choosen_profile["first"], ", o que você gostaria de assistir?")
    print(movie_catalog)
    print(show_catalog)
    input()
    
login_menu()
