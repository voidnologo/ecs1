from core.system import System


class CombatSystem(System):

    components = ['Health', 'Damage']

    def update(self, dt=None):
        for entity in self.entities:
            for opponent in self.entities if opponent is not entity:
                opponent.health.current -= entity.damage()



