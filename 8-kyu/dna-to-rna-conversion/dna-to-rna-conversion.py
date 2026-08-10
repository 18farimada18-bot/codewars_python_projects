def dna_to_rna(dna):
    # split each letter into an item in a list
    dna_list = list(dna)
    # iterate thru the list
    for d in dna_list:
        if d == "T":
            # if T, change to u via reassignment
            dna_list[dna_list.index(d)] = "U"
    # mush together and return
    return "".join(dna_list)
​