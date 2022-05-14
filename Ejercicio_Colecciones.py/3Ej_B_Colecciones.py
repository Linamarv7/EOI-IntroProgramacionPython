from random import randint

dataset = list(
        {
            "gender" : "F" if randint(0,1) == 0 else "M"
            "age": randint(0,120),   
        }
    )

print(dataset)

mujeres_mayores_edad= len(
        [
            person
            for person in dataset
            if person["gender" == "F"]
        ]
    )