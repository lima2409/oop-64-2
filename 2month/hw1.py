class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

    def attack(self):
        print(f'{self.name}: наносит удар!')
        self.strength -= 1

    def rest(self):
        print(f'{self.name}: отдыхает…')
        self.health += 1

satoru = Hero("Satoru", 999, 10000, 10000000000000)
sukuna = Hero("Sukuna", 600, 10000, 10000000000)
satoru.greet()
sukuna.greet()
satoru.attack()
print(satoru.strength)
sukuna.attack()
print(sukuna.strength)
satoru.rest()
print(satoru.health)
sukuna.rest()
print(sukuna.health)