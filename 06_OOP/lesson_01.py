class Enemy:
    count = 0

    def __init__(self, hp, armor, dmg, name, speed):
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.name = name
        self.speed = speed

    def attack(self):
        print(f'{self.name} атакует с уроном {self.dmg}')

    def move(self):
        print(f'{self.name} движется')


class Dragon(Enemy):

    def __init__(self, hp, armor, dmg, name, speed, fly_speed):
        Enemy.__init__(self, hp, armor, dmg, name, speed)
        self.fly_speed = fly_speed

    def fly(self):
        print(f'{self.name} летит')

    def attack(self):
        print(f'{self.name} дышит огнем с уроном {self.dmg}')


class Witch(Enemy):
    def spoilage(self):
        print(f'{self.name} колдует')


orche = Enemy(150, 30, 25, 'Орче', 20)
elf = Enemy(100, 25, 20, 'Сильвана', 30)
gorynych = Dragon(150, 30, 25, 'Горыныч', 20, 40)
baba_yaga = Witch(00, 25, 20, 'Ягя', 30)

orche.attack()
elf.attack()
gorynych.attack()
baba_yaga.attack()