import os

profile_list = []

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

#Imprime todos os perfis criados no momento
def print_profiles():
    for i in range(len(profile_list)):
        print(i, " - ", profile_list[i]["first"], profile_list[i]['last'])

# Constroi um dicionario com as informações do perfil desejado do usuario
def user_profile(first_name, last_name, user_age):
    user = {'first': first_name, 'last': last_name, 'age':user_age}
    return user

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

    global choosen_profile #Criando uma variavel global
    choosen_profile = profile_list[user_choice]

# Menu inicial de navegação
def initial_menu():
    while(1):
        if len(profile_list) == 0: #Inicio do programa, nenhum perfil criado
            create_profile()

        else:
            os.system('cls') #Limpa a tela
            print("Olá, Gostaria de acessar algum perfil ou criar um novo?")
            option = int(input("Acessar perfil - 1\nCriar um novo - 2\nExcluir um perfil - 3\nSair - 4\n"))

            if option == 1:
                choose_profile()
                main_menu()
            elif option == 2:
                create_profile()
            elif option == 3:
                delete_profile()
            elif option == 4:
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
    
initial_menu()
