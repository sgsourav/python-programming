# Running Python Scripts

**It's good to run Python from Terminal or IDE too!**

The codes in this directory are standalone scripts written in Python. They have `.py` extension, and can be executed directly from the command-line -- Terminal in Linux/Mac and Command Prompt or Anaconda Prompt in Windows. You may of course choose an Integrated Development Environment (IDE) of your choice to edit and run Python 3 scripts more conveniently.

---

Python has two flavors -- Python 2 and Python 3 -- even in the Command-Line version (or Interpreter). It really depends on which version you have installed on your laptop/desktop. This set of example scripts (`.py` files) should be run using Python 3, either from command-line or through an IDE of your choice. Check the following instructions to know more about it.

#### Running the Scripts from Command-Line

Download the files on your laptop/desktop, open your Terminal (Linux/Mac) or the Command Prompt / Anaconda Prompt (Windows), navigate to the directory where the `.py` files are saved (e.g., `/Users/sourav/Desktop/python-programming-master/dotpyfiles`), and execute the Python 3 scripts using the following command right from the command-line.

`python <filename>.py`   |   e.g., `python checkPassword_v1.py`    

where `<filename>` is the name of the `.py` file, as in the example above.      
You may have to run `python3 <filename>.py` if you also have Python 2.

If you have any command-line argument parsed in your Python 3 code (like `checkPassword_v4.py` in this directory), you will need to pass the command-line argument(s) to your code while running it. You may run the script as follows in such a scenario.

`python <filename>.py --<flag>=<argument>`   |   e.g., `python checkPassword_v4.py --pass=Sourav@NTU`          

where `<filename>` is the name of the `.py` file, `<flag>` is the flag, and `<argument>` is the corresponding argument.


#### Running the Scripts from a standard IDE

Download the files on your laptop/desktop, and open your favorite Python 3 IDE. Every modern IDE will have an option for you to navigate to the directory where the `.py` files are saved (e.g., `/Users/sourav/Desktop/python-programming-master/dotpyfiles`), and open any `.py` file (script) for editing within the IDE. The IDE will generally offer you a `run` option for the Python 3 script that you opened for editing. Try the following IDEs, and then choose the one you like.

> PyCharm : https://www.jetbrains.com/pycharm/ : Really easy to use, quite powerful, but targeted only at Python      
> Visual Studio Code : https://code.visualstudio.com/ : Really powerful, hugely customizable, for all languages       
> Sublime Text : https://www.sublimetext.com/ : Really powerful, hugely customizable, again, for all languages    

---

**License Declaration** : Following the lead from the inspirations for this material, and the *spirit* of Python education and development, all modules of this work are licensed under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
