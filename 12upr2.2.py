class mother:
    age = 0
    name = " "
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def __str__(self):
        return ('this is mother. her name is ' + str(self.name) )

class daughter(mother):
    def __str__(self):
        super().__str__()
        return ('this is daugther. her name is ' + str(self.name) + '. shes ' + str(self.age) + ' years old')


d = daughter(3,'alla')


m = mother(8,'vanya')


print(m)
print(d)