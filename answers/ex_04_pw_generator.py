import random, string , os

#Méthode pour retourner tout les caracteres que l'on veut
chars = string.ascii_letters  + '!@#$%^&*()' + string.digits

random.seed = (os.urandom(1024))

num = input("Combien de mot de passe : ")
num = int(num)

leng = input("Combien de caractères ( > 12 ) : ")
leng = int(leng)

if leng >= 12:
    for p in range(num):
        print (''.join(random.choice(chars) for i in range(leng)))
else:
    print('On a dit plus de 12 caractères ! Essaye encore !')