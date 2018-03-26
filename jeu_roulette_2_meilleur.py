print("bienvenue dans le jeu des paris !")
print("au debut de la partie, vous commencerez avec 100 prems")
print("vous choisirez d'abord un intervalle (par exemple de 1 à 2 ou de 1 à 10 ou de 1 à 100)")
print("puis vous parierez sur un numero dans cet intervalle")
print("au moment de parier, vous indiquerez la somme que vous voulez miser")
print("ensuite, un numero sera tiré au hasard à l'interieur de l'intervalle")
print("si le numero sur lequel vous aviez parié sort, vous récupérez votre mise plus n fois votre mise")
print("le facteur n dépendra de l'intervalle que vous aurez choisi")
print("par exemple, si vous choisissez l'intervalle [1,2], n sera equal à 1")
print("donc, dans cet exemple(intervalle [1,2]), si vous pariez 50 prems et que votre numero tombe juste,")
print("vous récupérez vos 50 prems, et vous en gagnez 50 de plus.")
print("votre cagnotte s'élevera alors à 150 prems")
print("si le numero n'est pas le bon, vous perdez votre mise")
print("pour la table des valeurs de n en fonction des intervalles c'est très simple :")
print("pour [1,2] : n=1 ; pour [1,3] : n=2 ; pour [1,4] : n=3 ; etc...")
print("d'une manière générale, n=limite_superieure - 1")
print("pour info :")
print("high score of Sûrya Leonforte : 4025")
print("high score of Lucas Leonforte : 4000")
p=100
while p>0:
    a=input("entrez la limite supérieure de votre intervalle (par exemple 2 pour l'intervalle [1,2]) :")
    a=int(a)
    b=input("maintenant, entrez le numero sur lequel vous voulez pariez :")
    b=int(b)
    while b<1 or b>a:
        b=input("entrez un numero dans l'intervalle choisi !!")
        b=int(b)
    c=input("pour finir, entrez la somme que vous voulez miser :")
    c=int(c)
    while c<1 or c>p:
        c=input("entrez une somme que vous possédez !!")
        c=int(c)
    from random import *
    d=randint(1,a)
    print("le numero sorti est le:",d)
    if b==d:
        print("félicitations !! vous récupérez votre mise et gagnez en plus",(a-1)*c,"prems")
        p=p+(a-1)*c
    else:
        print("vous perdez votre mise")
        p=p-c
    print("vous possédez maintenant",p,"prems")
print("vous n'avez plus de prems, la partie est terminée")

        
        
