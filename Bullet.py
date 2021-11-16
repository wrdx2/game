class Bullet:
    def __init__(self, x=0, y=0, lv=0, name="", direction=""):
        self.__x = x
        self.__y = y
        self.__lv = lv
        self.__name = name
        self.__direction = direction

    def get_local(self):
        return [self.__x, self.__y]

    def move(self):
        if self.__direction == "up":
            self.__y -= self.__lv + 1
        if self.__direction == "down":
            self.__y += self.__lv + 1
        if self.__direction == "left":
            self.__x -= self.__lv + 1
        if self.__direction == "right":
            self.__x += self.__lv + 1
