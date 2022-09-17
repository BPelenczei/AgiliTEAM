# Pacman Environment
# Author : Csorba Levente , Knáb István Gellért
#Team : I_NEED_A


#import the needed libraries
import cv2
import numpy as np

class PacMan:
    def __init__(self, map_size):
        self.map_size = map_size
        # lists for the map components
        self.body = []
        self.objects = []
        # initiate default values
        self.step_ = 0
        self.dir = 1
        self.size = 5
        self.last_obs = None
        self.time_step=40
        # Variables for visualizing the current grid world
        self.show_img_size = 300
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.reset()


    def step(self):

        self.time_step -= 1

        if self.time_step == 0:
            done_=True

        return state, reward, done_, info


    def reset(self):


        return state


    def render(self):
        pass


def initialize_parameters():
    global map_size , done_
    map_size = 20
    done_ = False



if __name__ == "__main__":

    #initial parameters
    initialize_parameters()

    #Calling Constructor for the game
    env = PacMan(map_size=map_size)

    #starting state
    state = env.reset()

    #play loop
    while not done_:
        # here are declared the control keys
        print("control assist TODO")

        #add the next action
        action = int(input("Next action:\n"))

        #gym compatible return of step
        state, reward, done_, info = env.step(action=action)

        #visualization of the game
        env.render()






