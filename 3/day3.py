def main() -> int:
    a: list[list[str]] = []
    with open("./in2.txt", "r") as f:
        for line in f:
            a.append([c for c in line.rstrip("\n")])

    NROW = len(a)
    NCOL = len(a[0])

    def check_if_part(r: int, c: int, n_digits: int):
        for r1 in range(r - 1, r + 1 + 1):
            for c1 in range(c - 1, c + n_digits + 1):
                if r1 >= 0 and c1 >= 0 and r1 < NROW and c1 < NCOL:
                    c_i = a[r1][c1]
                    if c_i == '.' or c_i.isnumeric(): 
                        continue
                    # else we'll say it's symbolic
                    return True

        return False

    sum: int = 0
    s = ""
    for row in range(NROW):
        if len(s) > 0:
            if check_if_part(row, NCOL - len(s), len(s)):
                sum += int(s)
        s = ""
        for col in range(NCOL):
            # if there was a number at the end of the row
          
            c = a[row][col]
            # found a number, add it to current number builderrr
            if c.isnumeric():
                s += c
            else:
                if len(s) > 0:
                    if check_if_part(row, col - len(s), len(s)):
                        sum += int(s)
                    s = ""  # clear number for next round
        
        

    print(sum)


if __name__ == "__main__":
    main()
