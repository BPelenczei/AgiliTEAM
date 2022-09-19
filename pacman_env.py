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
        self.step_ = 100
        self.dir = 1
        self.size = 5
        self.last_obs = None
        # placeholder for additional information
        info = None
        self.time_step=40
        # Variables for visualizing the current grid world
        self.show_img_size = 300
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.reset()


    def step(self , action):
        # setting base reward
        score = 0
        # setting basic env status
        done_ = False
        # getting the current head position (always the last body part)
        pos_x, pos_y = self.body[-1]

        #choose action
        if action==0:
            #going right
            x,y = self.right(pos_x,pos_y,action)
        elif action == 1:
            #going up
            x, y = self.up(pos_x, pos_y, action)

        elif action == 2:
            #going left
            x, y = self.left(pos_x, pos_y, action)

        elif action == 3:
            #going down
            x, y = self.down(pos_x, pos_y, action)

        else:
            print("You lose")
            done_ = True
            score= -1

        if (x, y) in self.objects:

            #increment score by eating an object
            self.score += 1
            #if object reached  , remove
            self.objects.remove((x, y))

            # create observation
            obs = self._create_observation()

            # save observation
            self.last_obs = obs

        self.step_ -=1
        if self.step_ == 0:
            done_ = True

        return obs.flatten(), score, done_, info

    def right(self , x,y,action):

        #only the x coordinate changes

        x +=1
        y = y
        return x,y


    def up(self, x,y,action):

        #only the y coordinate changes
        x=x
        y +=1
        return x,y


    def left(self, x,y,action):

        x -= 1
        y = y

        return x,y


    def down(self, x,y,action):

        # only the y coordinate changes
        x = x
        y -= 1

        return x,y


    def _create_observation(self):
        pass


    def reset(self):


        return state


    def render(self):

        self.body = []
        self.objects = []
        self.dir = 1
        self.size = 5
        self.step_ = 0
        self.last_obs = None


        self._create_body()
        self._create_objects(num=10)
        obs_ = self._create_observation()
        return obs_.flatten()

        return obs_.flatten()

    def _create_body(self):
        self.body.append((0, 0))
        self.size = 5
    def _create_observation(self):
        """
        This funtion creates a grayscale observation (image) from the current state of the game.
        :return:
        """
        # init map
        obs_ = np.zeros((self.map_size, self.map_size, 1))

        # add objects
        for obj in self.objects:
            obs_[obj[0], obj[1], 0] = 0.25
        # add snake body
        for piece in self.body:
            obs_[piece[0], piece[1], 0] = 1
        # mark head
        head_coord = self.body[-1]
        obs_[head_coord[0], head_coord[1], 0] = 0.8
        return obs_

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



    print(f" Game over , your score is{env.score}")


