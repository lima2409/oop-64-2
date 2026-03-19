import random


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


class Warrior(Hero):
    def __init__(self, name, level, health, strength,stamina):
        super().__init__(name, level, health, strength)
        self.stamina=stamina

    def attack(self):
        print('Воин атакует мечом!')
        return super().attack()    


class Mage(Hero):
    def __init__(self, name, level, health, strength,mana):
        super().__init__(name, level, health, strength)
        self.mana=mana

    def attack(self):
        print('Маг кастует заклинание!')
        return super().attack()    

class Assassin(Hero):
    def __init__(self, name, level, health, strength,stealth):
        super().__init__(name, level, health, strength)
        self.stealth=stealth

    def attack(self):
        print('Ассасин атакует из-под тишка!')
        return super().attack()    
    
warrior = Warrior('Argus',15,15000,30000,8)
mage = Mage('Kagura',15,5000,15000,10)
assassin = Assassin('Aamon',15,8000,15000,3)

heroes_choise = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

user = input(f'Выберите героя:warrior,mage,assassin:').lower()
user_hero = heroes_choise.get(user)
enemy_hero = random.choice(list(heroes_choise.values()))

user_class = user_hero.__class__.__name__
enemy_class = enemy_hero.__class__.__name__
print(f'Вы выбрали:{user_class }')
print(f'Герой противника: {enemy_class}')

rules = {
    'Warrior':'Assassin',
    'Assassin':'Mage',
    'Mage':'Warrior'
}

if rules[user_class] == enemy_class:
    print(f'{user_class} победил!')

elif rules[enemy_class] == user_class:
    print(f'{enemy_class} победил!') 

else:
    print('ничья)')
