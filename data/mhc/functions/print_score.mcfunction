execute as @a run scoreboard players operation @s mhr_score_total = @s mhr_score_total
tellraw @s [{"text": "Mob Hunting Score: "}, {"score":{"name":"@s","objective":"mhr_score_total"},"bold":true}]
