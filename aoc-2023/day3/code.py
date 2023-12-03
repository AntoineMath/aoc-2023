def check_valid(start, end, i):
    global lines, symbols
    return check_up(start, end, i, lines, symbols) \
            or check_down(start, end, i, lines, symbols) \
            or check_current(start, end, i, lines, symbols)

def check_up(start, end, i, lines, symbols):
    if i>0:
        for s in symbols[i-1]:
            if start-1 <= s <= end+1:
                return True
    return False

def check_current(start, end, i, lines, symbols):
    for s in symbols[i]:
        if start-1 <= s <= end+1:
            return True
    return False

def check_down(start, end, i, lines, symbols):
    if i==len(lines)-1:
        return False
    for s in symbols[i+1]:
        if start-1 <= s <= end+1:
            return True
    return False

def valid_number(start, end, line):
    return int(line[start:end+1])

def get_ratios(line, col):
    ratios = []
    ratio_count = 0

    if i>0:
        for g in groups[line-1]:
            start, end= g[0], g[1]
            if start-1 <= col <= end+1:
                ratio_count+=1
                if ratio_count >2: return 0
                ratios.append(int(lines[line-1][start:end+1]))
    if i<len(lines)-1:
        for g in groups[line+1]:
            start, end= g[0], g[1]
            if start-1 <= col <= end+1:
                ratio_count+=1
                if ratio_count >2: return 0
                ratios.append(int(lines[line+1][start:end+1]))
    for g in groups[line]:
        start, end= g[0], g[1]
        if start-1 <= col <= end+1:
            ratio_count+=1
            if ratio_count >2: return 0
            ratios.append(int(lines[line][start:end+1]))
    if ratio_count == 2:
        res = 1
        for r in ratios:
            res*=r
        return res
    else: 
        return 0
    

if __name__ == "__main__":
    res = 0
    #with open("example.txt") as f:
    with open("data.txt") as f:
        lines = f.readlines()
        symbols = []
        groups = []
        for l in lines:
            l = l.strip()
            already_in_group = False
            line_symbols = []
            line_groups = []
            start = 0
            for i, c in enumerate(l):
                if i == len(l)-1:
                    if c.isdigit():
                        if not already_in_group:
                            line_groups.append((i, i))
                        else:
                            line_groups.append((start, i))
                        break

                if c.isdigit():
                    if not already_in_group:
                        start = i
                        already_in_group = True
                else:
                    if already_in_group:
                        line_groups.append((start, i-1))
                        already_in_group = False

                    if c != ".": # special chars
                        line_symbols.append(i)
            symbols.append(line_symbols)
            groups.append(line_groups)


        for i, l in enumerate(lines):
            for g in groups[i]:
                start, end = g[0], g[1]
                if check_valid(start, end, i):
                    res+=int(lines[i][start:end+1])

        print("part1", res)

        # PART2

        gear_ratios = 0
        for i, line_symbols in enumerate(symbols):
            for s in line_symbols:
                if lines[i][s]=="*":
                    gear_ratios+=get_ratios(i, s)

        print("part2", gear_ratios)
