#Funcão que irá filtrar os candidatos de acordo com as notas digitadas pelo usuário
#Utilizando split, cada nota é selecionada de acordo com seu posicionamento na String, pulando os "_" e a partir do indice 1
#If para verificar e adicionar na lista de aprovados apenas os candidatos que passarem nos requesitos mínimos
def filtraCandidatos(entrevista, testeTeorico, testePratico, softSkills, notas):

    candidato = " ".join(notas)
    entrevista, testeTeorico, testePratico, softSkills = candidato.split("_")
    entrevista = int(entrevista[1:])
    testeTeorico = int(testeTeorico[1:])
    testePratico = int(testePratico[1:])
    softSkills = int(softSkills[1:])

    if entrevista >= usuarioE and testeTeorico >= usuarioT and testePratico >= usuarioP and softSkills >= usuarioS:
        listaAprovados.append(notas)

#Lista de candidatos
candidato1 = ["e5_t10_p8_s8"]
candidato2 = ["e10_t7_p7_s8"]
candidato3 = ["e8_t5_p4_s9"]
candidato4 = ["e2_t2_p2_s1"]
candidato5 = ["e10_t10_p8_s9"]

#Lista de canditatos aprovados (é preenchida de acordo com o andamento da função (filtraCandidatos))
listaAprovados = []

#Variáveis vazias das notas dos candidatos, que são chamadas em conjunto da função (filtraCandidatos)
entrevista = 0
testeTeorico = 0
testePratico = 0
softSkills = 0

#Inputs para o usuário inserir as notas desejadas
usuarioE = int(input("Digite a nota mínima da Entrevista: "))
usuarioT = int(input("Digite a nota mínima do Teste Teórico: "))
usuarioP = int(input("Digite a nota mínima do Teste Prático: "))
usuarioS = int(input("Digite a nota mínima de Soft Skills: "))

#Chamada da função filtraCandidatos
filtraCandidatos(entrevista, testeTeorico, testePratico, softSkills, candidato1)
filtraCandidatos(entrevista, testeTeorico, testePratico, softSkills, candidato2)
filtraCandidatos(entrevista, testeTeorico, testePratico, softSkills, candidato3)
filtraCandidatos(entrevista, testeTeorico, testePratico, softSkills, candidato4)
filtraCandidatos(entrevista, testeTeorico, testePratico, softSkills, candidato5)

#Pilha de ifs para printar cada candidato da lista, de acordo com o seu número no cadastro
if candidato1 in listaAprovados:
    print("Candidato 1 ", candidato1)
if candidato2 in listaAprovados:
    print("Candidato 2 ", candidato2)
if candidato3 in listaAprovados:
    print("Candidato 3 ", candidato3)
if candidato4 in listaAprovados:
    print("Candidato 4 ", candidato4)
if candidato5 in listaAprovados:
    print("Candidato 5 ", candidato5)
else:
    print("Nenhum candidato aprovado!")

