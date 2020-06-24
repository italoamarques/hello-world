#Given a DNA strand, return its RNA complement (per RNA transcription).
#Both DNA and RNA strands are a sequence of nucleotides.
#The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
#The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
#Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
#G -> C
#C -> G
#T -> A
#A -> U

print(' --- DNA to RNA converter ---')
DNA = input('Enter the DNA strand:\n')
def DNA_to_RNA(DNA):
    RNA = []
    conversion = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
    }
    for item in DNA:
        if (item in conversion.keys()):
            RNA.append(conversion[item])
    return ''.join(RNA)

print('\nThe transcribed RNA strand is:\n{}'.format(DNA_to_RNA(DNA)))

