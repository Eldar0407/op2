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

Eldar = SuperHero('Eldar', 'Eldarrr', 'Speed', 200, 'Lets go!')
print(Eldar)
Eldar.Name()
Eldar.Upgrade()
print(Eldar)
print(len(Eldar))