# Default scheme looks like:
# {<Game Number>: {"color1": <max>, "color2": <max>...}, ...}

games_dict = dict()

with open(file="data/1202.csv") as f:
    lines = f.readlines()
    for line in lines:
        # Insane amount of splitting, intentionally annoying data file
        id_split = line.split(": ")
        game_id = id_split[0].split(" ")[1]
        rounds_dict = dict()

        # Grab each round of the game and loop through, setting the object's max
        for game in id_split[1].split("; "):
            for count in game.split(", "):
                color = count.split(" ")[1]
                num = int(count.split(" ")[0])
                if color in rounds_dict:
                    num = max(num, rounds_dict[color])
                rounds_dict[color] = num
        
        # We should have the maxed out counts from across the rounds, assign them to the game id
        games_dict[game_id] = rounds_dict

# This is the comparison dict, we'll loop and look at possible solutions
total_possible = 0
sd = {"red": 12, "green": 13, "blue": 14}
for gid in games_dict:
    gd = games_dict[gid]
    # Gross compound if
    if gd.get("red", 0) <= sd["red"] and gd.get("green", 0) <= sd["green"] and gd.get("blue", 0) <= sd["blue"]:
        total_possible = total_possible + int(gid)

print(total_possible)