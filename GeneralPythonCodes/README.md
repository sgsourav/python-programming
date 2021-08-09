# Python Scripts

**Learn how to use standard Python Interpreters and IDEs.**

Standalone Python code and scripts may be executed in multiple ways, as follows.
- Directly within **Python Interpreters** : Generally executed line-by-line or cell-by-cell. Good enough for basic programs and to practice while you learn python.
- Through **Command-Line** and **IDEs** : Generally executed as a complete script (single file) or as a multi-file program. Good for most standard python programs.

## Python Interpreters

The popular interpreters to run code/scripts within (generally line-by-line) are the basic **Python Interpreter** and the slightly more sophisticated **IPython Interpreter**. Both of these are accessible through the terminal in Linux/Mac and command prompt in Windows after you have installed python on your system. Install Python 3.8 to start with.

#### Installing Python
In terms of this course, the easiest way to install Python 3.8 and all relevant packages for computation is to install the entire [Anaconda platform for Python 3.8](https://www.anaconda.com/products/individual). Install it, open the `terminal` in case of Linux/Mac or the `cmd`  prompt in case of Windows, and check the version of python to make sure you have installed everything correctly.

```
$ python --version
Python 3.8.10
```

If this works fine, you are most likely in your `(base)` environment for `conda`, and your default python interpreter is Python 3.8. This is the most convenient setup for us.

#### Python Interpreter
Install Python 3.8 on your computer, open the `terminal` in case of Linux/Mac or the `cmd`  prompt in case of Windows, check the version of python, and type `python` to get to the basic Python Interpreter. You may execute basic codes in this interpreter, line by line.

```
Python 3.8.10 (default, May 19 2021, 11:01:55)     
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin     
Type "help", "copyright", "credits" or "license" for more information.   
>>> print("Hello Sourav!")
Hello Sourav!
>>>
```

#### IPython Interpreter
Install Python 3.8 on your computer, open the `terminal` in case of Linux/Mac or the `cmd`  prompt in case of Windows, check the version of python, and type `ipython` to get to the slightly more sophisticated IPython Interpreter. You may execute basic codes in this interpreter, in cells.

```
Python 3.8.10 (default, May 19 2021, 11:01:55)     
Type 'copyright', 'credits' or 'license' for more information    
IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.    

In [1]: print("Hello Sourav!")                                                                                               
Hello Sourav!

In [2]:
```

#### Online Python Interpreter
If you want to practice your python programming online, without installing anything on your computer, check out [https://repl.it/languages/python3](https://repl.it/languages/python3). You may execute standard codes and scripts in this online interpreter (or IDE), same as in the local interpreters.

```
Python 3.8.2 (default, Feb 26 2020, 02:56:10)
> print("Hello Sourav!")
Hello Sourav!
>
```

We will start online with [repl.it](https://repl.it/languages/python3), but it is highly recommended that you install the entire [Anaconda platform for Python 3.8](https://www.anaconda.com/products/individual) on your own computer. You will need it all the time!

## Command-Line and IDEs

The codes in this directory are mostly *scripts* written in Python, and sometimes, even multi-file programs. They all have `.py` extension, and can be executed directly from the command-line -- through the **Terminal** in Linux/Mac and **Command Prompt** in Windows. You may of course choose an Integrated Development Environment (IDE) of your choice to edit and run these Python scripts more conveniently.

#### Command-Line Interface (CLI)

Using the command-line interface is a necessary skill for using remote servers. Open the `terminal` in case of Linux/Mac or the `cmd`  prompt in case of Windows, navigate to the directory where your python scripts (`.py` files) are saved, and execute the scripts right from the command-line as follows.

```
$ python hellosourav.py
Hello Sourav!
```

We will later talk more about command-line executions, especially on passing command-line argument(s) to a program while executing it, and how to parse them within the code.


#### Integrated Development Environment (IDE)

IDEs are probably the most convenient way to edit, test, debug and run your python code. Every modern IDE will have an option for you to navigate to the directory where the `.py` files (scripts) are saved, and open any `.py` file (script) for editing within the IDE. The IDE will generally offer you a `run` option for the Python script that you opened for editing. You may have to choose the right IDE and configure it a little to suit your workflow. Try the following IDEs, and then choose the one you like. I like [VS Code](https://code.visualstudio.com/).

- PyCharm : https://www.jetbrains.com/pycharm/ : Really easy to use, quite powerful, but targeted only at Python      
- Visual Studio Code : https://code.visualstudio.com/ : Really powerful, hugely customizable, for all languages       
- Sublime Text : https://www.sublimetext.com/ : Really powerful, hugely customizable, again, for all languages    

---

**License Declaration** : Following the lead from the inspirations for this material, and the *spirit* of Python education and development, all modules of this work are licensed under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
