nombre_a_gauche = 5
nombre_a_droite = 10
symbole = "addition"
resultat = 0

match symbole :
      case "addition":
          resultat=nombre_a_gauche + nombre_a_droite
        print(f"{nombre_a_gauche} + {nombre_a_droite} ={resultat}")
      case "soustraction":
      case "multiplication":
      case "division":
          
