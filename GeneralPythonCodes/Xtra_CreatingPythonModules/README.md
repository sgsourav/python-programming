# Creating Python Modules

Any `.py` file can be used as an external module in Python, for other scripts to `import` and use. Generally, `.py` files with definitions of variables, functions and classes are used as modules. Such definitions can be imported into the `__main__` module while executing the top-level script. Within any python module, the `__name__` of that module is stored as `__main__`. Thus, while executing the top-level python script, the script itself is named the `__main__` module.

In this directory, there are two `.py` files, as follows.
- `playingcards.py` : Defines three classes Card, Deck, Hand. May be imported as a module.
- `cardgame.py` : Imports Card, Deck, Hand from the module to initiate a simple card game.

Note that if you execute the module `playingcards.py`, it will execute the testing routine for Card, Deck and Hand classes, as written under its `if __name__ == "__main__"` clause. However, if you execute the script `cardgame.py`, it just imports the module, but does not execute the testing routine.

---

**License Declaration** : Following the lead from the inspirations for this material, and the *spirit* of Python education and development, all modules of this work are licensed under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
