# Mob Hunting Rewards

A minecraft datapack that tracks and rewards mob kills.

## Features

- keep track of killed mobs
- receive advancements and rewards for killed mobs
- every player can view their own score with  
  `/trigger mob_score`
- admins can enable scoreboard with  
  `/scoreboard objectives setdisplay sidebar mhr_score_total`
- completely reset and uninstall with  
  `/function mhr:_remove`

## Installation

1. Download the latest datapack file _mob-hunting-rewards.zip_ from the [releases](https://github.com/lukasstorck/mob-hunting-rewards/releases).
2. Find the datapack folder of a world save.
3. Copy the zip file into the datapack folder.
4. run `/reload`

## Uninstall

1. run `/function mhr:_remove` while the datapack is still loaded (this will remove all modification to the world save)
2. disable datapack or delete from datapack folder

## Configuration

The datapack can be used as is or reconfigured via the [python script](./generate_files.py) and the [config file](./config.json). Following configurations can be made:

- mobs that belong to the same tier
- rewards per tier, that are granted on each first kill of a mob of that tier
- tier icon, title and description, as well as the score points awarded
- title and description patterns of advancements

### Generate files

It is not necessary to generate any files.
The .zip files under releases already come with the default configuration and all files already generated.
If you want to run a custom configuration, you can

1. navigate to the root directory of the repository
2. run the [python script](./generate_files.py) with `python generate_files.py`
3. create the zipped datapack with `zip mob-hunting-rewards.zip -r data/ pack.mcmeta` (or equivalent tools or commands based on your OS)
4. possibly copy the created .zip file to another location as there are known issues when importing the datapack directly from the git repository

## Known issues

Generating and importing (drag & drop) from the git repository folder directly into Minecraft sometimes fails with "Non-pack entries: The following entries were not valid packs and were not copied: mob-hunting-rewards.zip". This can be worked around by copying the zip-file to another location outside the git repository and loading it from there instead.
