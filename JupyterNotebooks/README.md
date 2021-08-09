# Python Notebooks

**Learn how to work with the vibrant Python Notebooks.**

This repository houses a set of Python 3.8 Chapters written in the beautifully simple IDE Jupyter Notebook. You may either use the Jupyter Notebook interface or Google Colab to view, edit and execute these notebooks. As Notebooks are rendered in the browser as web applications, they can support a wide range of frontend elements, including cells (code and markdown), graphics, animation and interactivity. This makes the Python Notebook a much more interesting platform to learn python than the other IDEs.

## Jupyter Notebooks

Jupyter initializes a local server running python at the backend (on your own computer), and renders the frontend through a Notebook environment at `localhost:8888`. Keep the backend server (generally runs on your terminal for Linux/Mac or Anaconda Prompt for Windows) running so that the frontend notebook interface can access Python.

#### Installing Jupyter

In terms of this course, the easiest way to install Python 3.8, Jupyter, and all relevant packages for computation is to install the entire [Anaconda platform for Python 3.8](https://www.anaconda.com/products/individual). Once you have installed Anaconda, you will find Jupyter installed within the platform.

- In Linux/Mac, open `terminal` and type `jupyter notebook` to access the platform.
- In Windows, you may simply search-and-click *Jupyter Notebook* in your standard applications, or open the *Anaconda Prompt* and type `jupyter notebook` to begin.

> In case installing Anaconda is too heavy for you, and you already know how to manage `conda` environments and packages, you may also download and install MiniConda (https://docs.conda.io/en/latest/miniconda.html). It's much lighter in footprint, but you will have to install all required data science packages individually, through `conda`.

#### Using the Notebooks

You may download the Notebooks (Chapters) posted in this repository (or `git clone` the entire repository), store them in a dedicated folder on your computer, access the folder through Jupyter Notebook navigation tree, and open the Notebooks individually. Get yourself familiar with the Jupyter Notebook environment, and the basic Python syntax in [Chapter 0](Chapter0_TheNotebook.ipynb). Then, feel free to explore the rest of the Chapters in sequence.

> [Chapter 0](Chapter0_TheNotebook.ipynb) : Python in Jupyter Notebook   
> [Chapter 1](Chapter1_DataTypes.ipynb) : Basic Data Types in Python  
> [Chapter 2](Chapter2_DataStructures.ipynb) : Data Structures in Python   
> [Chapter 3](Chapter3_ConditionLoop.ipynb) : Conditions and Loops in Python   
> [Chapter 4](Chapter4_Functions.ipynb) : Functions and Chapters in Python   
> [Chapter 5](Chapter5_PythonComputing.ipynb) : Computing with Python   
> [Chapter 6](Chapter6_DataHandling.ipynb) : Data Handling with Python   
> [Chapter 7](Chapter7_BasicDataScience.ipynb) : Basic Data Science in Python   
> [Chapter 8](Chapter8_ObjectOrientedPython.ipynb) : Classes and Objects in Python   
> [Chapter X](ChapterX_MiscellaneousTopics.ipynb) : Miscellaneous Topics in Python     


## Google Colaboratory

Google Colab offers a wonderful cloud platform to host, edit, run and share your Python Notebooks. The look and feel is similar to Jupyter Notebooks, and you can use the same Notebooks on both the platforms. In case you do not want to install Anaconda on your computer, but still want to access all data science packages, Google Colab comes with almost all of them pre-installed. In addition, it offers you free (but limited) access to GPUs for high-performance computing requirements. You must check it out!

> Visit the [Google Colaboratory](https://colab.research.google.com/) website, and start exploring on your own.

---

**License Declaration** : Following the lead from the inspirations for this material, and the *spirit* of Python education and development, all Chapters of this work are licensed under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
