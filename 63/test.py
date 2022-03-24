class LampRow:
    __state = 0

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, val):
        self.__state = val


class Win:
    size = [1000, 600]

    @property
    def width(self):
        return self.size[0]

    @width.setter
    def state(self, val):
        self.size[0] = val

    mode = 'main'


lamps = LampRow()
lamps.state = 1
print(lamps.state)

a = Win()
a.width = 0
print(a.size)
