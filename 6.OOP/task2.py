'''
Реализирайте клас Projectline, моделиращ снаряд, изстрелян във въздуха. Снаряда има маса, x и y координати.
Реализирайте следните методи: конструктор с маса на снаряда и x координата (y е нула) метод move, който придвижва снаряда на време t.
Той променя x и y. Метод shoot с параметри ъгъл и начална скорост. Методът да вика move през 0.1 секунди, докато y координатата не
стане 0. Нека програмата ви прави инстанция на такъв клас, като пита потребителя за ъгъл и начална скорост и след това извиква shoot.
Текущите координати да се разпечатат във вид, удобен за внасяне в електронна таблица и изчертаването им.
'''
import math


class Projectile:
    def __init__(self, mass, x):
        self.mass = mass
        self.x = x
        self.y = 0
        self.angle = 0
        self.initial_velocity = 0

    def move(self, t):
        self.x += self.initial_velocity * math.cos(math.radians(self.angle)) * t
        self.y += self.initial_velocity * math.sin(math.radians(self.angle)) * t - 0.5 * 9.81 * t ** 2
        self.initial_velocity -= 9.81 * t

    def shoot(self, angle, initial_velocity):
        self.angle = angle
        self.initial_velocity = initial_velocity

        time_step = 0.1
        time = 0

        print("X (m)\t\tY (m)")
        while self.y >= 0:
            print(f"{self.x:.2f}\t\t{self.y:.2f}")
            self.move(time_step)
            time += time_step


if __name__ == "__main__":
    mass = float(input("Projectile mass: "))
    x = float(input("X coordinat: "))
    angle = float(input("Angle: "))
    initial_velocity = float(input("Velocity(m/s): "))

    projectile = Projectile(mass, x)
    projectile.shoot(angle, initial_velocity)
