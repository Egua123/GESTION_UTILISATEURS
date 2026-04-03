print("bienvenue dans le programme de gestion d'utilisateur. \n")

def verification_num_entree (num_entree, menu_ou_age, age_ou_num) :
    
    try :
        
        num_valide = int(num_entree)
        if age_ou_num=="num" and num_valide >= 1 and num_valide <= 4 :
            return num_valide
        elif age_ou_num =="age":
            return num_valide
        else:
            print(f"Entrée invalide. { menu_ou_age } \n")
    except:

        print("Entrée invalide. Ce n'est pas un nombre. \n")

def menu() :
    menu_ou_age = " Entrer le chiffre correspondant à votre choix \n"

    while True:
        num_entree = input(""" 
            Veuillez choisir l'une des options suivantes: 
            
            
            1.  Ajouter un utilisateur (nom + âge)
            2.  Afficher tous les utilisateurs
            3.  Rechercher un utilisateur par nom  
            4.  Quitter  

        """)
    
        num_valide = verification_num_entree (num_entree, menu_ou_age, "num")

        if num_valide is not None :    
            return num_valide
        else :
            print("Vous n'avez pas rentrer le numéro approprié")

def creer_utilisateur (nom, age):
    utilisateur = {
        "nom" : nom,
        "age" : age

    }
    return utilisateur

def rechercher_user_par_nom(liste, nom):
    
    for user in liste:
        if user.get("nom") == nom :
            return user
            
    return None

def existence_user(user):
    if user is None :
        print("Cet utilsateur n'existe pas \n")
    else :
        print(f" vous avez cherher pour l'utilisateur {user.get('nom')} âgé de {user.get('age')}. \n")

def action (num_valide, liste_utilisateurs) :

    menu_ou_age = "Veuillez rentrer un nombre ( c'est l'âge qui est demnadé). \n "
    if num_valide == 1:

        nom = input("Quelle est votre nom au complet : \n")
        age = input("Quelle est votre äge : \n")
        age_valide = verification_num_entree (age, menu_ou_age, "age" )
        utilisateur = creer_utilisateur (nom, age_valide)
        liste_utilisateurs.append(utilisateur)
        print(f"{utilisateur.get('nom')} a été ajouté à la liste. \n" )


    elif  num_valide == 2:
        print(liste_utilisateurs)

    elif  num_valide == 3:   
        nom = input("Quelle est le nom de l'utilisateur que vous chercher : \n")
        user = rechercher_user_par_nom(liste_utilisateurs, nom)    
        existence_user(user)
    else :
        print("Trou noir!")


def main():
    liste_utilisateurs = []
    while True :
        num_valide  = menu()
        if num_valide == 4:
            break
        else:
            action (num_valide, liste_utilisateurs)

main()