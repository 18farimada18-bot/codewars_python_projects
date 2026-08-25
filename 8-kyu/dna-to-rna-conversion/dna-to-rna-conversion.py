def dna_to_rna(dna):
    dna_list = list(dna)
    for i in dna_list:
        if i =="T":
            dna_list[dna_list.index("T")] = "U"
    return "".join(dna_list)