from core.system import System


class CombatSystem(System):

    components = ['Health', 'Damage']

    def update(self, dt=None):
        # breakpoint()
        cowboys = (e for e in self.entities if e.race.race == 'cowboy' and e.health.alive)
        aliens = (e for e in self.entities if e.race.race == 'alien' and e.health.alive)

        # Combat happens simultaneously and to the death
        cowboy = next(cowboys, None)
        alien = next(aliens, None)
        # breakpoint()

        if cowboy and alien:
            while cowboy.health.alive and alien.health.alive:
                alien.health.current = alien.health.current - cowboy.damage()
                cowboy.health.current = cowboy.health.current - alien.damage()
