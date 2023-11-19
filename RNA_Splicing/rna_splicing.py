rna_codon_table = {}
with open('RNA_codon_table.txt', 'r') as table_file:
    for line in table_file:
        codon_data = line.split()
        codon = codon_data[0]
        amino_acid = codon_data[1]
        rna_codon_table[codon] = amino_acid
        
introns = []
dna_string = []
with open('rosalind_splc.txt', 'r') as file:
    file.readline() #to skip name of DNA
    while True:
        line = file.readline()
        if line[0] == ">":
            break
        dna_string.append(line.strip())
    for line in file.readlines():
        if line[0] != ">": #to skip name of introns
            introns.append(line.strip())
dna_string = "".join(dna_string)

remaining_part = [True] * len(dna_string)
for intron in introns:
    for i in range(len(dna_string) - len(intron) + 1):
        if dna_string[i:i + len(intron)] == intron:
            for j in range(len(intron)):
                remaining_part[i+j] = False

exons = []
for i in range(len(dna_string)):
    if remaining_part[i]:
        exons.append(dna_string[i])
        
exons = "".join(exons)
rna_string = exons.replace('T', 'U')

amino_acids = []
for i in range(0, len(rna_string), 3):
    codon = rna_string[i:i + 3]
    amino_acid = rna_codon_table[codon]
    if amino_acid != 'Stop': 
        amino_acids.append(amino_acid)
    else:
        break  
    
protein_string = ''.join(amino_acids)
print(protein_string)