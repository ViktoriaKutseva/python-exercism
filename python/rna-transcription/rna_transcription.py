def to_rna(dna_strand):
    dna_rna_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    
    result = ''
    for key in dna_strand:
        value = dna_rna_dict[key]
        result += value
    return result
    

