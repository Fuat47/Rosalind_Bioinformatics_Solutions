rna_codon_table = {}
with open('RNA_codon_table.txt', 'r') as table_file:
    for line in table_file:
        codon_data = line.split()
        codon = codon_data[0]
        amino_acid = codon_data[1]
        rna_codon_table[codon] = amino_acid

with open('rosalind_prot.txt', 'r') as file:
    rna_string = file.readline().strip()

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