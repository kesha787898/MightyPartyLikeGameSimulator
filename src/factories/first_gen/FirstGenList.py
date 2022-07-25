from src.abstract.AbstractUnitFactory import AbstractUnitFactory
from src.base.BaseUnit import RangedUnit, MeleeUnit
from src.config import mag_hp, mag_base_attack_power, priest_hp, priest_base_attack_power, archer_hp, \
    archer_base_attack_power, warrior_hp, warrior_base_attack_power, knight_hp, knight_base_attack_power, druid_hp, \
    druid_base_attack_power

mag = AbstractUnitFactory(
    lambda team_id: RangedUnit(team_id, hp=mag_hp, base_attack_power=mag_base_attack_power, name="mag"))

priest = AbstractUnitFactory(
    lambda team_id: RangedUnit(team_id, hp=priest_hp, base_attack_power=priest_base_attack_power, name="priest"))

archer = AbstractUnitFactory(
    lambda team_id: RangedUnit(team_id, hp=archer_hp, base_attack_power=archer_base_attack_power, name="archer"))

warrior = AbstractUnitFactory(
    lambda team_id: MeleeUnit(team_id, hp=warrior_hp, base_attack_power=warrior_base_attack_power, name="warrior"))

knight = AbstractUnitFactory(
    lambda team_id: MeleeUnit(team_id, hp=knight_hp, base_attack_power=knight_base_attack_power, name="knight"))

druid = AbstractUnitFactory(
    lambda team_id: MeleeUnit(team_id, hp=druid_hp, base_attack_power=druid_base_attack_power, name="druid"))

melee_first_gen = [warrior, knight, druid]
ranged_first_gen = [mag, priest, archer]

all_first_gen = [*melee_first_gen, *ranged_first_gen]
