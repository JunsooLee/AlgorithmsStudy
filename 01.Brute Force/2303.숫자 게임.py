from itertools import combinations

N = int(input())
people = []

for idx in range(N):
    card = list(map(int, input().split(' ')))
    comb = set(combinations(card, 3))
    max_value = 0
    for c in comb:
        max_value = (sum(c) % 10) if max_value <= (sum(c) % 10) else max_value

    people.append(max_value)

winner_value = max(people)

for idx in range(N):
    if people[idx] == winner_value:
        winner = idx + 1

print(winner)
