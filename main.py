import json

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

def verif_age(age) :
    if age >0 and age <150:
        return True
    return False    

def menu() :
    menu_ou_age = " Entrer le chiffre correspondant à votre choix \n"

    while True:
        num_entree = input(""" 
            Veuillez choisir l'une des options suivantes: 
            
            
            1.  Ajouter un utilisateur (nom + âge)
            2.  Afficher tous les utilisateurs
            3.  Rechercher un utilisateur par nom
            4.  Supprimer un utilisateur de la liste 
            5.  Modifier la valeur d'un champ 
            6.  Quitter  

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
        
        ajouter_utilisateur(liste_utilisateurs, nom, age_valide)
        
        
        

    elif  num_valide == 2:
        print(liste_utilisateurs)

    elif  num_valide == 3:   
        nom = input("Quelle est le nom de l'utilisateur que vous chercher : \n")
        user = rechercher_user_par_nom(liste_utilisateurs, nom)    
        existence_user(user)
    elif  num_valide == 4:
        nom = input("Entree le nom complet de la personne à supprimer")
        supprimer_utilisateur(liste_utilisateurs, nom):

    
    elif  num_valide == 5:
        nom = input("Quel est le nom de l'utilisteur dont on veut faire les modifications : \n")
        age = input("Quel est votre âge : \n")
        a_modifie = input("Rentrer le nom du champ a modifié")
        a_modifie_par =input(f"Rentrer ce par quoi vous voulez remplacer {a_modifie} :  \n")
        
        champ, valeur = valider_modification(a_modifie, a_modifie_par)
        
        if champ is not None:
             modifier_utilisateurs(liste_utilisateurs, nom, champ, valeur)

       
    else :
        print("Trou noir!")

def charger_utilisateurs():
    try:
        with open("utilisateurs.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def sauvegarder_utilisateurs(liste):
    with open("utilisateurs.json", "w", encoding="utf-8") as f:
        json.dump(liste, f, ensure_ascii=False, indent=4)


def ajouter_utilisateur(liste, nom, age):
    utilisateur_recherche = rechercher_user_par_nom(liste, nom)
    if utilisateur_recherche is None :
        utilisateur = creer_utilisateur (nom, age)
        liste.append(utilisateur)
        sauvegarder_utilisateurs(liste)
        print(f"{utilisateur.get('nom')} a été ajouté à la liste. \n" )

    else :
        print(f"Le nom {nom} existe déjà. \n Veuillez consulter la liste pour savoir quel suffixe approprié approprié\n. ")
    

def supprimer_utilisateur(liste, nom):
    utilisateur_recherche = rechercher_user_par_nom(liste, nom)

    if utilisateur_recherche is None:
        print("Cet utilisateur n'existe pas.\n")
    else:
        liste.remove(utilisateur_recherche)
        sauvegarder_utilisateurs(liste)
        print(f"L'utilisateur {nom} a été supprimé.\n")



def valider_modification(a_modifier, a_modifier_par):

    # Nettoyage du champ
    a_modifier = a_modifier.strip().lower()

    # 1. Vérifier que le champ est valide
    if a_modifier not in ["nom", "age"]:
        print("Champ invalide.\n")
        return None, None

    # 2. Cas AGE
    if a_modifier == "age":
        try:
            a_modifier_par = int(a_modifier_par)
            if a_modifier_par <= 0:
                print("Âge invalide.\n")
                return None, None
        except:
            print("Veuillez entrer un nombre valide.\n")
            return None, None

    # 3. Cas NOM
    elif a_modifier == "nom":
        a_modifier_par = a_modifier_par.strip()

        if a_modifier_par == "":
            print("Nom invalide.\n")
            return None, None

    # 4. Retourner valeurs validées
    return a_modifier, a_modifier_par



def modifier_utilisateurs(liste_utilisateurs, nom, a_modifie, a_modifie_par):
    user = rechercher_user_par_nom(liste, nom)
    if user is None:
        print(f"Le nom {nom} n'existe pas ou est erroné. \n Veuillez consulter la liste pour vérifier l,existence du nom. ")

        
    else:
        if a_modifie in ["nom", "age"] and verif_age(age):

            user[a_modifie] = a_modifie_par
            
            sauvegarder_utilisateurs(liste)
        
        else:
            print(f"le champ a modifié {a_modifie} n'existe pas ou est erroné. \n Veillez consulter le format de la liste en sélectionnant afficher la liste. \n")
    
       

def main():
    liste_utilisateurs = charger_utilisateurs()
    while True :
        num_valide  = menu()
        if num_valide == 6:
            break
        else:
            action (num_valide, liste_utilisateurs)

main()