#lista de comprension
frutas = ['mango','banano','papaya','granadilla']

nueva_lista=[] #aqui pasen los nuevos elementos solo cuya letra a apareca
for fruta in frutas:
    if "a" in fruta:
        nueva_lista.append(fruta)

nueva_lista = [fruta for fruta in frutas if "a" in frutas]
nueva_lista.append(frutas)
print(nueva_lista)