"""
python main.py --name "NAME"
               [--affinity "AFFINITY"]
               UPGRADE
               STRENGTH
               DEXTERITY
               INTELLIGENCE
               FAITH
               ARCANE
"""
import argparse
import stats
import weapon_damage

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--affinity', type=str, default=None)
    parser.add_argument('upgrade', type=int)
    parser.add_argument('strength', type=int)
    parser.add_argument('dexterity', type=int)
    parser.add_argument('intelligence', type=int)
    parser.add_argument('faith', type=int)
    parser.add_argument('arcane', type=int)
    args = parser.parse_args()
    wdmg = weapon_damage.ComputeWeaponParams(args.name, args.affinity,
                                             args.upgrade, 
                                             stats.Stats(args.strength,
                                                         args.dexterity,
                                                         args.intelligence,
                                                         args.faith,
                                                         args.arcane))

    print('{:2}/{:2}/{:2}/{:2}/{:2} {} {} +{} {}'.format(args.strength,
        args.dexterity, args.intelligence, args.faith, args.arcane,
        args.affinity, args.name, args.upgrade, wdmg))

