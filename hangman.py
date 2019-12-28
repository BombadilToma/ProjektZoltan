import random as rnd

def get_index(letter, word):
    word_list = [a for a in word]
    return_list=[]
    counter=0
    for element in word_list:
        if letter == element:
            return_list.append(counter)
        counter+=1
    return return_list

def akasztofa_message(letter, user_msg, akasztofa):
    user_msg_lst = [a for a in user_msg]
    string=''
    letter_index = get_index(letter,akasztofa)
    for darab in letter_index:
        user_msg_lst[darab*2] = letter

    for i in user_msg_lst:
        string += i
    return string

def szotar(lista):
    masiklista = []
    vegsolista=[]
    for elem in kitalalando:
        k=elem.strip()
        masiklista.append(k)

    for elem in masiklista:
        if " " in elem:
            segedlista = elem.split(" ")
            vegsolista += segedlista
        elif " " not in elem:
            vegsolista.append(elem)
    return vegsolista


with open ('szavasfile.txt', 'r') as f:
    kitalalando = f.readlines()
    egy_szo = szotar(kitalalando)

akasztofa = rnd.choice(egy_szo)
user_msg = len(akasztofa)*"_ "

print(f"""
Szia ez egy Hangman jatek. Gondoltam egy szora {len(akasztofa)} karakter hosszu.
Van 8 probalkozasod. Kerem az elso massalhangzot.
{len(akasztofa)*"_ "}
""")
akasztofax = list(akasztofa)
lifecount = 15
while '_' in user_msg and lifecount>0:
    guess = input(">>>")
    if guess in akasztofax:
        user_msg = akasztofa_message(guess, user_msg, akasztofa)
        print(user_msg)

    elif guess not in akasztofax:
        lifecount-=1
        print(f"""hat ez melle ment, {lifecount} eleted maradt.
{user_msg}""")

    if lifecount == 1:
        print("ez lesz az utolso probalkozasod")
else:
    if '_' not in user_msg:
        print("Gratula nyertel")
    else:
        print(f"""vesztettel vazeh, a szo "{akasztofa}" volt""")







