complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

with open('rosalind_revc.txt', 'r') as file:
    dna_string = file.readline().strip()

# Reverse the DNA string and apply the complement transformation
reverse_complement = ''.join(complement_dict[nucleotide] for nucleotide in dna_string[::-1])

print(reverse_complement)