# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
alphabet= 'abcdefghijklmnopqrstuvwxyz'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
            
        doctor={}
        upper_perm=vowels_permutation.upper()
        for i in alphabet:
            doctor.update({i:i})
        for j in alphabet.upper():
            doctor.update({j:j})
        for k in range(len(VOWELS_LOWER)):
            doctor[VOWELS_LOWER[k]]=vowels_permutation[k]
        for l in range(len(VOWELS_UPPER)):
            doctor[VOWELS_UPPER[l]]=upper_perm[l]
        
        return doctor
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        benkuz=[]
        after=self.get_message_text()
        for k in after:
            if(transpose_dict.get(k,0)==0):
                benkuz.append(k)
            else:
                benkuz.append(transpose_dict[k])
        dollar=''.join(benkuz)
        return dollar
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self,text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        best=0
        numero=VOWELS_LOWER
        origtext=SubMessage.get_message_text(self)
        text=origtext.split()
        daz=get_permutations(VOWELS_LOWER)
        for w in daz:
            count=0
            talker=SubMessage.build_transpose_dict(self,w)
            for token in text: 
                drez=SubMessage(token)
                temp=drez.apply_transpose(talker)
                if is_word(drez.get_valid_words(), temp):
                    count+=1
            if count>=best:
                numero=w
                best=count
                
        duncan=SubMessage.build_transpose_dict(self,numero)
        new_message=SubMessage.apply_transpose(self,duncan)
        return new_message
        
        
        
    

if __name__ == '__main__':
    
    subtext = SubMessage('beta')
    print('Expected Output: buta')
    daft=subtext.build_transpose_dict('auioe')
    print('Actual Output:', subtext.apply_transpose(daft))
     
    subtext1 = SubMessage('There once was a man from Nantucket.')
    print('Expected Output: Thuru oncu was a man from Nanteckut.')
    daft1=subtext1.build_transpose_dict('auioe')
    print('Actual Output:', subtext1.apply_transpose(daft1))
     
    entext = EncryptedSubMessage('cuul')
    print('Expected Output: cool')
    print('Actual Output:', entext.decrypt_message())
     
    entext1 = EncryptedSubMessage('Eporatien Cemploto.')
    print('Expected Output: Operation Complete.')
    print('Actual Output:', entext1.decrypt_message())
