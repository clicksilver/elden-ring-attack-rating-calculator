"""
Lookup Table for a weapon (name and affinity) to it's Formula IDs for each
damage type, and it's Scaling ID.

Formula ID: IDs for each of the main damage types
            (Phys, Magic, Fire, Lightning, Holy)

Scaling ID: ID which maps to the scaling configuration of the weapon (which
            decides if a weapon's damage-type scales with each stat).
"""
VERBOSE = False

def convertToBool(val):
    return val == 1

class StatScalingConfig:
    def __init__(self, values):
        self.scales_with_stre = convertToBool(values[0])
        self.scales_with_dext = convertToBool(values[1])
        self.scales_with_inte = convertToBool(values[2])
        self.scales_with_fait = convertToBool(values[3])
        self.scales_with_arca = convertToBool(values[4])

    def __str__(self):
        return '{:<5} {:<5} {:<5} {:<5} {:<5}'.format(
                self.scales_with_stre,
                self.scales_with_dext,
                self.scales_with_inte,
                self.scales_with_fait,
                self.scales_with_arca)

class ScalingConfig:
    def __init__(self, values):
        self.phys = StatScalingConfig(values[ 0: 5])
        self.magi = StatScalingConfig(values[ 5:10])
        self.fire = StatScalingConfig(values[10:15])
        self.litg = StatScalingConfig(values[15:20])
        self.holy = StatScalingConfig(values[20:25])

    def __str__(self):
        return ('{:4}: {:5} {:5} {:5} {:5} {:5}\n' +
                'PHYS: {}\n' +
                'MAGI: {}\n' +
                'FIRE: {}\n' +
                'LITG: {}\n' +
                'HOLY: {}').format('TYPE', 'STR', 'DEX', 'INT', 'FAI', 'ARC',
                        str(self.phys), str(self.magi), str(self.fire),
                        str(self.litg), str(self.holy))

class WeaponInfo:
    def __init__(self, name, formula_id_list, scaling_config):
        self.name = name
        self.phys_formula_id = formula_id_list[0]
        self.magi_formula_id = formula_id_list[1]
        self.fire_formula_id = formula_id_list[2]
        self.litg_formula_id = formula_id_list[3]
        self.holy_formula_id = formula_id_list[4]
        self.scaling_config = scaling_config

    def __str__(self):
        return '{}\n{},{},{},{},{}\n{}'.format(self.name,
                self.phys_formula_id,
                self.magi_formula_id,
                self.fire_formula_id,
                self.litg_formula_id,
                self.holy_formula_id,
                self.scaling_config)

def init_table():
    stat_scaling_table = {}
    with open('data/AttackElementCorrectParam.csv') as f:
        lines = f.readlines();
        for i in range(len(lines)-1):
            line = lines[i+1]
            tokens = line.split(',')
            scaling_id = int(tokens[0])
            stat_scaling_config = ScalingConfig([int(elem) for elem in tokens[1:]])
            stat_scaling_table[scaling_id] = stat_scaling_config
    with open('data/CalcCorrectGraph_ID.csv') as f:
        lines = f.readlines();
        for i in range(len(lines)-1):
            line = lines[i+1]
            tokens = line.split(',')
            wep_aff_name = tokens[0]
            values = [int(elem) for elem in tokens[1:]]
            scaling_id = values[-1]
            stat_scaling_config = stat_scaling_table[scaling_id]
            _TABLE[wep_aff_name] = WeaponInfo(wep_aff_name, values, stat_scaling_config)
    return

_TABLE = {}
init_table()

def GetWeaponInfo(name, affinity=None):
    if affinity:
        key = '{} {}'.format(affinity, name)
    else:
        key = name
    return _TABLE[key]

if __name__ == "__main__":
    print(GetWeaponInfo('Bloody Helice'))
