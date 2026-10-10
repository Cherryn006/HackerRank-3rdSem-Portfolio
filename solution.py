
n, q = map(int, input().split())

sequences = [[] for _ in range(n)]
lastAnswer = 0

for _ in range(q):
    query, x, y = map(int, input().split())
    idx = (x ^ lastAnswer) % n

    if query == 1:
        sequences[idx].append(y)
    else:
        lastAnswer = sequences[idx][y % len(sequences[idx])]
        print(lastAnswer)
