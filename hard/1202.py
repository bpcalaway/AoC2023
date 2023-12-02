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
                color = count.split(" ")[1].strip("\n")
                num = int(count.split(" ")[0])
                if color in rounds_dict:
                    num = max(num, rounds_dict[color])
                rounds_dict[color] = num
        
        # We should have the maxed out counts from across the rounds, assign them to the game id
        games_dict[game_id] = rounds_dict

# This is the comparison dict, we'll loop and look at possible solutions
total_powers = 0
for gid in games_dict:
    # Insanely rare instantiation of 1?
    cur_power = 1
    for c in games_dict[gid]:
        # If we never pull a color is it zero?
        cur_power = cur_power * games_dict[gid].get(c, 0)
    total_powers = total_powers + cur_power

print(total_powers)