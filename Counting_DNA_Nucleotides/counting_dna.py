count_A = 0
count_C = 0
count_G = 0
count_T = 0

with open('rosalind_dna.txt', 'r') as file:
    dna_string = file.readline().strip()

for symbol in dna_string:
    if symbol == 'A':
        count_A += 1
    elif symbol == 'C':
        count_C += 1
    elif symbol == 'G':
        count_G += 1
    elif symbol == 'T':
        count_T += 1

print(count_A, count_C, count_G, count_T)