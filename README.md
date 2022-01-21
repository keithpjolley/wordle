# wordle.py
python wordle solver


## Usage:

```
usage: wordle.py [-h] [--guesses GUESSES] [--nots NOTS] have

Wordle guesser. Start with ".....".

positional arguments:
  have               The word. UC for right place, lc for wrong place, else
                     "."

optional arguments:
  -h, --help         show this help message and exit
  --guesses GUESSES  How many guesses to return.
  --nots NOTS        Characters that are NOT in the word.

```

To start you don't know any letters and none are ruled out so your first entry
should be '.....'.

Let's say you enter 'eight' into wordle and you find out that 'g' is in the
correct spot (green), 't' is in an incorrect position but in the word (yellow),
and the rest are bad guesses. 

You'd find out the next guesses with:
```
⇒  ./wordle.py ..G.t --nots eih
```

`--guesses N` says list N guesses. Default is 15. 


## Example:

*First guess:*  
![starting wordle grid](images/wordle1.jpg "Starting Wordle Grid")


```
⇒  ./wordle.py .....
20458: arose
20458: oreas
20455: aries
20455: arise
20455: raise
20455: serai
20369: leora
20366: ariel
20353: erian
20353: irena
20353: reina
20306: orate
20303: arite
20303: artie
20303: irate
20303: retia
```

Note that not all words in the input dict `/usr/share/dict/words` are in the wordle dictionary so you may
need to skip the highest rated words. `arose` is my go-to start word.

---

*Second Guess:*  
![First guess wordle grid](images/wordle2.jpg "First guess Wordle Grid")


```
⇒  ./wordle.py .R... --guess 5 --nots aose
239: bruit
239: fruit
230: irgun
229: bruin
226: print
225: urbic
```

Don't know what `bruit` is. Would think it's not in most puzzle word lists.
Go with `fruit` instead.

---

*Third Guess:*  
![Second guess wordle grid](images/wordle3.jpg "Second guess Wordle Grid")

```
⇒  ./wordle.py .R.i. --guess 5 --nots aosefut
84: prink
82: prick
80: crink
79: crimp
79: gripy
78: brink
```

Not sure I've heard of `prink` so go with `prick`.

---

*Got it!*  

![Solved wordle grid](images/wordle4.jpg "Solved Wordle Grid")
