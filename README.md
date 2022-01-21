# wordle
python wordle solver


## Usage:

![starting wordle grid](images/wordle1.jpg "Starting Wordle Grid")

*First guess:*

```
% ./wordle.py .....                                                                                          22-01-18 - 7:56:54
12623: aries
12623: arise
12623: raise
12623: serai
12567: erian
12567: irena
12567: reina
12550: ariel
12526: arite
12526: artie
12526: irate
12526: retia
12526: tarie
12431: arose
12431: oreas
12358: leora
```

Note that not all words in the input dict `/usr/share/dict/words` are in the wordle dict so you may
need to skip the highest rated words. Also, if there are a bunch of obscure words at the top of the
list then a very common word, you may want to go with the more common word.


![First guess wordle grid](images/wordle2.jpg "First guess Wordle Grid")

*Second Guess:*

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

![Second guess wordle grid](images/wordle3.jpg "Second guess Wordle Grid")

*Third Guess:*

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
Got it!

![Solved wordle grid](images/wordle4.jpg "Solved Wordle Grid")
