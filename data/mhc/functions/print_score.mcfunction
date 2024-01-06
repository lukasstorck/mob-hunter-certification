execute as @a run scoreboard players operation @s mhc_score_total = @s mhc_score_total
tellraw @s [{"text": "Personal Mob Hunter Certification Score: "}, {"score":{"name":"@s","objective":"mhc_score_total"},"bold":true}]
