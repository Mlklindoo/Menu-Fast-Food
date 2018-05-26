menu = ["Cheeseburguer", "Nuggets", "Batata Frita"]
vsodio = [714, 360, 284]
vcal = [302, 159, 319]
indice = 1
totmen = len(menu)
inimenu = 0

def gera_menu():
    global indice
    global inimenu
    while indice <= totmen:
      print(indice, "-", menu[inimenu])
      indice = indice + 1
      inimenu = inimenu + 1

def op1():
    global totmen
    menu.append(str(input("Escreva qual comida deseja adicionar: ")))
    vsodio.append( int(input("Digite qual o valor total de sódio em mg, em número inteiro, do alimento a ser adicionado: ")))
    vcal.append(int(input("Digite quantas calorias em kcal, em número inteiro, o alimento a ser adicionado contém: ")))
    totmen = totmen + 1
    print("Alimento adicionado!")
    inicio()

def op2():
    gera_menu()

def inicio():
    print("Opções:")
    print("1 - Adicionar item no menu (Função em alpha, ainda não funciona)")
    print("2 - Mostrar menu")
    print("Escolha uma opção ")
    op = int(input("Digite a opção desejada:"))
    if op == 1:
        op1()
    if op == 2:
        op2()
    else:
        print("Seleção não encontrada, selecione novamente: ")
        inicio()

print("Vamos ver sobre calorias e VD's!\n")
inicio()

opcao = int(input("Selecione uma opção: "))
if opcao == 1:
    print("Opção escolhida: Cheeseburguer!")
    vds1 = ((vsodio[0]/1000)*100)/5
    float(vds1)
    print("O Chesseburguer contém {:.2f}% do seu valor recomendado de consumo de sódio diário." .format(vds1))
    vdc1 = (vcal[0]*100)/2000
    float(vdc1)
    print("O Cheeseburguer contém {:.2f}% do seu valor recomendado de consumo diário de calorias." .format(vdc1))

if opcao == 2:
    print("Opção escolhida: Nuggets!")
    vds2 = ((vsodio[1]/1000)*100)/5
    float(vds2)
    print("O Nugget contém {:.2f}% do seu valor recomendado de consumo de sódio diário." .format(vds2))
    vdc2 = (vcal[1]*100)/2000
    float(vdc2)
    print("O Nugget contém {:.2f}% do seu valor recomendado de consumo diário de calorias." .format(vdc2))

if opcao == 3:
    print("Opção escolhida: Batata Frita!")
    vds3 = ((vsodio[1] / 1000) * 100) / 5
    float(vds3)
    print("A Batata Frita contém {:.2f}% do seu valor recomendado de consumo de sódio diário.".format(vds3))
    vdc3 = (vcal[1] * 100) / 2000
    float(vdc3)
    print("O Nugget contém {:.2f}% do seu valor recomendado de consumo diário de calorias.".format(vdc3))

print("\nFim do Programa!")
