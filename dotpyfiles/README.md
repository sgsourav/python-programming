# Running Python Scripts

**It's good to run Python from Terminal or IDE too!**

The codes in this directory are basic standalone scripts written in Python. They have a `.py` extension, and can be executed directly from the Command-Line (Terminal in Linux/Mac or Command Prompt/Anaconda Prompt in Windows) or the Python Interpreter. You may of course choose an Integrated Development Environment (IDE) of your choice to edit and run the scripts more conveniently.

---

Python has two flavors -- Python 2 and Python 3 -- even in the Command-Line version (or Interpreter). It really depends on which version you have installed on your laptop/desktop. This set of example scripts (`.py` files) should be run using Python 3, either from Command-Line (or Interpreter) or through an IDE of your choice. Check the following instructions to know more about it.

#### Running the Scripts from Command-Line

Download the files on your laptop/desktop (download the repository if you wish), open your Terminal (Linux/Mac) or the Anaconda Prompt (Windows), navigate to the directory where the `.py` files are saved (e.g., `/Users/sourav/Desktop/python-programming-master/dotpyfiles`), and execute the Python 3 scripts using the following simple command right from the command-line.

```python <filename>.py```    

where `<filename>` is the name of the `.py` file. You may have to run `python3 <filename>.py` if you also have Python 2.

If you have any command-line argument parsed in your Python 3 code (like `checkPassword_v4.py` in this directory), you will need to pass the command-line argument(s) to your code while running it. You may run the script as follows in such a scenario.

```python <filename>.py --<flag> <argument> --<flag> <argument>```      

where `<filename>` is the name of the `.py` file, `<flag>` are argument markers, and `<argument>` are the command-line arguments.


#### Running the Scripts from a standard IDE

Download the files on your laptop/desktop (download the repository if you wish), and open your favorite Python 3 IDE. Every modern IDE will have an option for you to navigate to the directory where the `.py` files are saved (e.g., `/Users/sourav/Desktop/python-programming-master/dotpyfiles`), and open any `.py` file (script) for editing within the IDE. The IDE will generally offer you a `run` option for the Python 3 script that you opened for editing. Try the following IDEs, and then choose the one you like.

> PyCharm : https://www.jetbrains.com/pycharm/ : Really easy to use, quite powerful, but targeted only at Python      
> Visual Studio Code : https://code.visualstudio.com/ : Really powerful, hugely customizable, for all languages       
> Sublime Text : https://www.sublimetext.com/ : Really powerful, hugely customizable, again, for all languages    

---

**License Declaration** : Following the lead from the inspirations for this material, and the *spirit* of Python education and development, all modules of this work are licensed under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
