class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient,str):
            self.ingredient = ingredient
        else:
            self.ingredient = "banana"

    def show_my_drink(self):
        if self.ingredient:
            print(f'Soda with {self.ingredient}')  
        else:
            print(' Basic soda')

drink1 = Soda()
drink2 = Soda('Skibidi toilet flavour ')
drink3 = Soda(999999)

drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

