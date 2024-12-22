players = {"Kshitiz":4, "Vlad":1, "David":5, "Sebastian":6, "Joe":2, "Toma":0}
sorted_by_values = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_values)