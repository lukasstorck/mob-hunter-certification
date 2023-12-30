execute as @a run scoreboard players operation @s mob_slayer_score_total = @s mob_slayer_score_total
tellraw @s [{"text": "Personal Mob Slayer Score: "}, {"score":{"name":"@s","objective":"mob_slayer_score_total"},"bold":true}]
