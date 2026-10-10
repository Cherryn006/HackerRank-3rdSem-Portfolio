
def matchingStrings(stringList, queries):
    frequency = {}

    for s in stringList:
        frequency[s] = frequency.get(s, 0) + 1

    return [frequency.get(query, 0) for query in queries]


if __name__ == "__main__":
    n = int(input().strip())
    stringList = [input().strip() for _ in range(n)]

    q = int(input().strip())
    queries = [input().strip() for _ in range(q)]

    result = matchingStrings(stringList, queries)

    for count in result:
        print(count)
