candidato1 = ["e8_t8_p8_s8"]
alex = " ".join(candidato1)
#---------------------------------#
candidato2 = ["e7_t7_p7_s7"]
joao = " ".join(candidato2)
#---------------------------------#
candidato3 = ["e6_t6_p6_s6"]
pedro = " ".join(candidato3)
#---------------------------------#
candidato4 = ["e5_t5_p5_s5"]
lucas = " ".join(candidato4)
#---------------------------------#
candidato5 = ["e9_t9_p9_s9"]
rafael = " ".join(candidato5)

listaVazia = []
n1 = 0
n2 = 0
n3 = 0
n4 = 0

usuarioE = input("Digite a nota minima para a Entrevista: ")
usuarioT = input("Digite a nota minima para o Teste Teórico: ")
usuarioP = input("Digite a nota minima para o Teste Prático: ")
usuarioS = input("Digite a nota minima para as Soft Skills: ")

def projetoN(n1, n2, n3, n4, notas):

    n1 = notas[1]
    n2 = notas[4]
    n3 = notas[7]
    n4 = notas[10]

    if n1 >= usuarioE and n2 >= usuarioT and n3 >= usuarioP and n4 >= usuarioS:
        listaVazia.append(notas)
    
projetoN(n1, n2, n3, n4, alex)
projetoN(n1, n2, n3, n4, joao)
projetoN(n1, n2, n3, n4, pedro)
projetoN(n1, n2, n3, n4, lucas)
projetoN(n1, n2, n3, n4, rafael)

print(listaVazia)
