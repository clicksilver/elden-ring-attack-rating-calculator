"""
Maps the weapon (name, affinity, upgrade) to the base attack ratings in each of
the damage types.
"""

def init_table():
    with open('data/Attack.csv') as f:
        lines = f.readlines();
        for i in range(len(lines)-1):
            line = lines[i+1]
            tokens = line.split(',')
            wep_aff_name = tokens[0]
            wep_attack = [float(elem) for elem in tokens[1:]]
            _TABLE[wep_aff_name] = wep_attack
    return

_TABLE = {}
init_table()

class WeaponAttackRatings:
    def __init__(self, values):
        self.phys_rating = values[0]
        self.magi_rating = values[1]
        self.fire_rating = values[2]
        self.litg_rating = values[3]
        self.holy_rating = values[4]
        self.stag_rating = values[5]

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
                self.phys_rating, self.magi_rating, self.fire_rating,
                self.litg_rating, self.holy_rating, self.stag_rating)

class WeaponAttackRatingsLevel:
    def __init__(self, name, values):
        self.map = {}
        for ulevel in range(26):
            stride = ulevel * 6
            ratings = WeaponAttackRatings(values[(stride):(stride+6)])
            self.map[ulevel] = ratings

def GetWeaponAttackRatings(name, affinity=None, level=0):
    key = name
    if affinity:
        key = '{} {}'.format(affinity, name)
    entry = _TABLE[key]
    weapon_ratings = WeaponAttackRatingsLevel(key, entry)
    return weapon_ratings.map[level]

if __name__ == "__main__":
    print(GetWeaponAttackRatings('Dagger', 'Blood', 5))
