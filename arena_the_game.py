from random import randint, uniform
from time import sleep


THINGS_NAMES = [
    'Warming Stone of the Lizard',
    'Runes of Grim Futures',
    'Singing Sword of Warning',
    'Farseeing Runes',
    'Cup of Compromise',
    'Cloak of Forgiveness',
    'Featherstep Boots',
    'Lipreading Goggles',
    'Saddle of the Skeletal Rider',
    'Herbacious Candle of Seduction',
    'Bracelet of Revival',
    'Chultish Vine Whip',
    'Jar of Stolen Souls',
    'Pyramid of Origins',
    'Self-Propelling Wagon',
    'Herbacious Candle of Seduction',
    'Critter Creator',
    'Runes of Grim Futures',
    'Imps Mantle',
    'Spoon of Seasoning',
    'Friendship-Seeking Hound Collar',
    'Chultish Vine Whip',
    'Law-Abiding Quiver',
    'Grail of Storms',
    'Lamp of the Elementals',
    'Barbarian’s Calming Helm',
    'Ethereal Elevator',
    'Anytender Coin',
    'Best-Forgotten Poems of the Wretched Bard',
    'Eavesdropper’s Earring'
    'Fancy Boots',
    'Torque Wrench of the Artificier',
    'Seeds of Hope',
    'Law-Abiding Quiver',
    'Bomb-Thrower’s Bandoleer',
    'Sculptable Setting Sand',
    'Jar of Stolen Souls',
    'Jagged Spoon of Surprise',
    'Beastcallers Horn',
    'One-Minute Tree Seeds',
    'Burn Book of the Nine Hells'
]

MAX_THINGS_MULTIPLIER = 0.1
MAX_THINGS_TO_ONE_PERSON = 4

PERSONS_NAMES = [
    'Caligula',
    'Super man',
    'Nikola Tesla',
    'Michael Jackson',
    'Anatoliy Dukalis',
    'Keanu Reeves',
    'Mikhail Parechenkov',
    'Karl Marx',
    'Stephen King',
    'Elvis Presley',
    'Homer Simpson',
    'Doctor Zoidberg',
    'Hank Hill',
    'Predator',
    'Alien',
    'Uncle Styopa',
    'Cheburashka',
    'Casper the friendly ghost',
    'Albert Einstein',
    'Vladimir Mayakovsky',
]

BASE_PERSON_PROTECTON = 0.01
BASE_ATTACK_DAMAGE = 25
BASE_HIT_POINTS = 100

PERSONS_COUNT = 10
THINGS_COUNT = MAX_THINGS_TO_ONE_PERSON * PERSONS_COUNT

things_names_editable = THINGS_NAMES.copy()
persons_names_editable = PERSONS_NAMES.copy()


def get_random_name(names: list) -> str:
    """Get name for Thing, Paladin, Warrior instances."""
    return names.pop(randint(0, len(names) - 1))


def get_random_things_multiplier(max_value=MAX_THINGS_MULTIPLIER) -> float:
    """Get rounded multiplier for Thing instance."""
    return round(uniform(max_value / 4, max_value), 3)


class Thing:
    """Useful magic items for in-game persons."""

    def __init__(self) -> None:
        self.name: str = get_random_name(things_names_editable)
        self.protection_multiplier: float = get_random_things_multiplier()
        self.attack_damage_multiplier: float = get_random_things_multiplier()
        self.hit_points_multiplier: float = get_random_things_multiplier()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Person:
    """Parent for game person classes."""

    def __init__(
            self,
            base_protection: float = BASE_PERSON_PROTECTON,
            base_attack_damage: int = BASE_ATTACK_DAMAGE,
            base_hit_points: int = BASE_HIT_POINTS
    ) -> None:
        self.name = get_random_name(persons_names_editable)
        self.base_protection = base_protection
        self.base_attack_damage = base_attack_damage
        self.base_hit_points = base_hit_points
        self.owned_things: list = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def set_things(self, things: list) -> None:
        """Dispance things to persons."""
        for _ in range(randint(1, MAX_THINGS_TO_ONE_PERSON)):
            self.owned_things.append(things.pop())

    def set_final_characteristics(
            self,
            things_protection: float,
            things_attack_damage: float,
            things_hit_points: float
    ) -> None:
        """Define person characteristics with things characteristics."""
        self.final_protection = round(
            self.base_protection + things_protection, 3
        )
        self.attack_damage = round(self.base_attack_damage + (
            self.base_attack_damage * things_attack_damage),
            3
        )
        self.hit_points = round(self.base_hit_points + (
            self.base_hit_points * things_hit_points),
            3
        )

    def get_recieving_damage(self, enemy_attack_damage: float) -> float:
        """Calculating damage according to person protection."""
        return round(enemy_attack_damage - (
            enemy_attack_damage * self.final_protection),
            3
        )

    def decrease_hit_points(self, enemy_attack_damage: float) -> None:
        """Deacresing person's hit points after recieving damage."""
        self.hit_points = round(
            self.hit_points - self.get_recieving_damage(enemy_attack_damage),
            3
        )


class Paladin(Person):
    """Properties of paladin type game person."""

    def __init__(self) -> None:
        super().__init__(
            base_protection=BASE_PERSON_PROTECTON * 2,
            base_hit_points=BASE_HIT_POINTS * 2
        )


class Warrior(Person):
    """Properties of warrior type game person."""

    def __init__(self) -> None:
        super().__init__(base_attack_damage=BASE_ATTACK_DAMAGE * 2)


def main():
    """Set game logic and process game events."""

    # Creating game objects (things, persons)
    things = sorted(
        [Thing() for _ in range(THINGS_COUNT)],
        key=lambda thing: thing.protection_multiplier
    )
    paladins = [Paladin() for _ in range(randint(0, PERSONS_COUNT))]
    warriors = [Warrior() for _ in range(PERSONS_COUNT - len(paladins))]

    # Adding persons to arena
    battle_arena: list = []
    battle_arena.extend(paladins)
    battle_arena.extend(warriors)

    # Dispancing things to persons and calculating persons final charac-s
    for person in battle_arena:
        person.set_things(things)
        person.set_final_characteristics(
            things_protection=sum(
                thing.protection_multiplier for thing in person.owned_things
            ),
            things_attack_damage=sum(
                thing.attack_damage_multiplier for thing in person.owned_things
            ),
            things_hit_points=sum(
                thing.hit_points_multiplier for thing in person.owned_things
            ))

    # Game cycle
    while len(battle_arena) != 1:

        # Choosing attacking and defending persons
        attacking_person: object = battle_arena.pop(
            randint(0, len(battle_arena) - 1)
        )
        defending_person: object = battle_arena.pop(
            randint(0, len(battle_arena) - 1)
        )

        # Deacresing defending person's hit points
        defending_person.decrease_hit_points(attacking_person.attack_damage)
        print(f'''{attacking_person} ⚔️  hits {defending_person}
                    with {defending_person.get_recieving_damage(
                  attacking_person.attack_damage)} damage''')
        print(f'{defending_person} has '
              f'{defending_person.hit_points} hit points ❤️\n')

        # Returning attacking person to battle arena list
        battle_arena.append(attacking_person)

        # Checking defending person's hit points number
        if defending_person.hit_points > 0:
            battle_arena.append(defending_person)
        else:
            print(f'💀💀💀 {defending_person} leaves battle arena 💀💀💀\n')
            sleep(0.1)
        sleep(0.25)

    print(f'🏆🏆🏆 OUR WINNER IS {battle_arena[0].name.upper()} 🏆🏆🏆')


if __name__ == '__main__':
    main()
