"""
Maps the weapon (name, affinity, and upgrade level) to the scaling factors for
each of the main stats (strength, dexterity, intelligence, faith, arcane).
"""

def init_table():
    with open('data/Scaling.csv') as f:
        lines = f.readlines();
        for i in range(len(lines)-1):
            line = lines[i+1]
            tokens = line.split(',')
            wep_aff_name = tokens[0]
            wep_scalings = [float(elem) for elem in tokens[1:]]
            _TABLE[wep_aff_name] = wep_scalings
    return

_TABLE = {}
init_table()

class StatScalingFactors:
    def __init__(self, values):
        self.stre_factor = values[0]
        self.dext_factor = values[1]
        self.inte_factor = values[2]
        self.fait_factor = values[3]
        self.arca_factor = values[4]

    def __str__(self):
        return '{} {} {} {} {}'.format(self.stre_factor, self.dext_factor,
                self.inte_factor, self.fait_factor, self.arca_factor)

class WeaponScaling:
    def __init__(self, name, values):
        self.level_to_scale_factor = {}
        for ulevel in range(26):
            stride = ulevel * 5
            scaling_factors = StatScalingFactors(values[(stride):(stride+5)])
            self.level_to_scale_factor[ulevel] = scaling_factors

def GetWeaponScalingFactors(name, affinity=None, level=0):
    key = name
    if affinity:
        key = '{} {}'.format(affinity, name)
    entry = _TABLE[key]
    weapon_scaling = WeaponScaling(key, entry)
    return weapon_scaling.level_to_scale_factor[level]

if __name__ == "__main__":
    print(GetWeaponScalingFactors('Dagger', 'Blood', 5))
