import math


def look_for_gold(player, gold):
    distance = math.sqrt((player.x - gold.x) ** 2 + (player.y - gold.y) ** 2)

    if distance < gold.capture_radius:
        player.take_gold(gold)
