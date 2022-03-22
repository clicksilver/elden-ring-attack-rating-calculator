"""
Maps the Scaling ID value to the Scaling Config

The scaling ID is a lookup value from the weapon parameters.
The scaling config decides whether a stat improves a damage type.
"""

VERBOSE = False

def init_table():
    with open('data/AttackElementCorrectParam.csv') as f:
        lines = f.readlines();
        for i in range(len(lines)-1):
            line = lines[i+1]
            tokens = line.split(',')
            scaling_id = int(tokens[0])
            scaling_config = [int(elem) for elem in tokens[1:]]
            _TABLE[scaling_id] = scaling_config
    return

_TABLE = {}
init_table()

def convertToBool(val):
    return val == 1

class StatConfig:
    def __init__(self, values):
        self.stre = convertToBool(values[0])
        self.dext = convertToBool(values[1])
        self.inte = convertToBool(values[2])
        self.fait = convertToBool(values[3])
        self.arca = convertToBool(values[4])

    def __str__(self):
        return '{:<5} {:<5} {:<5} {:<5} {:<5}'.format(self.stre, self.dext, self.inte, self.fait, self.arca)

class ScalingConfig:
    def __init__(self, values):
        self.phys = StatConfig(values[ 0: 5])
        self.magi = StatConfig(values[ 5:10])
        self.fire = StatConfig(values[10:15])
        self.litg = StatConfig(values[15:20])
        self.holy = StatConfig(values[20:25])

    def __str__(self):
        return ('{:4}: {:5} {:5} {:5} {:5} {:5}\n' +
                'PHYS: {}\n' +
                'MAGI: {}\n' +
                'FIRE: {}\n' +
                'LITG: {}\n' +
                'HOLY: {}').format('TYPE', 'STR', 'DEX', 'INT', 'FAI', 'ARC',
                        str(self.phys), str(self.magi), str(self.fire),
                        str(self.litg), str(self.holy))


def GetScalingConfig(scaling_id):
    entry = _TABLE[scaling_id]
    cfg = ScalingConfig(entry)
    return cfg


if __name__ == "__main__":
    cfg = GetScalingConfig(20030)
    print(cfg)
