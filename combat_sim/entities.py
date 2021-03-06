from core.entity import Entity

from components import Health, Damage, Humanoid

def setup_entities(number_of_cowboys=100, number_of_aliens=100):
    '''Sets up all the entities'''

    # Generate entities and add components to them
    cowboys = []
    for cowboy in range(number_of_cowboys):
        cowboy = Entity(f'cowboy-{cowboy:02}')
        cowboy.health = Health(current=51, max=51)
        cowboy.damage = Damage(normal=12, critical=17, critical_percent=10)
        cowboy.race = Humanoid(race='cowboy')
        cowboys.append(cowboy)

    aliens = []
    for alien in range(number_of_aliens):
        alien = Entity(f'alien-{alien:02}')
        alien.health = Health(current=102, max=102)
        alien.damage = Damage(normal=6, critical=8, critical_percent=20)
        alien.race = Humanoid(race='alien')
        aliens.append(alien)

    # Convenient dictionary splitting the two types of entities
    entities = {'cowboys': cowboys, 'aliens': aliens}
    return entities
