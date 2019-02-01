from random import randint

from core.component import Component


class Health(Component):
    defaults = {'current': 100, 'max': 100}

    @property
    def alive(self):
        return self.current > 0


class Damage(Component):
    defaults = {'normal': 10, 'critical': 15, 'critical_percent': 10}

    def __call__(self):
        '''Returns a damage calc based on properties'''
        crit = randint(0, 99) <= (self.critical_percent - 1)
        return self.critical if crit else self.normal
