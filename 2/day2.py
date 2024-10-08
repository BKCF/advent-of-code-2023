import math

N_RED: int = 12
N_GREEN: int = 13
N_BLUE: int = 14

with open("in.txt", "r") as f:
    game_sum: int = 0
    for game_number, line in enumerate(f, start=1):
        possible: bool = True

        # skip "Game {}: " without parsing the number out
        ndigit: int = math.floor(math.log10(game_number)) + 1
        i = ndigit + 7
        while i < len(line):
            #print("i", str(i))
            #print("char", line[i])
            # parse the next integer into n
            n = 0

            while line[i] != " ":
                n *= 10
                n += ord(line[i]) - 48  # 48 == ord('0')
                i += 1
            #print(f"{n}")

            #cursor is on the space
            # i is always a space, let's get the first letter of the color word
            # okay...so we know in the last elif that its's red. there's probably some irrelevant hyper-optimization that will make the code faster based on the order of conditionals...IDGAF!
            
            if line[i + 1] == "g":
                if n <= N_GREEN:
                    i += 6  # G R E E N + the space from earlier
                else:
                    possible = False
                    break
            elif line[i + 1] == "b":
                if n <= N_BLUE:
                    i += 5  # B L U E + the space from earlier
                else:
                    possible = False
                    break
            else:
                if n <= N_RED:
                    i += 4
                else:
                    possible = False
                    break

            # we actually don't care about the games. we only care if any draw of a color is > max
            # skip trailing comma/semicolon + space
            i += 2

        if False == possible:
            continue
        game_sum += game_number
    print("sum :",game_sum)
