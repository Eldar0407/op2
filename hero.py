class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health = health_points
        self.catchphrase = catchphrase
    def Name(self):
        print(self.name)
    def Upgrade(self):
        self.health = self.health*2
    def __str__(self):
        return (f'Прозвище:{self.nickname}\n'
                f'Суперспособность:{self.superpower}\n'
                f'Здоровье:{self.health}\n')
    def __len__(self):
        return len(self.catchphrase)

Eldar1 = SuperHero('Eldar', 'Eldarrr', 'Speed', 200, 'Lets go!')
print(Eldar1)
Eldar1.Name()
Eldar1.Upgrade()
print(Eldar1)
print(len(Eldar1))


class AirHero(SuperHero):
    people = 'birds'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def Upgrade(self):
        self.health = self.health**2
    def TRu(self):
        return print('True in the True_phrase')

Eldar2 = AirHero('Eldar', 'Eldarrr', 'Speed', 200, 'Lets go!', 50, False)

Eldar2.TRu()
Eldar2.Upgrade()

class CosmoHero(SuperHero):
    people = 'alien'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def Upgrade(self):
        self.health = self.health ** 2

    def TR(self):
        return print('True in the True_phrase')


Eldar3 = CosmoHero('Eldar', 'Eldarrr', 'Speed', 200, 'Lets go!', 50, False)

Eldar3.TR()
Eldar3.Upgrade()

class Villain(AirHero):
    people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)

    def gen_x(self):...
    def crit(self):
        self.damage = self.damage**2

Eldar4 = Villain('Eldar', 'Eldarrr', 'Speed', 200, 'Lets go!', 50, False)
Eldar3.crit()
#Метод crit не работает на объекте класса CosmoHero т.к. не объявлен в нём
#Некоторые части домашнего задания не были для меня понятны(смысл).
#Предполагаю, что некоторые действия связаны с будущими дз и поэтому сделал все как понял по описанию
