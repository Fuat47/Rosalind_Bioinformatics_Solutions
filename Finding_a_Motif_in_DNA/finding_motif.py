with open('rosalind_subs.txt', 'r') as file:
    s = file.readline().strip()
    t = file.readline().strip()

positions = []
for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
        positions.append(i + 1)  # Adding 1 to convert 0-based index to 1-based index

print(*positions)