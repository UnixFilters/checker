#!/usr/bin/env python3
import json, sys, difflib

if __name__ == "__main__":
    if len(sys.argv) != 4:
        # On vérifie le nombre d'arguments mais ça ne devrait pas se produire
        # (erreur du taskgrader)
        print("Error: invalid number of arguments.")
        sys.exit(1)

    # On lit les étapes générées par le programme
    stepsStr = open(sys.argv[1], "r").read()
    steps = json.loads(stepsStr)

    # On lit le fichier .in et .out qui ont été fournis au programme
    inputData = open(sys.argv[2], "r").read()
    expectedData = open(sys.argv[3], "r").read()

    # On définit le nombre d'étapes minimum pour résoudre l'exercice
    nb_steps_minimum = 3

    has_error = False
    nb_steps = 0

    # On enregistre les étapes où une erreur s'est produite
    failed_steps = [step for step in steps["steps"] if step["return"] != 0]
    if failed_steps:
        has_error = True

    # Fonction pour retourne le numéro du/des étapes(s) où une erreur s'est produite
    def returnStepWithError():
        return [step["number"] + 1 for step in failed_steps]

    # Comparaison des données attendues et générées
    last_output = steps["steps"][-1]["output"]
    if last_output:
        last_output_cleaned = "\n".join(
            line.strip() for line in last_output.splitlines()
        )
    else:
        last_output_cleaned = ""
    nb_steps = len(steps["steps"])
    result = {"score": 0, "message": "", "steps": steps}

    if not has_error:
        if last_output_cleaned.strip() == expectedData.strip():
            if nb_steps > nb_steps_minimum:
                result["score"] = 90
                result["message"] = (
                    f"Solution correcte mais peut être améliorée : votre commande est effectuée en {nb_steps} étape(s), "
                    f"elle pourrait être faite en {nb_steps_minimum} étape(s)."
                )
            else:
                result["score"] = 100
                result["message"] = "Solution correcte !"

        else:
            result["score"] = 0
            result["message"] = "Solution incorrecte !"

    else:
        result["score"] = 0
        result["message"] = (
            f"Il y a eu une erreur pendant l'exécution de votre programme lors de ou des étapes {returnStepWithError()}. "
            f"Corrigez et réessayez."
        )
    print(json.dumps(result))
