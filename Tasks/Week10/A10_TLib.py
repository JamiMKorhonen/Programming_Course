def readValues(Values, Filename):
    with open(Filename, "r") as fileHandle:
        for line in fileHandle:
            stripped = line.strip()
            if stripped != "":
                Values.append(int(stripped))
    return Values

def displayValues(Values, Filename):
    print(f"Raw '{Filename}' ->", end=" ")
    print(*Values, sep=", ")
    return None

def bubbleSort(Values, PAsc):
    n = len(Values)

    for i in range(n):
        for j in range(0, n - i - 1):
            if (PAsc and Values[j] > Values[j + 1]) or (not PAsc and Values[j] < Values[j + 1]):
                Values[j], Values[j + 1] = Values[j + 1], Values[j]
    return Values