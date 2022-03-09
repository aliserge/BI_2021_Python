class Rna():
    def __init__(self,string):
        bases = ('A', 'U', 'G', 'C', 'N')
        for base in string:
            if base not in bases:
                return ('Please provide RNA (A, U, G, C, N)')
        self.rna_sequence = string
        
        self.rna_len = len(self.rna_sequence)
    def gc_content(self):
        return sum([base in ('G', 'C') for base in self.rna_sequence]) / self.rna_len
    def reverse_complement(self):
        complimentary_map = {
        'A' : 'U',
        'U' : 'A',
        'G' : 'C',
        'C' : 'G',
        'N' : 'N' 
            }
        return ''.join([complimentary_map[base] for base in self.rna_sequence])
    
    ### Iterator part
    def __iter__(self):

        return self.rna_sequence.__iter__()

    ### eq and hash
    def __eq__(self, other_obj):
        if isinstance(other_obj, Rna):
            return self.rna_sequence == other_obj.rna_sequence
        return False
    def __hash__(self):
        return hash(self.rna_sequence)
    

class Dna():
    def __init__(self,string):
        bases = ('A', 'T', 'G', 'C', 'N')
        for base in string:
            if base not in bases:
                return ('Please provide DNA (A, T, G, C, N)')
        self.dna_sequence = string
        self.dna_len = len(self.dna_sequence)
    def gc_content(self):
        return sum([base in ('G', 'C') for base in self.dna_sequence]) / self.dna_len
    def reverse_complement(self):
        complimentary_map = {
        'A' : 'T',
        'T' : 'A',
        'G' : 'C',
        'C' : 'G',
        'N' : 'N',
            }
        return ''.join([complimentary_map[base] for base in self.dna_sequence])
    
    ### Iterator part
    def __iter__(self):
        return self.dna_sequence.__iter__()
   
    ### eq and hash
    def __eq__(self, other_obj):
        if isinstance(other_obj, Dna):
            return self.dna_sequence == other_obj.dna_sequence
        return False
    def __hash__(self):
        return hash(self.dna_sequence)
    
    ### trabscribe
    def transcribe(self):
        transcribe_map = {
        'A' : 'A',
        'T' : 'U',
        'G' : 'G',
        'C' : 'C',
        'N' : 'N',
            }
        rna_seq = ''.join([transcribe_map[base] for base in self.dna_sequence])
        return Rna(rna_seq) 
