TRANSLATE = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU', 'UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA', 'UAG', 'UGA'],
}


def proteins(strand):
    """Translates RNA sequences into proteins."""
    polypep = []
    codons = [strand[x:x+3] for x in range(0, len(strand), 3)]
    for codon in codons:
        if codon in TRANSLATE['STOP']:
            break
        for k, v in TRANSLATE.items():
            if codon in v:
                polypep.append(k)
    return polypep
