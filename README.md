# FuzzyClassification
Seminarski rad iz predmeta Računarska Inteligencija na Matematičkom fakultetu.

Naš skup sa podacima sadrži 600+ fudbalera koji igraju na poziciji napadača.

| Name           | Rating  | Class | ... | Stamina | Heading | Finishing | 
|:--------------:| -------:| ----: | ---:| -------:| -------:| ---------:|
| C. Ronaldo     | 94      | 5     |     | 92      | 85      | 93        |
| L.Messi        | 93      | 5     |     | 74      | 71      | 95        |
| Neymar         | 92      | 5     |     | 79      | 62      | 89        |
| L. Suarez      | 92      | 5     |     | 89      | 77      | 94        |
| R. Lewandowski | 90      | 5     |     | 79      | 85      | 91        |

Svi fudbaleri su rasporedjeni u 5 klasa, gde najbolji napadači imaju oznaku 5. <br>
Napadači su svoje ocene dobili na osnovu rejtinga koji imaju.

| Rating    | Class| Number of instance |
| ---------:| ----:| ------------------:|
| 80-94     | 5    | 71                 |
| 79-75     | 4    | 116                |
| 74-71     | 3    | 184                |
| 70-66     | 2    | 199                |
| 66>       | 1    | 123                |

Atributi na osnovu kojih su ocenjeni fudbaleri:
``` Ball Control, Dribbling, Speed, Stamina, Heading, Finishing ```

Na ovom skupu za klasifikaciju, najbolje se pokazao `KNN` algoritam (`accuracy= ~0.75`)cija je matrica konfuzije:
```
Matrica konfuzije
    1  2  3  4  5
   -------------
1 | 3  3  0  0  0
2 | 1  7  2  0  0
3 | 0  1  8  0  0
4 | 0  0  0  5  0
5 | 0  0  0  1  3
```
Ovakav izlaz možemo smatrati dovoljno dobrim, s obzirom na to da smo mi ti koji smo 
dodelili klase igračima i da je veoma mala razlika između igrača npr sa rejtingom 80 i 79.
Prilikom provera igrača koji se nalaze na sredinama intervala svog rejtinga, algoritam odlično pogađa.
