votes = {
    "otter": 1281,
    "polar bear": 587,
    "fox": 863,
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)  # {'otter': 1, 'fox': 2, 'polar bear': 3}
winner = get_winner(ranks)
print(winner)  # otter
