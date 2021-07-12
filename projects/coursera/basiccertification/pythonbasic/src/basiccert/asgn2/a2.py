def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    total = 0
    for ch in dna:
        if ch == nucleotide:
            total = total + 1
    return total


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

     Return True if and only if the DNA sequence is valid
     (that is, it contains no characters other than ’A’, ’T’,’C’ and ’G’ 
     casesensitive).

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('atCGCG')
    False
    >>> is_valid_sequence('atcggc')
    False    
    >>> is_valid_sequence('ATCXGGC')
    False
    """
    isvalid = True
    for ch in dna:
        if ch not in "ATCG":
            isvalid = False
    return isvalid 
    

def insert_sequence(indna,addna,at):
    """ (str,str,int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.
    Assumption:  index that is "at" is valid. 

    >>> insert_sequence('ATGC','CG',2)
    ATCGGC
    >>> insert_sequence('CCGG','AT',2)
    CCATGG
    >>> insert_sequence('AGCC','TA',3)
    AGCTAC    
    >>> insert_sequence('TGG','TAG',1)
    TTAGGG
    """
    return indna[:at]+addna+indna[at:] 


def get_complement(nct):
    """ (str) -> str

     Return the nucleotide's complement.
     The first parameter is a nucleotide ( that is ’A’, ’T’, ’C’ or ’G’)
    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G    
    >>> get_complement('G')
    C
    >>> get_complement('M')
    """
    cmpl=None
    if nct ==  "A":
        cmpl = 'T'
    elif nct ==  "T":
        cmpl = 'A'
    elif nct ==  "C":
        cmpl = 'G'
    elif nct ==  "G":
        cmpl='C' 
    return cmpl


    
def get_complementary_sequence(dna):
    """ (str) -> str

     Return the DNA sequence that is complementary to the given DNA sequence.
     The parameter is a DNA sequence. 
     
    >>> get_complementary_sequence('ATCGGC')
    'TAGCCG'
    >>> get_complementary_sequence('GGAACCCTA')
    'CCTTGGGAT'
    >>> get_complementary_sequence('AT')
    'TA'    
    >>> get_complementary_sequence('GCAT')
    'CGTA'
    """
    cmpseq = ''
    for ch in dna:
          cmpseq = cmpseq + get_complement(ch)
    return cmpseq 
