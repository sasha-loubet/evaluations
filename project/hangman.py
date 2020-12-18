import random

#def lors du lancement
def start():
    print("JOUER AU PENDU")
    while game():
        pass

def word():
    list_word = open("words.txt", "r").readlines()
    random_number = random.randint(0, len(list_word))
    word = list_word[random_number].rstrip()
    return word

#def ingame

def guess_letter():
    letter = (input("Choisie une lettre : ").upper())
    letter.strip()
    return letter

def game():
    choose_word = word()
    print("Le mot contient {} lettres.".format(len(choose_word )))
    choice = len(choose_word ) * ["-"]
    print("".join(choice))
    tries = 6
    letters_tried = ""
    letters_wrong = 0
    while (letters_wrong != tries) and ("".join(choice) != choose_word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("Tu as deja choisis", letter)
            else:
                letters_tried += letter
                first_index = choose_word .find(letter)
                if first_index == -1:
                    letters_wrong += 1
                else:
                    for i in range(len(choose_word)):
                        if letter == choose_word[i]:
                            choice[i] = letter
        else:
            print("")
        print(hanged(letters_wrong))
        print("".join(choice))
        print("Lettre choisie :", letters_tried)
        if letters_wrong == tries :
            print("PERDU! {}".format(choose_word))
            break
        if "".join(choice) == choose_word:
            print("GAGNEEEEEEEE")
            break


#definition de hanged (piqué sur internet)
def hanged(man):
    graphic = [
    '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]
if __name__ == "__main__":
    start()