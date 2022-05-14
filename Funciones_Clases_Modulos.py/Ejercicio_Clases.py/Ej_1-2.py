class Jets:
    def __init__(self,name,country,cantidad): #valores q paso a la construccion, name y country
        self.name = name
        self.origin = country
        self.cantidad = cantidad

    def _str_(self):
        return "{}->{}".format(self.name, self.origin)

first_item = Jets("F16", "USA") # , le digo a la variable q asigne el valor, crreando el obj first item aqui llamo a init y creo el objeto

a=first_item.name
b= first_item.origin
print(a)
print(b)

# 3 
first_item=Jets("F14","USA") #(name,country)
second_item=Jets("SU33","Russia")
third_item=Jets("AJS37","Sweden")
fourth_item=Jets("Mirage2000","France")
fifth_item=Jets("Mig29","USSR")
sixth_item=Jets("A10","USA")
first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
print(first_army)

# 4
first_item=Jets('A','F14',87)
second_item=Jets('B','Mirage2000',35)
total=first_item.cantidad + second_item.cantidad
print(total)