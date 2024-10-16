from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    #Forward if ducks are far enough
    #smaller value so priority is on the others rules
    res[000:250, 000:640] = 0.4
    #Turns right if a duckie is on the left
    res[250:480, 000:280] = 1.0
    #Reverse right wheel to go backward if a duck is in front
    #or to turn left faster
    res[250:480, 280:480] = -1.0
    #Helps turn left if a duck is on the right
    res[250:480, 480:640] = 0.0
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    #Forward if ducks are far enough
    #smaller value so priority is on the others rules
    res[000:250, 000:640] = 0.4
    #Helps turn right if a duck is on the left
    res[250:480, 000:160] = 0.0
    #Reverse right wheel to go backward if a duck is in front
    #or to turn right faster
    res[250:480, 160:360] = -1.0
    #Turns left if a duckie is on the right
    res[250:480, 360:640] = 1.0
    # ---
    return res
