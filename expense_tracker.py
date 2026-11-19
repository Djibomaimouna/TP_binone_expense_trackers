expenses = []

def delete_expense():
    if not expenses:
        print("Aucune dépense à supprimer.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

    choice = input("Numéro de la dépense à supprimer : ").strip()
    if not choice.isdigit():
        print("Numéro de dépense invalide.")
        return

    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Dépense supprimée : {removed['description']}")
    else:
        print("Numéro de dépense invalide.")

def add_expense():
    description = input("Description de la dépense : ")
    try:
        amount = float(input("Montant de la dépense : "))
    except ValueError:
        print("Montant invalide.")
        return
    expenses.append({"description": description, "amount": amount})
    print("Dépense ajoutée !")

def show_expenses():
    if not expenses:
        print("Aucune dépense enregistrée.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total : {total:.2f}")

def main():
    while True:
        print("\n===== SUIVI DES DÉPENSES =====")
        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3. Afficher le total")
        print("4. Supprimer une dépense")
        print("5. Quitter")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
