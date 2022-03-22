print('62, C\n')


def repl(_str: str, _dict: dict) -> str:
    for k, v in _dict.items():
        _str = _str.replace(str(k), str(v))
    return _str

class LampRow:
    def __init__(self, count: int = 8):
        self.count = count
        self.wipe()

    
    def __repr__(self):
        return repl(
            self.__state,
            {
                '0': '-',
                '1': '*',
                '2': 'o',
            },
        )
    

    def wipe(self):
        self.__state = '0' * self.count

    def show(self):
        print(self)
    
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, val):
        val = str(val)
        if len(val) == self.count:
            self.__state = val
        else:
            print(
                f'Ошибка, длина "{val}"'
                f' равна "{len(val)}"'
                f' вместо "{self.count}"'
            )
            self.wipe()



lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()
