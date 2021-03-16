note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

notes_eleve1=[]
for n in notes :
  if n[0]=="eleve1":
    notes_eleve1.append(n[2])
  moy= sum(notes_eleve1)/len(notes_eleve1)
print("la moyenne de l'éléve 1 est de",moy)



notes_eleve1_math=[]
matiere="math"
for n in notes :
  if n[0]=="eleve1":
    if n[1]==matiere:
      notes_eleve1_math.append(n[2])
      moy_m= sum(notes_eleve1_math)/len(notes_eleve1_math)
print(f"la moyenne de l'éléve 1 en {matiere} est de",moy_m)


def moyenne_tuples(notes, matiere, eleve):
  notes_filtres=[]
  for n in notes :
    if n[0]==eleve:
      if n[1]==matiere:
        notes_filtres.append(n[2])
  moy_m= sum(notes_filtres)/len(notes_filtres)
  print(f"la moyenne de l'{eleve} en {matiere} est de",moy_m)

moyenne_tuples(notes,"math","eleve1")
moyenne_tuples(notes,"math","eleve2")
