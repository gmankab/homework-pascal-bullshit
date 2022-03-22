class Animal:
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = 'aboba',
    ):
        self.__name = name
        self.__age = age
        self.__phrase = phrase

    @property
    def name(self) -> str:
        return self.__name
        
    @property
    def age(self) -> int:
        return f'{self.__age} лет'

    @property
    def phrase(self) -> str:
        return self.__phrase
    
    def make_older(
        self,
        years: int = 1
    ) -> None:
        self.__age += years
    
    def say(
        self,
        phrase: str = None,
    ):
        if not phrase:
            phrase = self.phrase
        print(f'{self.__name}: {phrase}')


class Mammal(Animal):
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = 'aboba'
    ):
        Animal.__init__(
            self = self,
            name = name,
            age = age,
            phrase = phrase
        )
    
    def run(self):
        print(f'{self.name} побежал...')


class Dog(Mammal):
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = 'Гав!'
    ):
        Mammal.__init__(
            self = self,
            name = name,
            age = age,
            phrase = phrase
        )


class Cat(Mammal):
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = 'Мяу!'
    ):
        Mammal.__init__(
            self = self,
            name = name,
            age = age,
            phrase = phrase
        )


class Reptile(Animal):
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = 'aboba'
    ):
        Animal.__init__(
            self = self,
            name = name,
            age = age,
            phrase = phrase
        )

    def crawl(self):
        print(f'{self.name} пополз...')


class Turtle(Reptile):
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = '...'
    ):
        Reptile.__init__(
            self = self,
            name = name,
            age = age,
            phrase = phrase
        )
    

class Snake(Reptile):
    def __init__(
        self,
        name: str,
        age: int,
        phrase: str = 'ш-ш-ш-ш...'
    ):
        Reptile.__init__(
            self = self,
            name = name,
            age = age,
            phrase = phrase
        )
