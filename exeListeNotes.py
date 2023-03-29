def ExoNotes():
    nbEleves=input("Entrer le nombre d'élèves")
    nbMatieres=input("Entrer le nombre de matieres")
    nbEleves=int(nbEleves)
    nbMatieres=int(nbEleves)
    listeNotes=[]
    for i in range (0,nbEleves):
        print("Eleve ",i)
        listeNotes.append([])
        for j in range (0,nbMatieres):
            listeNotes[i].append([])
            print("Matiere ", j)
            randNote=0
            k=0
            while(randNote>=0):
                if(k==0):
                    randNote=random.randint(0,20)
                else:
                    randNote = random.randint(-4, 20)
                if(randNote>=0):
                    print("Note ", k+1," : ",randNote)
                    listeNotes[i][j].append([])
                    listeNotes[i][j][k]=randNote
                k+=1
    print("Les notes ont été entrées automatiquement")
    print("#########################################")
    totalNbNotes=0
    totalScoreNotes=0
    minClasse=20
    maxClasse=0
    for i in range(0, nbEleves):
        print("Eleve ", i)
        cumulNotes=0
        nbNotes=0
        for j in range(0, nbMatieres):
            print("Matiere ", j)
            minElMat=20
            maxElMat = 0
            for k in range(0,len(listeNotes[i][j])):
                if(listeNotes[i][j][k]<minElMat):
                    minElMat=listeNotes[i][j][k]
                if (listeNotes[i][j][k] > maxElMat):
                    maxElMat = listeNotes[i][j][k]
                if (listeNotes[i][j][k] < minClasse):
                    minClasse = listeNotes[i][j][k]
                if (listeNotes[i][j][k] > maxClasse):
                    maxClasse = listeNotes[i][j][k]
                nbNotes+=1
                cumulNotes+=listeNotes[i][j][k]
                totalNbNotes += 1
                totalScoreNotes += listeNotes[i][j][k]
            print("Minimum Matiere ",j," : ",minElMat)
            print("Maximum Matiere ",j," : ", maxElMat)
            print("Moyenne Matiere ",j," : ", (cumulNotes/nbNotes))
            print("- - - - - - -")
        print("___________________")
    print("=======================")
    print("Minimum Classe : ", minClasse)
    print("Maximum Classe : ", maxClasse)
    print("Moyenne Classe : ", (totalScoreNotes / totalNbNotes))

    print("Les notes ont été entrées automatiquement")
