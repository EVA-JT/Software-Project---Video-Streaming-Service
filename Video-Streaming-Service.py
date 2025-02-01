import os

from data import movie_catalog
from data import show_catalog
from data import quality_list
from data import genres_list

profile_list = []
user_data = {}
logged_user = "sample"
choosen_profile = "sample"

# --- UTILIDADES ---

#Imprime todos os perfis criados no momento
def print_profiles():
    for i in range(len(profile_list)):
        print(i, " - ", profile_list[i]["first"], profile_list[i]['last'])

def calculate_review_score(movie_dict):
    reviews = movie_dict['reviews']
    scores_sum = 0
    scores = 0

    for reviwer in reviews:
        scores_sum += reviews[reviwer]['score']
        scores += 1
    
    if scores == 0:
        return -1
    else:
        return scores_sum / scores
    
def print_reviews(movie_dict):
    reviews = movie_dict['reviews']
    reviews_sum = 0

    for reviwer in reviews:
        if reviews[reviwer]['review'] != "":
            print(f"{reviwer} : {reviews[reviwer]['review']}")
            reviews_sum += 1

    if reviews_sum == 0:
        print("There are no reviews for this title at the moment")

#------

def review_page(movie_dict, title):
    global choosen_profile 
    reviews = movie_dict['reviews']

    score = int(input(f"What would you rate {title} out of 10?\n"))
    review = input("Write your review: ")

    reviewer_name = choosen_profile['first']
    reviews[reviewer_name] = {
        "score": score,
        "review": review
    }
    
    input("Your review has been saved. Press enter to continue.")


#Cria uma conta do usuario, usando email, uma senha e o plano de pagamento e salva essas informações no dicionario de dados do usuario
def create_a_user():
    while(1): # Loop até um email novo ser digitado      
        email = input("Enter your email: ")
        if email in user_data: #Se o email já estiver na database
            print("This email has already been registered, please try again.")
        else:
            break
    
    while(1): # Loop até as senhas baterem
        password = input("Enter your password: ")
        rpt_password = input("Enter your password again: ")
        if password != rpt_password:
            print("The two passwords are not the same, try again.")
        else:
            break
            

    print("After your 7-day free trial, what type of payment plan would you like?\n1 - Monthly\n2 - quarterly\n3 - Annual")
    payment_plan = int(input())

    user_data[email] = { #A "chave" da variavel 'email' corresponde a essas informações
        'password': password,
        'payment_plan': payment_plan
    }

#O login do usuario, ao digitar o email e senha ele checa se ambos estão em user_data e se estiverem retorna 1 para login_menu() para prosseguir
def user_login():
    email = input("Enter your email: ")
    password = input("Enter your password again: ")
    
    if email in user_data and user_data[email]['password'] == password: # checa se o email está presente em user_data, se sim, checa se a senha digitada bate com a do dicionario
        global logged_user # variavel global (tem que ser declarada assim sempre que for usar)
        logged_user = email

        input("Login succesful, press enter to continue.")
        return 1 #sucesso
    else:
        input("Wrong email or password, try again or create an account.")
        return 0 #falha

#Pede as informações nescessárias do usuario para criar um perfil
def create_profile():
    os.system('cls')
    print("Create a profile!")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = input("Your age: ")

    while(1):
        category_preference = input("Do you prefer: movies, shows or both? ")
        category_preference = category_preference.lower()

        if category_preference == "movies" or category_preference == "shows":
            category_preference = category_preference[:-1] # remove a ultima letra 's'
            break

        elif category_preference == "both":
            category_preference = "all"
            break

        else:
            input("Category not available. Press enter to try again")

    g_l = genres_list.copy() #copia a lista de generos para g_l
    fav_genres = []
    while (len(g_l) >= 1):
        print("Enter your favorite genres or 'cancel' to exit.")
        for genre in g_l:
            print(f"{genre.title()} | ", end='') #printa os generos disponiveis

        opt = input("\n")
        opt = opt.lower()

        if opt == "cancel":
            break

        elif opt in genres_list and opt not in fav_genres: #se o genero digitado estiver em genres_list e não estiver em fav_genres, ele é adicionado
            fav_genres.append(opt)
            g_l.remove(opt)

        else:
            input("This genre is not availabe. Press enter to try again.")

    if not fav_genres: #se a lista estiver vazia então os generos favoritos serão todos (genres_list)
        fav_genres = genres_list.copy()

    profile = {
        'first': first_name,
        'last': last_name, 
        'age': age,
        'c_preference': category_preference,
        'g_preference': fav_genres,
        'bandwidth': "",
        'bookmarks': [],
        'w_history': []
    }

    profile_list.append(profile)
    return profile

#Exclui o perfil que o usuario pedir   
def delete_profile():
    print_profiles()
    opt = int(input("Which profile would you like to delete?\n"))
    assurance = str(input("Are you sure? Y/N\n"))

    if assurance == "Y" or assurance == "y":
        profile_list.pop(opt)

#Escolhe o perfil
def choose_profile():
    global choosen_profile 
    print("Which profile would you like to use?")
    print_profiles()
    user_choice = int(input())

    
    choosen_profile = profile_list[user_choice]

#Página de configuração da conta do usuário
def account_management():
    while(1):
        global logged_user #declarando a variavel global para usa-la
        os.system('cls')
        print("Hello user", logged_user, ". What would you like to change in your account?")
        print("1 - Change e-mail\n2 - Change password\n3 - Change payment plan\n4 - Delete account\n5 - Exit menu")

        opt = int(input())
        if opt == 1:
            while(1): # Loop até um email novo ser digitado      
                email = input("Enter your new e-mail or type 'out' to cancel: ")
                if email in user_data:
                    print("This email has already been registered, please try again.")
                elif email == "out" or email == "Out":
                    break
                else:
                    user_data[email] = user_data.pop(logged_user)
                    logged_user = email
                    input("New email successfully registered. Press enter to exit.")
                    break
        elif opt == 2:
            while(1): # Loop até as senhas baterem
                password = input("Enter your new password or type 'out' to cancel: ")
                if password == "out" or password == "Out":
                    break
                rpt_password = input("Enter your password again: ")
                if password != rpt_password:
                    print("The two passwords are not the same, try again.")
                else:
                    user_data[logged_user]['password'] = password
                    input("Password changed successfully. Press enter to exit")
                    break
        elif opt == 3:
            print("There are still 7 days until the next billing.")
            print("What type of payment plan would you like?\n1 - Monthly\n2 - Quarterly\n3 - Annual\n4 - Cancel")
            opt = int(input())
            if opt == 4:
                break
            else:
                user_data[logged_user]['payment_plan'] = opt
                input("Payment plan changed successfully. Press enter key to exit.")
        elif opt == 4:
            con = input("Are you sure you want to delete your account? Y/N\n")
            if con == "y" or con == "Y":
                user_data.pop(logged_user)
                return 0
        elif opt == 5:
            return 1

#Mostra as informações de um filme/show escolhido usando o genero, categoria e titulo
#GENRE: uma string correspondete a algum item de genre_list[]
#CATEGORY: uma string "movie" ou "show"
#TITLE: uma string que corresponde a algum filme/show da database
def show_details(genre, category, title):
    global choosen_profile 
    os.system('cls')

    #escolhe qual catalogo usar
    if category == "movie":
        choosen_one = movie_catalog[genre][title]
    else:
        choosen_one = show_catalog[genre][title]

    print(f"Title: {title}\nSinopsis: {choosen_one['sinopsis']}\nYear: {choosen_one['year']}\nRating: {choosen_one['rating']}\n")

    opt = int(input("1 - Watch\n2 - Bookmark it\n3 - Bandwidth settings\n4 - Show reviews\n5 - Exit\n"))

    #salva o item assistido no histórico
    if opt == 1:
        if choosen_profile['bandwidth'] == "":
            while(1):
                b_w = input("In what quality do you want to watch, 'Low', 'Medium' or 'High'? (We recommend 'High' for your bandwidth)\n")
                b_w = b_w.lower()

                if b_w in quality_list:
                    choosen_profile['bandwidth'] = b_w
                    break
                else:
                    input("Error. Press enter to try again")


        history = {
            'genre': genre,
            'category': category,
            'title': title
        }
        choosen_profile['w_history'].append(history)
        input(f"You've just watched {title} in {choosen_profile['bandwidth']} quality. Press enter to continue")
    #salva o item nos bookmarks
    elif opt == 2:
        bookmark = {
            'genre': genre,
            'category': category,
            'title': title
        }
        choosen_profile['bookmarks'].append(bookmark)
        input(f"{title} has just been added to your bookmarks. Press enter to continue.")
    elif opt == 3:
        if choosen_profile['bandwidth'] == "":
            print("You haven't chosen your preferred quality.")
        else:
            print(f"Your current choosen quality is: {choosen_profile['bandwidth']}")

            while(1):
                b_w = input("In what quality do you want to watch, 'Low', 'Medium' or 'High'? (We recommend 'High' for your bandwidth)\nType 'exit' to cancel.\n")
                b_w = b_w.lower()

                if b_w == "exit":
                    show_details(genre, category, title)
                    break
                elif b_w in quality_list:
                    choosen_profile['bandwidth'] = b_w
                    input(f"Your preferred quality is now {b_w}. Press enter to continue")
                    break
    elif opt == 4:
        opt = int(input("Would you like to:\n1 - Leave a review\n2 - See the current score and reviews\n3 - Exit\n")) #add fallback
        if opt == 1:
            review_page(choosen_one, title)
        elif opt == 2:
            print_reviews(choosen_one)
        
    return

#Mostra o catalogo baseado nos parametros
#CATEGORY: uma string que pode ser "movie", "show" ou "all"
#GENRE: uma lista de strings ou uma string que pode ser qualquer genero da genres_list[]
def show_catalogs(category, genre):
    os.system('cls')
    i = 1
    titles = []
    if isinstance(genre, str): #se 'genre' for uma string, transforma ela em uma lista
        genre = [genre]

    if category == "movie" or category == "all":
        print("Movies:")
        for gen in genre:
            print(f"\n{gen.title()}:")

            for movie in movie_catalog[gen].keys():
                print(f"{i} - {movie} | ", end='')
                i += 1
                titles.append((gen, "movie", movie)) #guarda a tupla do genero, categoria e titulo do filme

    
    if category == "show" or category == "all":
        print("\n\nShows:")
        for gen in genre:
            print(f"\n{gen.title()}")

            for show in show_catalog[gen].keys():
                print(f"{i} - {show} | ", end='')
                i += 1
                titles.append((gen, "show", show))

    opt = int(input(f"\n\nEnter the number of wich item you want to watch: "))
    genre_c, category_c, title_c = titles[opt - 1] #como o i começa em 1, opt deve ser subtraida

    show_details(genre_c, category_c, title_c)

#Passa as informações de genero e categoria favoritos do perfil para o show_catalogs()
def recommendations_page():
    global choosen_profile
    category = choosen_profile['c_preference']
    genres = choosen_profile['g_preference']

    show_catalogs(category, genres)

#Lista os generos a serem escolhidos
def genre_page():
    while(1):
        os.system('cls')
        print("Enter the genre to browse on or type 'exit' to cancel.")

        for i in range(len(genres_list)):
            print(f"{genres_list[i].title()} | ", end='')

        opt = str(input("\n"))
        opt = opt.lower() #deixa a escolha em letras minusculas

        if opt == "exit":
            return
        elif opt in genres_list:
            show_catalogs("all", opt)
        else:
            input("This genre is not availabe, press enter to try again")

#Lista as categorias a serem escolhidas
def category_page():
    while(1):
        os.system('cls')
        print("Choose a category to browse on or type 'exit' to cancel.")

        opt = str(input("'Movie' or 'Show'\n"))
        opt = opt.lower()

        if opt == "exit":
            return
        elif opt == "movie" or opt == "show":
            show_catalogs(opt, genres_list)
        else:
            input("This category is not availabe, press enter to try again")

#Lista os itens salvos, podendo ser escolhidos também
def bookmarks_page():
    os.system('cls')
    global choosen_profile 
    if len(choosen_profile['bookmarks']) == 0:
        input("There are no bookmarks. Press enter to exit.")
    else:
        bm_list = []
        i = 1

        for bookmark in choosen_profile['bookmarks']:
            print(f"{i} - Title: {bookmark['title']}, Genre: {bookmark['genre']}")
            bm_list.append(bookmark)
            i += 1
        
        opt = int(input("Enter wich item you want to watch: "))
        sel = bm_list[opt - 1]
        show_details(sel['genre'], sel['category'], sel['title'])

#Lista os itens que foram assistidos
def watch_history_page():
    os.system('cls')
    global choosen_profile
    if len(choosen_profile['w_history']) == 0:
        input("You haven't watched anything recently. Press enter to exit.")
    else:
        w_list = []
        i = 1

        for h_item in choosen_profile['w_history']:
            print(f"{i} - Title: {h_item['title']}, Genre: {h_item['genre']}")
            w_list.append(h_item)
            i += 1
        
        opt = int(input("Enter wich item you want to watch: "))
        sel = w_list[opt - 1]
        show_details(sel['genre'], sel['category'], sel['title'])

# ----MENUS----

# Menu de login, 
def login_menu():
    while(1):
        os.system('cls')

        print("Welcome to [site name], would you like to:\n1 - Log in\n2 - Create an account\n3 - Log out")

        opt = int(input())
        if opt == 1:
            if user_login():
                initial_menu()
        elif opt == 2:
            create_a_user()
        elif opt == 3:
            break

# Menu para seleção de perfis
def initial_menu():
    while(1):
        if len(profile_list) == 0: #Inicio do programa, nenhum perfil criado
            create_profile()

        else:
            os.system('cls') #Limpa a tela
            print("Hello, would you like to access a profile or create a new one?")
            option = int(input("1 - Access a profile\n2 - Create a new one\n3 - Delete a profile\n4 - Account settings\n5 - Exit\n"))

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
                print("Are you sure you want to log out? Y/N")
                assurance = str(input())
                if assurance == "Y":
                    break

# Menu inicial onde será mostrado o catálogo de filmes e séries
def main_menu():
    while(1):
        os.system('cls')
        print(f"Hello, {choosen_profile['first']}, what will you watch today?\n")
        opt = int(input("Browse by:\n1 - Recommendations based on your preferences\n2 - Category\n3 - Genre\n4 - Bookmarks\n5 - Watch History\n6 - Exit\n"))

        if opt == 1:
            recommendations_page()
        elif opt == 2:
            category_page()
        elif opt == 3:
            genre_page()
        elif opt == 4:
            bookmarks_page()
        elif opt == 5:
            watch_history_page()
        elif opt == 6:
            return

#---

login_menu()
