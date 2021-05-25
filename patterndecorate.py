"""
    En Python, les fonctions sont des objets comme les autres : elles peuvent donc être passées à d’autres fonctions et en sortir comme n’importe quelle autre valeur.

    Le design pattern Décorateur fournit une façon de modifier une fonction, souvent en ajoutant des fonctionnalités avant et après son exécution.

    Il peut être utile lorsque plusieurs fonctions similaires ont des fonctionnalités centrales différentes, mais des fonctionnalités partagées significatives.

    Il peut aussi être utile lorsque vous ne souhaitez pas modifier le code interne d’une fonction, pour pouvoir la réutiliser de différentes manières.

    La syntaxe  @decorate_function  simplifie l’écriture de code impliquant des décorateurs.
"""

from time import time, sleep


def calculate_time_spent(function):
    """calcule le temps que met une fonction à s'executer."""

    # notez *args et **kwargs. Ce sont des paramètres dynamiques
    # qui permet au décorateur de s'adapter à tout type de fonction !
    # N'hésitez pas à vous documenter sur l'unpacking pour en apprendre
    # davantage.
    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # On appelle cela le temps "epoch".
        start = time()

        result = function()

        # mettez ici votre code. Il s'agit de faire la différence entre
        # 2 temps "epochs", celui qui est gardé dans "start", et celui qui
        # sera gardé dans votre variable 'end'. ;)
        end = time()
        time_spent = end - start
        print(f"secondes passées: {time_spent:.2f}")

        return result

    return wrapper


@calculate_time_spent
def calculate_the_trajectory():
    """Calcule la trajectoire du vaisseau."""
    print("Calcul en cours...")
    sleep(3)  # on met le programme en pause pendant 3 secondes !
    print("Calcul terminé !")


calculate_the_trajectory()