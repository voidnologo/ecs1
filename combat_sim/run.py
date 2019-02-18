from entities import setup_entities
from systems import CombatSystem

def simulate(number_of_cowboys, number_of_aliens):
    '''Simulates combat between aliens and cowboys'''
    combat_system = CombatSystem()

    entities = setup_entities(number_of_cowboys, number_of_aliens)

    print('='*40)
    print(' Combat Sim: Cowboys vs Aliens')
    print('-'*40)
    print("Round: # -- C | A")
    print('-----------------')
    combat_rounds = 0
    while True:
        cowboys_alive = sum(e.health.alive for e in entities['cowboys'])
        aliens_alive = sum(e.health.alive for e in entities['aliens'])
        if cowboys_alive == 0 or aliens_alive == 0:
            break
        print(f'Round: {combat_rounds} -- {cowboys_alive} | {aliens_alive}')
        combat_rounds += 1
        combat_system.update()

    print('='*40)
    print(f' Finished in {combat_rounds} round(s)')
    print('-'*40)
    alive = {
        'cowboys': sum(e.health.alive for e in entities['cowboys']),
        'aliens': sum(e.health.alive for e in entities['aliens'])
    }
    print(f'Cowboys alive: {alive["cowboys"]}')
    print(f'Aliens alive: {alive["aliens"]}')
    print('-'*40)
    if alive['cowboys'] > 0:
        print(' Cowboys win')
    elif alive['aliens'] > 0:
        print(' Aliens win')
    else:
        print(' Everyone died!')
    print('\n')


if __name__ == '__main__':
    number_of_cowboys = 100
    number_of_aliens = 100
    print(f'simulate({number_of_cowboys}, {number_of_aliens})')
    simulate(number_of_cowboys, number_of_aliens)

