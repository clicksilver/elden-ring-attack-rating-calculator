# elden-ring-attack-rating-calculator
A python script to calculate the weapon attack ratings based on your stats, upgrade levels, and affinity for any weapon

# Usage

```
python main.py --name "NAME"
               [--affinity "AFFINITY"]
               UPGRADE
               STRENGTH
               DEXTERITY
               INTELLIGENCE
               FAITH
               ARCANE
```

```
python main.py --name "Dagger" --affinity "Flame Art" 10 20 30 10 15 40
```

# Implementation Notes

The code is entirely based off the work from u/TarnishedSpreadsheet which uses game data files to figure out the formulas and coefficients. It makes extensive use of lookup tables as a result.

There are 5 Stats:
* Strength (stre)
* Dexterity (dext)
* Intelligence (inte)
* Faith (fait)
* Arcane (arca)

There are 5 Damage Types:
* Physical
* Magic
* Fire
* Lightning
* Holy

The typical flow is as follows:

1. Choose Stats (allocate strength, dexterity, intelligence, faith and arcane).
2. Choose Weapon Characteristics:
    * Name
    * Affinity (if applicable: Standard, Heavy, Keen, Quality, Magic, Cold, Fire, Lightning, Holy, Blood, Poison, Occult, etc)
    * Upgrade Level (Up to +10 for uniques, or +25 for standard).
3. Using the Name and Affinity, to determine the Weapon Info, for **each** damage type (Phys/Magic/:
    * _Formula Set_ : This is a group of four formulas and coefficients which caclulate a _Scaling Factor_ given a Stat.
    * _Scaling Config_: This is whether a DamageType is scaled by Stat (25 possible pairs, organized in a tuple of booleans)
4. Once we know the Formula Set and Scaling Config, we can apply the formulas and compute the Scaling Factor for each DamageType-Stat pair.
5. Using the Name, Affinity and Upgrade Level we can lookup:
    * _Attack Rating_ for each DamageType
    * _Scaling Rating_ for each Stat
6. Using the _Attack Rating_, _Scaling Rating_, and _Scaling Factor_ (for each Stat) we can compute the final Attack Rating of the weapon.

# To Do

* Refactor `lookup_*.py` scripts for better naming:
  * `lookup_scaling_id_to_config` can be combined with `lookup_weapon_info`
  * Change the names for the lookup table helpers to be less verbose
* Passive Effects like Blood, Frost, Poison, etc
* Sorcery and Incantation Scaling

# Credit

All the formulas and calculation comes from the creators of this spreadsheet:

https://docs.google.com/spreadsheets/d/1JdkVb-llZHPhMD-IwO8d2o1jtHhiTIXbcJv0YzC8ZHY/copy

https://www.reddit.com/r/Eldenring/comments/tbco46/elden_ring_weapon_calculator/i0xlhi1/?context=3

u/TarnishedSpreadsheet
