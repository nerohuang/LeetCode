board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
charStore = {};
for row in board:
    for char in row:
        if char not in charStore:
            charStore[char] = 1;
        else:
            charStore[char] += 1;
for char in word:
    if char in charStore:
        charStore[char] -= 1;
        if not charStore[char]:
            print(False);
    else:
        print(False);
print(True);