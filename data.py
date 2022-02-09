import sys
import types

sys_arg = False

try:
    modules = sys.argv[1].split('|')
    sys_arg = True
except IndexError:
    modules = []


def checker(depends):
    for item in depends:
        if isinstance(item, types.FunctionType):
            try:
                if not item()[0]:
                    return False, item()[1]
            except RecursionError:
                return False, f"There's a circular dependency for {item}'"
        elif item not in modules and type(item) == str:
            return False, item
    return [True]


# Tier 1
assassin = ['Deadeye', 'Vampiric']
corrupter = ['Bloodletter', 'Chaosweaver']
drought_bringer = ['Malediction', 'Deadeye']
entangler = ['Toxic', 'Bloodletter']
evocationist = ['Flameweaver', 'Frostweaver', 'Stormweaver']
executioner = ['Frenzied', 'Berserker']
flame_strider = ['Flameweaver', 'Hasted']
frost_strider = ['Frostweaver', 'Hasted']
heralding_minions = ['Dynamo', 'Arcane Buffer']
hexer = ['Chaosweaver', 'Corrupter']
ice_prison = ['Permafrost', 'Sentinel']
invulnerable = ['Sentinel', 'Juggernaut', 'Consecrator']
magma_barrier = ['Incendiary', 'Bonebreaker']
mana_siphoner = ['Consecrator', 'Dynamo']
mirror_image = ['Echoist', 'Soul Conduit']
necromancer = ['Bombardier', 'Overcharged']
rejuvenating = ['Gargantuan', 'Vampiric']
storm_strider = ['Stormweaver', 'Hasted']
treant_horde = ['Toxic', 'Sentinel', 'Steel-infused']


# Tier 2
abberath_touched = ['Flame Strider', lambda: checker(flame_strider), 'Frenzied', 'Rejuvenating', lambda: checker(rejuvenating)]
brine_king_touched = ['Ice Prison', lambda: checker(ice_prison), 'Storm Strider', lambda: checker(storm_strider), 'Heralding Minions', lambda: checker(heralding_minions)]
corpse_detonator = ['Necromancer', lambda: checker(necromancer), 'Incendiary']
crystal_skinned = ['Permafrost', 'Rejuvenating', lambda: checker(rejuvenating), 'Berserker']
effigy = ['Hexer', lambda: checker(hexer), 'Malediction', 'Corrupter', lambda: checker(corrupter)]
empowered_elements = ['Evocationist', lambda: checker(evocationist), 'Steel-infused', 'Chaosweaver']
empowering_minions = ['Necromancer', lambda: checker(necromancer), 'Executioner', lambda: checker(executioner), 'Gargantuan']
soul_eater = ['Soul Conduit', 'Necromancer', lambda: checker(necromancer), 'Gargantuan']
temporal_bubble = ['Juggernaut', 'Hexer', lambda: checker(hexer), 'Arcane Buffer']
trickster = ['Overcharged', 'Assassin', lambda: checker(assassin), 'Echoist']
tukohama_touched = ['Bonebreaker', 'Executioner', lambda: checker(executioner), 'Magma Barrier', lambda: checker(magma_barrier)]

# Tier 3
arakaali_touched = ['Corpse Detonator', lambda: checker(corpse_detonator), 'Entangler', lambda: checker(entangler), 'Assassin', lambda: checker(assassin)]
kitava_touched = ['Abberath-touched', lambda: checker(abberath_touched), 'Corrupter', lambda: checker(corrupter), 'Tukohama-touched', lambda: checker(tukohama_touched), 'Corpse Detonator', lambda: checker(corpse_detonator)]
lunaris_touched = ['Invulnerable', lambda: checker(invulnerable), 'Frost Strider', lambda: checker(frost_strider), 'Empowering Minions', lambda: checker(empowering_minions)]
shakari_touched = ['Entangler', lambda: checker(entangler), 'Soul Eater', lambda: checker(entangler), 'Drought Bringer', lambda: checker(drought_bringer)]
solaris_touched = ['Invulnerable', lambda: checker(invulnerable), 'Magma Barrier', lambda: checker(magma_barrier), 'Empowering Minions', lambda: checker(empowering_minions)]

# Tier 4
innocence_touched = ['Lunaris-touched', lambda: checker(lunaris_touched), 'Solaris-touched', lambda: checker(solaris_touched), 'Mirror Image', lambda: checker(mirror_image), 'Mana Siphoner', lambda: checker(mana_siphoner)]

# All ingredients (Except ones that don't appear in a recipe such as Innocence-touched or Effigy)
all_items = ['Abberath-touched',
             'Arcane Buffer',
             'Assassin',
             'Berserker',
             'Bloodletter',
             'Bombardier',
             'Bonebreaker',
             'Chaosweaver',
             'Consecrator',
             'Corpse Detonator',
             'Corrupter',
             'Deadeye',
             'Drought Bringer',
             'Dynamo',
             'Echoist',
             'Empowering Minions',
             'Entangler',
             'Evocationist',
             'Executioner',
             'Flame Strider',
             'Flameweaver',
             'Frenzied',
             'Frost Strider',
             'Frostweaver',
             'Gargantuan',
             'Hasted',
             'Heralding Minions',
             'Hexer',
             'Ice Prison',
             'Incendiary',
             'Invulnerable',
             'Juggernaut',
             'Lunaris-touched',
             'Magma Barrier',
             'Malediction',
             'Mana Siphoner',
             'Mirror Image',
             'Necromancer',
             'Opulent',
             'Overcharged',
             'Permafrost',
             'Rejuvenating',
             'Sentinel',
             'Solaris-touched',
             'Soul Conduit',
             'Soul Eater',
             'Steel-infused',
             'Storm Strider',
             'Stormweaver',
             'Toxic',
             'Tukohama-touched',
             'Vampiric']

# All items that require ingredients (or craftables)
all_craft_names = ['Heralding Minions',
                   'Empowering Minions',
                   'Assassin',
                   'Trickster',
                   'Necromancer',
                   'Rejuvenating',
                   'Executioner',
                   'Hexer',
                   'Drought Bringer',
                   'Entangler',
                   'Temporal Bubble',
                   'Treant Horde',
                   'Frost Strider',
                   'Ice Prison',
                   'Soul Eater',
                   'Flame Strider',
                   'Corpse Detonator',
                   'Evocationist',
                   'Magma Barrier',
                   'Mirror Image',
                   'Storm Strider',
                   'Mana Siphoner',
                   'Corrupter',
                   'Invulnerable',
                   'Crystal-skinned',
                   'Empowered Elements',
                   'Effigy',
                   'Lunaris-touched',
                   'Solaris-touched',
                   'Arakaali-touched',
                   'Brine King-touched',
                   'Tukohama-touched',
                   'Abberath-touched',
                   'Shakari-touched',
                   'Innocence-touched',
                   'Kitava-touched']

all_crafts = [heralding_minions,
              empowering_minions,
              assassin,
              trickster,
              necromancer,
              rejuvenating,
              executioner,
              hexer,
              drought_bringer,
              entangler,
              temporal_bubble,
              treant_horde,
              frost_strider,
              ice_prison,
              soul_eater,
              flame_strider,
              corpse_detonator,
              evocationist,
              magma_barrier,
              mirror_image,
              storm_strider,
              mana_siphoner,
              corrupter,
              invulnerable,
              crystal_skinned,
              empowered_elements,
              effigy,
              lunaris_touched,
              solaris_touched,
              arakaali_touched,
              brine_king_touched,
              tukohama_touched,
              abberath_touched,
              shakari_touched,
              innocence_touched,
              kitava_touched]
