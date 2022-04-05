class WaterBird:
    def __init__(self, name):
        self.name = name
        print("Bird is {}".format(self.name))

    def where_is_live(self):
        print("On the Earth")

    def swim(self):
        print("Can swim faster")

    def voice(self):
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print("Penguin is ready")

    def where_is_live(self):
        print("South Pole")

    def run(self):
        print("Run faster")

    def voice(self):
        print('Pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print("Anywhere")

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('Kra-kra-kra')


class Duck1(WaterBird):
    # def __init__(self, name):
    #     super().__init__(name)
    #     print('Duck is ready')

    def where_is_live(self):
        print(f'Name: {self.name}')
        print("Anywhere")

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('Kra-kra-kra')


peggy = Penguin('Ping')

peggy.where_is_live()
peggy.swim()
peggy.run()
peggy.voice()

print('======================')
duck = Duck('Donald Dug')

duck.where_is_live()
duck.swim()
duck.fly()
duck.voice()
