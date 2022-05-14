print("Antes del while")
valor = 0
while(valor<5):
    valor+=1
    if(valor==3):
        continue
    print(f"Valor actual:{valor}")

print("Después del while")

print("Antes del while")
valor = 0
while(valor<5):
    valor+=1
    if(valor>3):
        continue
    print(f"Valor actual:{valor}")

print("Después del while")