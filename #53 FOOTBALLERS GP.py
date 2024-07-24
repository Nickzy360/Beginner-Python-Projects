#ამოცანა: დაამატეთ ორი ობიექტი ფეხბურთელების სახით, და დაამატეთ მეთოდები: ასაკის და ნომრის ცალცალკე გამოსატანად.
#ასევე დააამატეთ მეთოდი რომელიც გამოიტანს ატრიბუტრბს შემდეგი ფორმით: სახელი: Khvicha Kvaratskhelia, ასაკი: 23, ნაკრებში მაისურის ნომერი: "7"

class Footballer:
    def __init__(self,name,surname,age,number):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
    def getfullname(self):
        return f'{self.name} {self.surname}'
    def getage(self):
        return f'{self.age}'
    def getnumber(self):
        return f'{self.number}'
    def getdata(self):
        return f'სახელი: {self.name} {self.surname}, ასაკი: {self.age} წლის, მაისურის ნომერი ნაკრებში: {self.number}.'
mamardashvili = Footballer("Giorgi","Mamardashvili",24,"25")    
kvara = Footballer("Khvicha","Kvaratskhelia",23,"77")
print(kvara.getdata())
