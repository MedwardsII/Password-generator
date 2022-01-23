from string import ascii_lowercase, ascii_uppercase \
    , digits, punctuation
import secrets


def password_generator(password_length, template_str):
    '''
    Function to create a random password string.
    '''
    for n in range(0, int(password_length)):
        yield secrets.choice(template_str)

def create_password_str(**kwargs):
    '''Function to create string object to create password'''
    template_str = ''
    if kwargs['has_lower']:
        template_str += ascii_lowercase
    if kwargs['has_upper']:
        template_str += ascii_uppercase
    if kwargs['has_digit']:
        template_str += digits
    if kwargs['has_punctuation']:
        template_str += punctuation
    return template_str
