def get_card_matches(card: str) -> int:
    winnings = card.split("|")[0].split(":")[1].strip().replace("  ", " ").split(" ");
    actual = card.split("|")[1].strip().replace("  ", " ").split(" ");
    matches = sum([a in winnings for a in actual])
    return matches


def get_score(nb_matches):
    tot = 0
    if nb_matches > 0:
        tot+=2**(nb_matches-1)

    return tot


def get_nb(card):
    return int(card.split(":")[0].split("Card")[1].strip())


with open("data.txt") as f:
    cards = [l.strip() for l in f.readlines()]

    # PART1
    tot = 0
    for c in cards:
        tot += get_score(get_card_matches(c))
    print(tot)

    # PART2 
    # TODO : DP 
    d = {k:1 for k in range(len(cards))}
    for i, c in enumerate(cards):
        score = get_card_matches(c)
        for s in range(d[i]):
            for j in range(score):
                d[i+j+1] +=1
    print(sum(d.values()))