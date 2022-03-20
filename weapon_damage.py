"""
inputs to figure out weapon parameters

NAME weapon name
AFFI weapon affinity (none, heavy, keen, etc.)
UPLV upgrade level (0-10 or 0-25)

NAME and AFFI decide whether each of the Damage Types scales off of the
Offensive Stats:

Damage Types:
    Physical
    Magic
    Fire
    Lightning
    Holy

Offensive Stats:
    Strength
    Dexterity
    Intelligence
    Faith
    Arcane

ScalingType: 5x5 binary value Matrix

        Stre    Dext    Inte    Fait    Arca
Phys    -       -       -       -       -
Magi    -       -       -       -       -
Fire    -       -       -       -       -
Ligh    -       -       -       -       -
Holy    -       -       -       -       -

"""
import stats

import lookup_weapon_name_affinity_upgrade_base_rating as war
import lookup_scaling_id_to_config as sc
import lookup_weapon_name_affinity_upgrade_stat_scaling_factor as ssf
import lookup_weapon_name_affinity_formula_type as ft
import weapon_formulas as wf

import math

class WeaponDamage:
    def __init__(self, phys_ar, phys_dmg, magi_ar, magi_dmg, fire_ar, fire_dmg,
                 litg_ar, litg_dmg, holy_ar, holy_dmg):
        self.phys_ar = phys_ar
        self.magi_ar = magi_ar
        self.fire_ar = fire_ar
        self.litg_ar = litg_ar
        self.holy_ar = holy_ar
        self.phys_dmg = phys_dmg
        self.magi_dmg = magi_dmg
        self.fire_dmg = fire_dmg
        self.litg_dmg = litg_dmg
        self.holy_dmg = holy_dmg
        
    def __str__(self):
        return '{}+{} / {}+{} / {}+{} / {}+{} / {}+{}'.format(
                         self.phys_ar, self.phys_dmg,
                         self.magi_ar, self.magi_dmg,
                         self.fire_ar, self.fire_dmg,
                         self.litg_ar, self.litg_dmg,
                         self.holy_ar, self.holy_dmg)

def ComputeWeaponParams(name, affinity, level, stats):
    # base attack ratings for each damage type
    wep_ar = war.GetWeaponAttackRatings(name, affinity, level)
    
    # tuple of formula IDs by damage type, and scaling IDs
    wep_info = ft.GetWeaponInfo(name, affinity)
    wisc = wep_info.scaling_config

    # tuple of factors affecting stat scaling per stat
    wep_scale_fac = ssf.GetWeaponScalingFactors(name, affinity, level)

    phys_ar = wep_ar.phys_rating
    magi_ar = wep_ar.magi_rating
    fire_ar = wep_ar.fire_rating
    litg_ar = wep_ar.litg_rating
    holy_ar = wep_ar.holy_rating

    stre_fac = wep_scale_fac.stre_factor
    dext_fac = wep_scale_fac.dext_factor
    inte_fac = wep_scale_fac.inte_factor
    fait_fac = wep_scale_fac.fait_factor
    arca_fac = wep_scale_fac.arca_factor

    # phys
    phys_fid = wep_info.phys_formula_id
    phys_stre_fac = wisc.phys.stre * wf.GetCorrectionFactor(stats.stre, phys_fid)
    phys_dext_fac = wisc.phys.dext * wf.GetCorrectionFactor(stats.dext, phys_fid)
    phys_inte_fac = wisc.phys.inte * wf.GetCorrectionFactor(stats.inte, phys_fid)
    phys_fait_fac = wisc.phys.fait * wf.GetCorrectionFactor(stats.fait, phys_fid)
    phys_arca_fac = wisc.phys.arca * wf.GetCorrectionFactor(stats.arca, phys_fid)
    phys_stre_dmg = phys_ar * stre_fac * phys_stre_fac / 100
    phys_dext_dmg = phys_ar * dext_fac * phys_dext_fac / 100
    phys_inte_dmg = phys_ar * inte_fac * phys_inte_fac / 100
    phys_fait_dmg = phys_ar * fait_fac * phys_fait_fac / 100
    phys_arca_dmg = phys_ar * arca_fac * phys_arca_fac / 100
    phys_damage = phys_stre_dmg + phys_dext_dmg + phys_inte_dmg + phys_fait_dmg + phys_arca_dmg

    # magi
    magi_fid = wep_info.magi_formula_id
    magi_stre_fac = wisc.magi.stre * wf.GetCorrectionFactor(stats.stre, magi_fid)
    magi_dext_fac = wisc.magi.dext * wf.GetCorrectionFactor(stats.dext, magi_fid)
    magi_inte_fac = wisc.magi.inte * wf.GetCorrectionFactor(stats.inte, magi_fid)
    magi_fait_fac = wisc.magi.fait * wf.GetCorrectionFactor(stats.fait, magi_fid)
    magi_arca_fac = wisc.magi.arca * wf.GetCorrectionFactor(stats.arca, magi_fid)
    magi_stre_dmg = magi_ar * stre_fac * magi_stre_fac / 100
    magi_dext_dmg = magi_ar * dext_fac * magi_dext_fac / 100
    magi_inte_dmg = magi_ar * inte_fac * magi_inte_fac / 100
    magi_fait_dmg = magi_ar * fait_fac * magi_fait_fac / 100
    magi_arca_dmg = magi_ar * arca_fac * magi_arca_fac / 100
    magi_damage = magi_stre_dmg + magi_dext_dmg + magi_inte_dmg + magi_fait_dmg + magi_arca_dmg

    # fire
    fire_fid = wep_info.fire_formula_id
    fire_stre_fac = wisc.fire.stre * wf.GetCorrectionFactor(stats.stre, fire_fid)
    fire_dext_fac = wisc.fire.dext * wf.GetCorrectionFactor(stats.dext, fire_fid)
    fire_inte_fac = wisc.fire.inte * wf.GetCorrectionFactor(stats.inte, fire_fid)
    fire_fait_fac = wisc.fire.fait * wf.GetCorrectionFactor(stats.fait, fire_fid)
    fire_arca_fac = wisc.fire.arca * wf.GetCorrectionFactor(stats.arca, fire_fid)
    fire_stre_dmg = fire_ar * stre_fac * fire_stre_fac / 100
    fire_dext_dmg = fire_ar * dext_fac * fire_dext_fac / 100
    fire_inte_dmg = fire_ar * inte_fac * fire_inte_fac / 100
    fire_fait_dmg = fire_ar * fait_fac * fire_fait_fac / 100
    fire_arca_dmg = fire_ar * arca_fac * fire_arca_fac / 100
    fire_damage = fire_stre_dmg + fire_dext_dmg + fire_inte_dmg + fire_fait_dmg + fire_arca_dmg

    # litg
    litg_fid = wep_info.litg_formula_id
    litg_stre_fac = wisc.litg.stre * wf.GetCorrectionFactor(stats.stre, litg_fid)
    litg_dext_fac = wisc.litg.dext * wf.GetCorrectionFactor(stats.dext, litg_fid)
    litg_inte_fac = wisc.litg.inte * wf.GetCorrectionFactor(stats.inte, litg_fid)
    litg_fait_fac = wisc.litg.fait * wf.GetCorrectionFactor(stats.fait, litg_fid)
    litg_arca_fac = wisc.litg.arca * wf.GetCorrectionFactor(stats.arca, litg_fid)
    litg_stre_dmg = litg_ar * stre_fac * litg_stre_fac / 100
    litg_dext_dmg = litg_ar * dext_fac * litg_dext_fac / 100
    litg_inte_dmg = litg_ar * inte_fac * litg_inte_fac / 100
    litg_fait_dmg = litg_ar * fait_fac * litg_fait_fac / 100
    litg_arca_dmg = litg_ar * arca_fac * litg_arca_fac / 100
    litg_damage = litg_stre_dmg + litg_dext_dmg + litg_inte_dmg + litg_fait_dmg + litg_arca_dmg

    # holy
    holy_fid = wep_info.holy_formula_id
    holy_stre_fac = wisc.holy.stre * wf.GetCorrectionFactor(stats.stre, holy_fid)
    holy_dext_fac = wisc.holy.dext * wf.GetCorrectionFactor(stats.dext, holy_fid)
    holy_inte_fac = wisc.holy.inte * wf.GetCorrectionFactor(stats.inte, holy_fid)
    holy_fait_fac = wisc.holy.fait * wf.GetCorrectionFactor(stats.fait, holy_fid)
    holy_arca_fac = wisc.holy.arca * wf.GetCorrectionFactor(stats.arca, holy_fid)
    holy_stre_dmg = holy_ar * stre_fac * holy_stre_fac / 100
    holy_dext_dmg = holy_ar * dext_fac * holy_dext_fac / 100
    holy_inte_dmg = holy_ar * inte_fac * holy_inte_fac / 100
    holy_fait_dmg = holy_ar * fait_fac * holy_fait_fac / 100
    holy_arca_dmg = holy_ar * arca_fac * holy_arca_fac / 100
    holy_damage = holy_stre_dmg + holy_dext_dmg + holy_inte_dmg + holy_fait_dmg + holy_arca_dmg

    return WeaponDamage(math.trunc(phys_ar), math.floor(phys_damage),
                        math.trunc(magi_ar), math.floor(magi_damage),
                        math.trunc(fire_ar), math.floor(fire_damage),
                        math.trunc(litg_ar), math.floor(litg_damage),
                        math.trunc(holy_ar), math.floor(holy_damage))

if __name__ == "__main__":
    stats = stats.Stats(32, 22, 9, 27, 9)
    print(ComputeWeaponParams('Cross-Naginata', 'Flame Art', 12, stats))
