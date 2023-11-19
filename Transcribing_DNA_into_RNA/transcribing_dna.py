with open('rosalind_rna.txt', 'r') as file:
    dna_string = file.readline().strip()

rna_string = dna_string.replace('T', 'U')
print(rna_string)