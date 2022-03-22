print('62, A\n')

class LampRow:
    def __init__(self):
        self.wipe()
    
    def wipe(self):
        self.state = '0' * 8

    def show(self):
        if len(self.state) != 8:
            self.wipe()
        print(str(self.state).replace('0', '-').replace('1', '*'))


lamps = LampRow()
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()