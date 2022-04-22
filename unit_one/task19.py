algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
x = len(algoritm)

f = open("algoritm.csv", "w+")

for i in range(1, x):
    f.writelines(str(i) + " " + algoritm[i] + "\n")

f.close()