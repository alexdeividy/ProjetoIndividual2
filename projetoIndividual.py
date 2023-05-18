
candidato1 = ["e5_t10_p8_s8"]
candidato2 = ["e10_t7_p7_s8"]
candidato3 = ["e8_t5_p4_s9"]
candidato4 = ["e2_t2_p2_s1"]
candidato5 = ["e10_t10_p8_s9"]

listaAprovados = []

n1 = 0
n2 = 0
n3 = 0
n4 = 0

usuarioE = int(input("Digite a nota minima para a Entrevista: "))
usuarioT = int(input("Digite a nota minima para o Teste Teórico: "))
usuarioP = int(input("Digite a nota minima para o Teste Prático: "))
usuarioS = int(input("Digite a nota minima para as Soft Skills: "))

def filtraUsuarios(n1, n2, n3, n4, notas):

    candidato = " ".join(notas)
    n1, n2, n3, n4 = candidato.split("_")
    n1 = int(n1[1:])
    n2 = int(n2[1:])
    n3 = int(n3[1:])
    n4 = int(n4[1:])

    if n1 >= usuarioE and n2 >= usuarioT and n3 >= usuarioP and n4 >= usuarioS:
        listaAprovados.append(candidato)

filtraUsuarios(n1, n2, n3, n4, candidato1)
filtraUsuarios(n1, n2, n3, n4, candidato2)
filtraUsuarios(n1, n2, n3, n4, candidato3)
filtraUsuarios(n1, n2, n3, n4, candidato4)
filtraUsuarios(n1, n2, n3, n4, candidato5)

print(listaAprovados)
