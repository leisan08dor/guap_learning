class Soda:
    def _init_(self, add=None):
        self.add=add
    def show_my_drink(self):
        if not self.add:
            print(f'Газировка и {self.add}')
        else:
            print('Обычная газировка')
sd1=Soda('Дюшес')
sd1.show_my_drink()
sd2=Soda()
sd2.show_my_drink()