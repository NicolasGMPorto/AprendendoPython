mencoes = []

for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    mencoes.append(resultado)

print("Quantidade de menções", len(mencoes))

for n in mencoes:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota", nota)