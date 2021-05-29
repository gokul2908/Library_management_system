class Person:
    def __init__(self, name, age, address, sex) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.sex = sex
    
    def __str__(self) -> str:
        return f'name is: {self.name} \nAge is {self.age} \nAddress: {self.address} \ngender:{self.sex}'
