max_colors = {"red": 12, "green": 13, "blue": 14}
valids = 0
tot_power = 0
with open("aoc2-data.txt") as f:
    for l in f.readlines():
        l = l.strip()
        print(l)

# ## PART 1
#         draws = l.split(":")[1].split(";")
#         is_valid = True
#         for d in draws:
#             colors = d.strip().split(",")
#             for c in colors:
#                 color = c.strip().split(" ")[1]
#                 nb_color = c.strip().split(" ")[0]
#                 if max_colors[color] < int(nb_color):
#                     is_valid = False
#                     break
#             if not is_valid:
#                 break
#         if is_valid:
#             valids+=id
# 
#     print("part1", valids)

## PART 2
        temp_colors = {"red":0, "green":0, "blue":0}
        draws = l.split(":")[1].split(";")
        for d in draws:
            colors = d.strip().split(",")
            for c in colors:
                color = c.strip().split(" ")[1]
                nb_color = int(c.strip().split(" ")[0])
                if temp_colors[color] < nb_color:
                    temp_colors[color] = nb_color

        game_power = 1
        for v in temp_colors.values():
            game_power *= v

        tot_power += game_power

print("part2", tot_power)
