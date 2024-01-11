import json
import pathlib

config_path = pathlib.Path('config.json')
config = json.load(config_path.open())


def capitalize_all(x: str):
    return ' '.join(map(lambda s: s.capitalize(), x.split()))


def generate_point_functions():
    path_functions = pathlib.Path('data/mhr/functions')
    for old_file in path_functions.glob('add_*.mcfunction'):
        old_file.unlink()

    for tier in config['tiers']:
        function_name = f'add_{tier["points"]}_point{"" if tier["points"] == 1 else "s"}'
        function = f'scoreboard players add @s mhr_score_total {tier["points"]}'
        pathlib.Path(path_functions /
                     f'{function_name}.mcfunction').open('w+').write(function)


def generate_loot_tables():
    path_loot_tables = pathlib.Path('data/mhr/loot_tables')
    for old_file in path_loot_tables.glob('reward_*.json'):
        old_file.unlink()

    for tier in config['tiers']:
        loot_table_name = f'reward_{tier["name"]}'
        data = {
            'type': 'minecraft:advancement_reward',
            'pools': [
                {
                    'rolls': reward['amount'],
                    'entries': [
                        {
                            'type': 'minecraft:item',
                            'name': reward['item_name'],
                            **({'functions': [
                                {
                                    'function': 'minecraft:set_potion',
                                    'id': reward['potion_id']
                                }
                            ]} if 'potion_id' in reward else {})
                        }
                    ]
                } for reward in tier['rewards']
            ]
        }
        json.dump(data, pathlib.Path(path_loot_tables /
                  f'{loot_table_name}.json').open('w+'))


def generate_mob_advancements():
    path_advancements = pathlib.Path('data/mhr/advancements/mhr')
    for old_file in path_advancements.glob('killed_*.json'):
        old_file.unlink()

    for tier in config['tiers']:
        mobs: list[str] = tier['mobs']
        tier_name: str = tier['name']
        parent = f'tier_{tier_name}'
        for mob in mobs:
            title = config['advancement_title'].replace(
                '<mob>', capitalize_all(mob.replace('_', ' ')))
            description = config['advancement_description'].replace(
                '<mob>', mob.replace('_', ' '))
            point_function_name = f'mhr:add_{tier["points"]}_point{"" if tier["points"] == 1 else "s"}'
            data = {
                'display': {
                    'icon': {
                        'item': 'minecraft:player_head' if mob == 'player' else f'minecraft:{mob}_spawn_egg',
                    },
                    'title': title,
                    'description': description,
                },
                'parent': f'mhr:mhr/{parent}',
                'criteria': {
                    f'killed_{mob}': {
                        'trigger': 'minecraft:player_killed_entity',
                        'conditions': {
                            'entity': {
                                'type': f'minecraft:{mob}'
                            }
                        }
                    }
                },
                'rewards': {
                    'function': point_function_name,
                    'loot': [f'mhr:reward_{tier_name}']
                }
            }
            file_name = f'killed_{mob}.json'
            parent = file_name[:-5]
            json.dump(data, pathlib.Path(
                path_advancements / file_name).open('w+'))
        
        # after all mobs add the tier advancement again as a kind of label and to reveal every advancment in between
        generate_tier_advancement(
            path_advancements,
            tier['name'] + '_end',
            tier['tier_icon'],
            tier['title'],
            tier['description'],
            parent
        )


def generate_tier_advancement(path: str, name: str, icon: str, title: str, description: str, parent: str):
    data = {
        'display': {
            'icon': {
                'item': f'minecraft:{icon}',
            },
            'title': title,
            'description': description,
            'show_toast': False,
            'announce_to_chat': False,
        },
        'parent': f'mhr:mhr/{parent}',
        'criteria': {
            'true': {
                'trigger': 'minecraft:tick'
            }
        },
    }
    json.dump(data, pathlib.Path(path / f'tier_{name}.json').open('w+'))


def generate_tier_advancements():
    path_advancements = pathlib.Path('data/mhr/advancements/mhr')
    for old_file in path_advancements.glob('tier_*.json'):
        old_file.unlink()

    parent = 'root'

    for tier in config['tiers']:
        generate_tier_advancement(
            path_advancements,
            tier['name'],
            tier['tier_icon'],
            tier['title'],
            tier['description'],
            parent
        )


if __name__ == '__main__':
    generate_loot_tables()
    generate_point_functions()
    generate_tier_advancements()
    generate_mob_advancements()
