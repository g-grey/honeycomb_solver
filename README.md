# Honeycomb Solver

Solves honeycomb word puzzles

```
        ___
       /   \  
   ___/  V  \___
  /   \     /   \
 /  H  \___/  C  \
 \     /   \     /
  \___/  R  \___/
  /   \     /   \
 /  A  \___/  L  \
 \     /   \     /
  \___/	 I  \___/
      \     /
       \___/
```

Rules: 
-	Words must contain at least 4 letters
-	Words MUST include the center letter
-	Words may not be proper nouns or hyphenated (note: word lists with proper nouns will give false positives)
-	Letters can be used more than once
- Each puzzle includes at least one “pangram” which uses every letter. 

Example:

`python honeycomb_solver.py r ahvcli`

Or optionally provide your own world list

`python honeycomb_solver.py r ahvcli your_word_list.txt`
 
