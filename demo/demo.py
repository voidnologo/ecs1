from components import Health, Damage
from entity import Entity


player = Entity('player', 0)
skeleton = Entity('skeleton-01', 1)

player.health = Health()
skeleton.health = Health()

player.damage = Damage()
skeleton.damage = Damage()

print(f'Player health: {player.health.current}')
player.health.current -= skeleton.damage()
print(f'Player health after attack: {player.health.current}')
