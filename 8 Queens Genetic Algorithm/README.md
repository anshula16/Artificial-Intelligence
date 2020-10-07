# 8 Queens Genetic Algorithm

## Prerequisites
>* [Python3.7 and above](https://www.python.org/)
>* [Anaconda](https://www.anaconda.com/products/individual)
>* Install Dependencies
>   * python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
>   * python -m pip install kivy.deps.gstreamer
>   * python -m pip install kivy.deps.angle 
>* Install Kivy
>   * python -m pip install kivy

## How to use?
Run [EightQueens.py](EightQueens.py)

## Modules
>- #### [BoardPosition.py](BoardPosition.py) : Class for different board positions.
>      > - [X] Sequence of positions of the queens
>      > - [X] Corresponding fitness value
>      > - [X] Corresponding survival value
>- #### [GeneticAlgorithm.py](GeneticAlgorithm.py) :
>      > - [X] Generates population
>      > - [X] Select parents from the population randomly
>      > - [X] Does a crossover of the parents to produce a child.
>      > - [X] Mutation of child is done, depending of the MUTATE_FLAG
>      > - [X] Calculates the fitness value of the child
>      > - [X] Add the child to the new population
>- #### [EightQueen.py](EightQueen.py) :
>      > - [X] Defines GUI which contains an 8x8 board, button to start genetic algorithm, a text box to input population size, and the number of the iteration when the solution was found.
>      > - [X] Clears board before starting the algorithm
