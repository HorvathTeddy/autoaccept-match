import os

def output_wrapper():
    os.system('cls')
    return 'EZ Queue will automatically accept your League of Legends match'

def output_message(message):
    print(output_wrapper())
    print(message)
