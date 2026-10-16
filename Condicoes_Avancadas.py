idade = int(input("Qual é a sua idade? "))

if idade <= 18:
    print("Tá novinho em? ")
elif idade >18 and idade <= 25:
    print("Tá na flor da idade")
elif idade >25 and idade <= 40:
    print("Tá maduro, tá bão")
elif idade >40:
    print("Tá acabado") 