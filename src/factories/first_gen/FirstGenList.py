from src.base.BaseUnit import BaseUnit
from src.abstract.AbstractUnitFactory import AbstractUnitFactory
from src.config import mag_hp, mag_base_attack_power, priest_hp, priest_base_attack_power, archer_hp, \
    archer_base_attack_power, warrior_hp, warrior_base_attack_power, knight_hp, knight_base_attack_power, druid_hp, \
    druid_base_attack_power

# Todo codestyle
mag = AbstractUnitFactory(
    lambda team_id: BaseUnit(team_id, hp=mag_hp, base_attack_power=mag_base_attack_power, name="mag", ),
    unit_type="ranged")

priest = AbstractUnitFactory(
    lambda team_id: BaseUnit(team_id, hp=priest_hp, base_attack_power=priest_base_attack_power, name="priest"),
    unit_type="ranged")

archer = AbstractUnitFactory(
    lambda team_id:
    BaseUnit(team_id,
             hp=archer_hp,
             base_attack_power=archer_base_attack_power,
             name="archer"),
    unit_type="ranged")

warrior = AbstractUnitFactory(
    lambda team_id:
    BaseUnit(team_id,
             hp=warrior_hp,
             base_attack_power=warrior_base_attack_power,
             name="warrior"),
    unit_type="melee")

knight = AbstractUnitFactory(
    lambda team_id:
    BaseUnit(team_id,
             hp=knight_hp,
             base_attack_power=knight_base_attack_power,
             name="knight"),
    unit_type="melee")

druid = AbstractUnitFactory(
    lambda team_id: BaseUnit(team_id, hp=druid_hp, base_attack_power=druid_base_attack_power, name="druid"),
    unit_type="melee")

melee_first_gen = [warrior, knight, druid]
ranged_first_gen = [mag, priest, archer]

all_first_gen = [*melee_first_gen, *ranged_first_gen]
