def to_rna(dna_strand):
    dna_rna_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(dna_rna_dict[key] for key in dna_strand)
