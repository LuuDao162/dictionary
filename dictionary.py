dictionary = {'Con ong': 'bee',
            'Con thỏ': 'rabbit',
            'Con cua': 'crab',
            'Con mèo': 'cat',
            'Con ngựa': 'horse',
            'Con khỉ': 'monkey',
            'Con lừa': 'donkey',
            'Con hổ': 'tiger',
            'Con rùa': 'turtle',
            'Con sư tử': 'lion',
            'Con cá': 'fish'
            } 
def look_up(dictionary, input_word):
    for key in dictionary.keys():
        if key == input_word:
            return dictionary[key]

        
while True:    
    input_word = input("Bạn hãy nhập từ tiếng Việt cần tra nghĩa: ")
    translate_word = look_up(dictionary, input_word)
    print(translate_word)
    y_o_n = input("Bạn muốn tiếp tục [Y/N]?: ")
    if y_o_n.upper() == "N":
        break