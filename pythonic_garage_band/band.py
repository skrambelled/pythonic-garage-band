class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances += [self.name]

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos += [member.play_solo()]
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name, instrument=None, solo=None):
        if self.__class__.__name__ == "Musician":
            raise NotImplementedError("Musician is for inheritance only")
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitar', 'face melting guitar solo')


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'bass', 'bom bom buh bom')


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drums', 'rattle boom crash')
