"""
Lookup Table for a weapon (name and affinity) to it's Formula IDs for each
damage type, and it's Scaling ID.

Formula ID: IDs for each of the main damage types
            (Phys, Magic, Fire, Lightning, Holy)

Scaling ID: ID which maps to the scaling configuration of the weapon (which
            decides if a weapon's damage-type scales with each stat).
"""
import lookup_scaling_id_to_config as scaling_config

def init_table():
    with open('data/CalcCorrectGraph_ID.csv') as f:
        lines = f.readlines();
        for i in range(len(lines)-1):
            line = lines[i+1]
            tokens = line.split(',')
            wep_aff_name = tokens[0]
            wep_info = [int(elem) for elem in tokens[1:]]
            _TABLE[wep_aff_name] = wep_info
    return

_TABLE = {}
init_table()

class WeaponInfo:
    def __init__(self, name, values):
        self.name = name
        self.phys_formula_id = values[0]
        self.magi_formula_id = values[1]
        self.fire_formula_id = values[2]
        self.litg_formula_id = values[3]
        self.holy_formula_id = values[4]
        self.scaling_config = scaling_config.GetScalingConfig(values[-1])

    def __str__(self):
        return '{}\n{},{},{},{},{}\n{}'.format(self.name,
                self.phys_formula_id,
                self.magi_formula_id,
                self.fire_formula_id,
                self.litg_formula_id,
                self.holy_formula_id,
                self.scaling_config)

def GetWeaponInfo(name, affinity=None):
    if affinity:
        key = '{} {}'.format(affinity, name)
    else:
        key = name
    entry = _TABLE[key]
    return WeaponInfo(key, entry)

if __name__ == "__main__":
    print(GetWeaponInfo('Arbalest'))
