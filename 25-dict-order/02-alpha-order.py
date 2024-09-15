from collections.abc import MutableMapping

votes = {
    "otter": 1281,
    "polar bear": 587,
    "fox": 863,
}


class SortedDict(MutableMapping):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        # 字母序
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)