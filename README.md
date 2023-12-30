# Mob Slayer
A minecraft datapack that tracks and rewards mob kills.

## Features
* keep track of killed mobs
* receive rewards for killed mobs
* every player can view their own score with  
  `/trigger mob_score`
* admins can enable scoreboard with  
  `/scoreboard objectives setdisplay sidebar mob_slayer_score_total`
* completely reset and uninstall with  
  `/function mob_slayer:_remove`

## Configuration
The datapack can be used as is or reconfigured via the [python script](./generate_files.py) and the [config file](./config.json). Following configurations can be made:
* mobs that belong to the same tier
* rewards per tier, that are granted on each first kill of a mob of that tier
* tier icon, title and description, as well as the score points awarded
* title and description patterns of advancements
