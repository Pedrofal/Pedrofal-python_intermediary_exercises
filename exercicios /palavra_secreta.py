secret_word = 'television'
attempts = 0
user_word = ''

while user_word != secret_word:
    user_letter = input('Enter one letter that you think is in the secret word: ')

    if len(user_letter) > 1:
        print ('Enter just one letter')
    

    elif user_letter in secret_word:
        user_letter += user_word
        attempts += 1
        print(f'')
        
    else:
        print('The secret word is:' + len(secret_word) *  ' * ')
        attempts += 1
else:
    print(f'The secret word ir {secret_word} and you found it in {attempts} attempts') 