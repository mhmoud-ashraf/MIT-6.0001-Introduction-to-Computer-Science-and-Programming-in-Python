# Problem Set 4B
# Name: Mahmoud Ashraf
# Collaborators: None
# Time Spent: -

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    tds. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
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



def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
#        pass #delete this line and replace with your code here
        self.message_text = text
        try: 
            self.valid_words = load_words(file_name)
        except NameError:
            self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
#        pass #delete this line and replace with your code here
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
#        pass #delete this line and replace with your code here
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
#        pass #delete this line and replace with your code here
        alphabet = string.ascii_letters
        dictionary_mapping = {}
        for letter in alphabet:
            letter_index = alphabet.find(letter)
            new_letter_index = letter_index + shift
            lower_case = new_letter_index > 25 and letter_index <= 25
            upper_case = new_letter_index > 51 and letter_index > 25
            if lower_case or upper_case:
                new_letter_index -= 26
            new_letter = alphabet[new_letter_index]
            dictionary_mapping[letter] = new_letter
        return dictionary_mapping

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
#        pass #delete this line and replace with your code here
        new_message = ''
        letters_mapping = self.build_shift_dict(shift)
        for char in self.message_text:
            if char in string.ascii_letters:
                char = letters_mapping[char]
            new_message += char
        return new_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
#        pass #delete this line and replace with your code here
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
#        pass #delete this line and replace with your code here
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
#        pass #delete this line and replace with your code here
        return self.build_shift_dict(self.shift).copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
#        pass #delete this line and replace with your code here
        return self.apply_shift(self.shift)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
#        pass #delete this line and replace with your code here
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
#        pass #delete this line and replace with your code here
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
#        pass #delete this line and replace with your code here
        max_number_of_real_words = 0
        best_shift = 0
        decrypted_message = ''
        for shift in range(26):
            number_of_real_words = 0
            decoded_messeage = self.apply_shift(shift)
            for word in decoded_messeage.split(' '):
                if len(word)==1:
                    if word in string.ascii_letters:
                        if is_word(self.get_valid_words(), word) == True:
                            number_of_real_words+=1
                else:
                    if is_word(self.get_valid_words(), word) == True:
                        number_of_real_words+=1
            if number_of_real_words > max_number_of_real_words:
                max_number_of_real_words = number_of_real_words
                best_shift = shift
                decrypted_message = decoded_messeage
        return (best_shift, decrypted_message)


if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

#    TODO: WRITE YOUR TEST CASES HERE
    # todo test case 1
    # test case for PlaintextMessage 
    plaintext = PlaintextMessage('The goal keeper saved our ass.', 6)
    print('Expected Output: Znk mugr qkkhx ygbkj uax gyy.')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #test case for CiphertextMessage
    ciphertext = CiphertextMessage('Znk mugr qkkvkx ygbkj uax gyy.')
    print('Expected Output:', (20, 'The goal keeper saved our ass.'))
    print('Actual Output:', ciphertext.decrypt_message())

    # todo test case 2
    # test case for PlaintextMessage 
    plaintext = PlaintextMessage('I hate YOU!!!!', 15)
    print('Expected Output: X wpit NDJ!!!!')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #test case for CiphertextMessage
    ciphertext = CiphertextMessage('X wpit NDJ!!!!')
    print('Expected Output:', (11, 'I hate YOU!!!!'))
    print('Actual Output:', ciphertext.decrypt_message())

#    TODO: best shift value and unencrypted story 
    ciphertext = CiphertextMessage(get_story_string())
    print('Best shift value:', ciphertext.decrypt_message()[0])
    print('unencrypted story:\n',ciphertext.decrypt_message()[1])
    
#    pass #delete this line and replace with your code here
    