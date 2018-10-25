# fantasy-textgen
Randomly generates a string of fantastic text.

## How to use:
fantasy_gen.py can be run from your terminal by typing "python fantasy_gen.py [numberOfWords]". The number of words must be provided, or the program will probably break, since this is a very quick and dirty project. texts.txt and texts.json are provided for you to play with. The program in its current state has already converted texts.txt into a dictionary, stored in texts.json, and therefore simply reads the dictionary in from texts.json for a much faster runtime. However, should you wish to provide your own text, some (currently commented out) lines of code in fantasy_gen.py will convert them into a dictionary for you.
