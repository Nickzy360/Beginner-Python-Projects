class Footballer:
    def __init__(self, name, surname, age, number, nationality, club, birthdate, position):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
        self.nationality = nationality
        self.club = club
        self.birthdate = birthdate
        self.position = position
    
    def get_fullname(self):
        return f'{self.name} {self.surname}'
    def get_age(self):
        return f'{self.age}'
    def get_number(self):
        return f'{self.number}'
    def get_nationality(self):
        return f'{self.nationality}'
    def get_club(self):
        return f'{self.club}'
    def get_birthdate(self):
        return f'{self.birthdate}'
    def get_position(self):
        return f'{self.position}'
    def get_data(self):
        return (f'სახელი: {self.name} {self.surname}, ასაკი: {self.age} წლის, '
                f'(დაბადების თარიღი {self.birthdate}), მისი ეროვნება: {self.nationality}, '
                f'რომელი კლუბის წევრია: {self.club}, მაისურის ნომერი ნაკრებში: {self.number}, '
                f'პოზიცია: {self.position}.')
ronaldo = Footballer("Christiano", "Ronaldo", 39, "7", "პორტუგალია", "Al-Nassr FC", "5 თებერვალი, 1985", "Forward")
messi = Footballer("Lionel", "Messi", 37, "30", "არგენტინა", "Inter Miami CF", "24 ივნისი, 1987", "Forward")
mbappe = Footballer("Kylian", "Mbappé", 24, "7", "საფრანგეთი", "Paris Saint-Germain", "20 დეკემბერი, 1998", "Forward")
de_bruyne = Footballer("Kevin", "De Bruyne", 31, "17", "ბელგია", "Manchester City", "28 ივნისი, 1991", "Midfielder")
lewandowski = Footballer("Robert", "Lewandowski", 34, "9", "პოლონეთი", "FC Barcelona", "21 აგვისტო, 1988", "Forward")
print(ronaldo.get_data())
print(messi.get_data())
print(mbappe.get_data())
print(de_bruyne.get_data())
print(lewandowski.get_data())
