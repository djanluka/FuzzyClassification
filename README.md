# FuzzyClassification
Seminarski rad iz predmeta Računarska Inteligencija na Matematičkom fakultetu.

Naš skup sa podacima sadrži 692 fudbalera koji igraju na poziciji napadača.

| Name           | Rating  | Class | ... |  Finishing | 
|:--------------:| -------:| ----: | ---:|  ---------:|
| C. Ronaldo     | 94      | 5     |     |  93        |
| L.Messi        | 93      | 5     |     |  95        |
| Neymar         | 92      | 5     |     |  89        |
| L. Suarez      | 92      | 5     |     |  94        |
| R. Lewandowski | 90      | 5     |     |  91        |

Svi fudbaleri su rasporedjeni u 5 klasa, gde najbolji napadači imaju oznaku 5. <br>
Napadači su svoje ocene dobili na osnovu rejtinga koji imaju.

| Rating    | Class| Number of instance |
| ---------:| ----:| ------------------:|
| 80-94     | 5    | 70                 |
| 79-75     | 4    | 116                |
| 74-71     | 3    | 184                |
| 70-66     | 2    | 199                |
| 66>       | 1    | 123                |

Atributi na osnovu kojih su ocenjeni fudbaleri:
``` Ball Control, Dribbling, Speed, Finishing ```.

Naš zadatak je bio da napravimo fazi algoritam koji će odrediti klasu fudbalera.
