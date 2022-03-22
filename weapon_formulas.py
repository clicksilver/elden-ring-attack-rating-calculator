"""
Fairly complicated system to compute the weapon's specific "correction factor"
for each Damage-Stat pair:
    Phys-Str
    Phys-Dex
    ...
    Magi-Int
    ...
    Holy-Fai
    Holy-Arc

That's 25 different pairs, each with its own unique correction factor.

The formulas are based on the Formula ID which an integer from
    {0, 1, 2, 4, 7, 8, 12, 14, 15, 16}

Each stat then determines the specific sub-formula based on the range:
    A: usually >80
    B: usually >60
    C: usually >20
    D: everything else

The limits vary based on the Formula ID.

Each factor is calculated with:
    - the Formula ID as input
    - the Subtype based on the Stat Value
Which is then computed using the correct formula and coefficients
"""

import sys

VERBOSE = False

def formula_0A(stat, limit, coeffs):
    return coeffs[0] + (coeffs[1] * (stat-limit) / coeffs[2])

def formula_0C(stat, limit, coeffs):
    return coeffs[0] + (coeffs[1] * (1-pow(1-((stat-limit)/coeffs[2]), coeffs[3])))

def formula_0D(stat, limit, coeffs):
    return coeffs[0] * pow((stat-1)/coeffs[1], coeffs[2])

def formula_4D(stat, limit, coeffs):
    return coeffs[0] * (stat - 1) / coeffs[1]

# If a formula is tagged as "original", then this the first time it is defined
# in the context of this map. Otherwise it is reusing a previously defined
# formula.
formula_map = {
    '0A': 'formula_0A', # original
    '0B': 'formula_0A',
    '0C': 'formula_0C', # original
    '0D': 'formula_0D', # original

    '1A': 'formula_0A',
    '1B': 'formula_0A',
    '1C': 'formula_0C',
    '1D': 'formula_0D',

    '2A': 'formula_0A',
    '2B': 'formula_0A',
    '2C': 'formula_0C',
    '2D': 'formula_0D',

    '4A': 'formula_0A',
    '4B': 'formula_0A',
    '4C': 'formula_0A',
    '4D': 'formula_4D', # original

    '7A': 'formula_0A',
    '7B': 'formula_0A',
    '7C': 'formula_0C',
    '7D': 'formula_0D',

    '8A': 'formula_0A',
    '8B': 'formula_0A',
    '8C': 'formula_0C',
    '8D': 'formula_0D',

    '12A': 'formula_0A',
    '12B': 'formula_0A',
    '12C': 'formula_0A',
    '12D': 'formula_4D',

    '14A': 'formula_0A',
    '14B': 'formula_0A',
    '14C': 'formula_0A',
    '14D': 'formula_4D',

    '15A': 'formula_0A',
    '15B': 'formula_0A',
    '15C': 'formula_0A',
    '15D': 'formula_4D',

    '16A': 'formula_0A',
    '16B': 'formula_0A',
    '16C': 'formula_0A',
    '16D': 'formula_4D',
}

# This maps FormulaID to Tuples which consist of:
# - LIMIT: minimum value of the stat to which this coefficient set is used
# - COEFFS: any-sized list of coefficient values to use with the corresponding
#           formula
coeff_map = {
    '0A': (80, [90, 20, 70]),
    '0B': (60, [75, 15, 20]),
    '0C': (18, [25, 50, 42, 1.2]),
    '0D': ( 0, [25, 17, 1.2]),

    '1A': (80, [90, 20, 70]),
    '1B': (60, [75, 15, 20]),
    '1C': (20, [35, 40, 40, 1.2]),
    '1D': ( 0, [35, 19, 1.2]),

    '2A': (80, [90, 20, 70]),
    '2B': (60, [75, 15, 20]),
    '2C': (20, [35, 40, 40, 1.2]),
    '2D': ( 0, [35, 19, 1.2]),

    '4A': (80, [95, 5, 19]),
    '4B': (50, [80, 15, 30]),
    '4C': (20, [40, 40, 30]),
    '4D': ( 0, [40, 19]),

    '7A': (80, [90, 20, 70]),
    '7B': (60, [75, 15, 20]),
    '7C': (20, [35, 40, 40, 1.2]),
    '7D': ( 0, [35, 19, 1.2]),

    '8A': (80, [90, 20, 70]),
    '8B': (60, [75, 15, 20]),
    '8C': (16, [25, 50, 44, 1.2]),
    '8D': ( 0, [25, 15, 1.2]),

    '12A': (45, [75, 25, 54]),
    '12B': (30, [55, 20, 15]),
    '12C': (15, [10, 45, 15]),
    '12D': ( 0, [10, 14]),

    '14A': (80, [85, 15, 19]),
    '14B': (40, [60, 25, 40]),
    '14C': (20, [40, 20, 20]),
    '14D': ( 0, [40, 19]),

    '15A': (80, [95,  5, 19]),
    '15B': (60, [65, 30, 20]),
    '15C': (25, [25, 40, 35]),
    '15D': ( 0, [25, 24]),

    '16A': (80, [90, 10, 19]),
    '16B': (60, [75, 15, 20]),
    '16C': (18, [20, 55, 42]),
    '16D': ( 0, [20, 17]),
}

def GetCorrectionFactor(stat, formula_id):
    for subtype in ['A', 'B', 'C', 'D']:
        full_type = str(formula_id) + subtype
        config = coeff_map[full_type]
        limit = config[0]
        coeffs = config[1]
        if stat > limit:
            if VERBOSE:
                print('Using formula {}'.format(full_type))
                print('Using limit {}'.format(limit))
                print('Using coeffs {}'.format(coeffs))
            method = getattr(sys.modules[__name__], formula_map[full_type])
            return method(stat, limit, coeffs)

if __name__ == "__main__":
    VERBOSE = True
    print(GetCorrectionFactor(32, 0))
