import kivy.app
import kivy.uix.gridlayout
import kivy.uix.boxlayout
import kivy.uix.button
import kivy.uix.textinput
import kivy.uix.label
import numpy as np
from kivy.config import Config
import GeneticAlgorithm as ga

class EightQueens(kivy.app.App):

    def build(self):
        '''
        Define the GUI which contains:
        - a 8x8 chessboard
        - a button to start the genetic algorithm
        - a text to input the initial population size
        - display the iteration number in which solution was found.
        '''

        boxLayout = kivy.uix.boxlayout.BoxLayout(orientation = "vertical")
        
        gridLayout = kivy.uix.gridlayout.GridLayout(rows = 8, size_hint_y = 9)
        boxLayout_buttons = kivy.uix.boxlayout.BoxLayout(orientation = "horizontal")

        boxLayout.add_widget(gridLayout)
        boxLayout.add_widget(boxLayout_buttons)

        # "O" as dtype means it is an object type.
        self.all_widgets = np.zeros(shape = (8, 8), dtype = "O")

        color1 = (0.863, 0.863, 0.863, 0.863)
        color2 = (1, 1, 1, 1)

        # 8x8 board
        for row_idx in range(self.all_widgets.shape[0]):
            
            color1, color2 = color2, color1
            for col_idx in range(self.all_widgets.shape[1]):

                if col_idx % 2 == 0:
                    color = color1
                else:
                    color = color2

                self.all_widgets[row_idx, col_idx] = kivy.uix.button.Button(font_size = 25, background_normal = '', background_color = color)
                gridLayout.add_widget(self.all_widgets[row_idx, col_idx])
        
        # to start genetic algorithm
        start_ga_button = kivy.uix.button.Button(text = "Start GA", font_size = 15, size_hint_x = 2)
        start_ga_button.bind(on_press = self.start)     # on pressing, start function defined below is called.
        boxLayout_buttons.add_widget(start_ga_button)

        # user input for number of population initially, by default it is 10000
        self.population_size = kivy.uix.textinput.TextInput(text="10000", font_size=20, size_hint_x=1)
        boxLayout_buttons.add_widget(self.population_size)


        # display the iteration number in which the solution was found. 
        self.iteration_num_fitness_val = kivy.uix.label.Label(text = "Iteration No./Fitness Value", font_size = 15, size_hint_x = 2)
        boxLayout_buttons.add_widget(self.iteration_num_fitness_val)

        return boxLayout

    def clearBoard(self):
        '''
        Before starting to find the solution, the board is cleared.
        '''

        for row_idx in range(self.all_widgets.shape[0]):
            for col_idx in range(self.all_widgets.shape[1]):

                self.all_widgets[row_idx, col_idx].text = ""
        self.iteration_num_fitness_val.text = "Iteration No./Fitness Value"

    def start(self, *args):
        '''
        Called on clicking the start genetic algorithm button.
        '''

        self.clearBoard()

        try:
            population_size = int(self.population_size.text)
            if population_size < 2:
                population_size = 100
        except:     # when the text is not an integer.
            population_size = 100
            
        population = ga.generatePopulation(population_size)

        iteration = 0
        while not ga.stop(population, iteration):

            # keep iterating till you find the best position
            if iteration % 100 == 0:
                print("  " * 10 ,"Executing Genetic  generation : ", iteration)
            population = ga.geneticAlgorithm(population)
            iteration +=1 
        
        flag = False
        # If a solution is found, display just one solution.
        for each in population:
            if not flag:
                if each.fitness == 28:
                    print(each.fitness, ga.calculateFitness(each.sequence_of_queens))
                    for row_idx in range(0, 8):
                        col_idx = each.sequence_of_queens[row_idx]
                        self.all_widgets[row_idx, col_idx].text = "Q"
                        self.all_widgets[row_idx, col_idx].color = (0, 0, 0, 1)
            
                    print(each.sequence_of_queens)
                    self.iteration_num_fitness_val.text = "Iteration : " + str(iteration) + " Fitness : " + str(each.fitness)
                    flag = True

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')

eightQueens = EightQueens()
eightQueens.run()
