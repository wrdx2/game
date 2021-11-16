from Bullet import Bullet


class Tank:
    def __init__(self, x=0, y=0, lv=0, name="", life=5, life_time=0, bullet=None):
        self.__x = x
        self.__y = y
        self.__lv = lv
        self.__name = name
        self.__life = life
        self.__life_time = life_time
        self.__bullet = bullet

    def get_local(self):
        return [self.__x, self.__y]

    def move(self, x, y):
        self.__x += (x * (self.__lv + 1))
        self.__y += (y * (self.__lv + 1))

    def shooting(self, direction):
        bu = Bullet(self.__x, self.__y, self.__lv, self.__name, direction)
        if self.__bullet is None:
            self.__bullet = []
        self.__bullet.append(bu)

    def bullet_move(self):
        for bullet in self.__bullet:
            bullet.move()

    def get_bullet(self):
        return self.__bullet

    def get_bullet_num(self):
        return 0 if self.__bullet is None else len(self.__bullet)
