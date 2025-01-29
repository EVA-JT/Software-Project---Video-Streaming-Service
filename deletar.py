user_quant = 0
profile_list = []

movie_catalog = [["filme_de_ação1", "filme_de_ação2", "filme_de_ação3"], ["filme_de_comedia1", "filme_de_comedia2", "filme_de_comedia3"], ["filme_de_romance1", "filme_de_romance2", "filme_de_romance3"]]
show_catalog =  [["serie_de_ação1", "serie_de_ação2", "serie_de_ação3"], ["serie_de_comedia1", "serie_de_comedia2", "serie_de_comedia3"], ["serie_de_romance1", "serie_de_romance2", "serie_de_romance3"]]

def user_profile(first_name, last_name, user_age):
    # Constroi um dicionario com as informações do perfil desejado do usuario
    user = {'first': first_name, 'last': last_name, 'age':user_age}

    return user

def create_profile():
    #Pede as informações nescessárias para o usuario para criar um perfil
    print("Crie um perfil!")
    first_name = input("Primeiro nome: ")
    last_name = input("Sobrenome: ")
    age = input("Idade: ")

    profile = user_profile(first_name, last_name, age)
    return profile
    
def catalog():
    #Imprime o catalogo baseado na escolha do usuario
    print("O que você pretende assistir, uma série ou um filme? (sem acentos e caracteres especiais))
    
    user_choice = input()
    opt = 0
    
    if user_choice == "serie":
        opt = 0
    elif user_choice == "filme":
        opt = 1
    
    print("Qual genero você que ver, ação ou comédia? (sem acentos e caracteres especiais)")
    user_choice = input()
    
    if user_choice == "acao":
        print(show_catalog[opt])
    elif user_choice == "comedia":
        print(movie_catalog[opt])
    
    
    

while(1):
    if(user_quant == 0):
        profile = create_profile()
        profile_list.append(profile)
        user_quant += 1
        
    else:
        print("\nOlá, Gostaria de acessar algum perfil ou criar um novo?")
        option = int(input("Acessar perfil - 1\nCriar um novo - 2\n"))
        if option == 1:
            for i in range(user_quant):
                print(i, " - ", profile_list[i]["first"])
                
            user_choice = int(input("Qual perfil você gostaria de usar?"))
            choosen_profile = profile_list[user_choice]
            print("Olá ", choosen_profile["first"], choosen_profile["last"], "o que gostaria de assistir?")
            catalog()
            break
        else:
            profile = create_profile()
            profile_list.append(profile)
            user_quant += 1


        


