scoreboard players enable @a mob_score
execute as @a if score @s mob_score matches 1.. run function mhc:print_score
execute as @a if score @s mob_score matches 1.. run scoreboard players reset @s mob_score
