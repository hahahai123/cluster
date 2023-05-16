import numpy as np
import math
from numpy import *
DDT = array([
    [1.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.250, 0.250, 0.250, 0.250, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.250, 0.000, 0.250, 0.000, 0.250, 0.250, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125],
    [0.000, 0.000, 0.250, 0.000, 0.000, 0.000, 0.125, 0.125, 0.000, 0.000, 0.000, 0.250, 0.125, 0.125, 0.000, 0.000],
    [0.000, 0.000, 0.250, 0.000, 0.000, 0.000, 0.125, 0.125, 0.000, 0.000, 0.250, 0.000, 0.125, 0.125, 0.000, 0.000],
    [0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.125, 0.125, 0.000, 0.125, 0.000, 0.000, 0.125, 0.125, 0.000],
    [0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.125, 0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.125],
    [0.000, 0.000, 0.000, 0.000, 0.250, 0.250, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125, 0.125, 0.125],
    [0.000, 0.000, 0.000, 0.000, 0.250, 0.250, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125, 0.125, 0.125],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.250, 0.250, 0.000, 0.125, 0.125, 0.125, 0.125, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.250, 0.000, 0.250, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125, 0.125, 0.125],
    [0.000, 0.000, 0.250, 0.000, 0.000, 0.000, 0.125, 0.125, 0.250, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125],
    [0.000, 0.000, 0.250, 0.000, 0.000, 0.000, 0.125, 0.125, 0.000, 0.250, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125],
    [0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.125, 0.000, 0.125, 0.000, 0.125, 0.000, 0.125, 0.125, 0.000],
    [0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.125, 0.125, 0.000, 0.125, 0.000, 0.125, 0.000, 0.000, 0.125]])

for input in range(15):
    for output in range(15):
        print("input difference of active S-boxes = ", input + 1)
        print("output difference of active S-boxes = ", output + 1)
        round_one = np.zeros((2**4, 2**4, 2**4, 2**4, 1))
        round_two = np.zeros((2**4, 2**4, 2**4, 2**4, 1))
        round_three = np.zeros((2**4, 2**4, 1))
        round_four = np.zeros((2**4, 2**4, 1))
        round_five = np.zeros((2**4, 2**4, 1))
        round_six = np.zeros((2**4, 2**4, 1))
        round_seven = np.zeros((2**4, 2**4, 2**4, 2**4, 1))
        Pr = 0
        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        round_one[i][j][s][t][0] = round_one[i][j][s][t][0] + (DDT[input + 1][i]**3)*DDT[input + 1][j]*(DDT[input + 1][s]**3)*(DDT[input + 1][t]**3)
        print(1)

        for i in range(16):
            for j in range(16):
                for s in range(4):
                    for t in range(4):
                        for m in range(4):
                            for n in range(4):
                                round_two[i][i][j][i][0] = round_two[i][i][j][i][0] + round_one[s+8][t+8][m+8][n+8][0]*DDT[s+8][i]*DDT[t+8][i]*DDT[m+8][j]*DDT[n+8][i]
        print(2)

        for i in range(16):
            for s in range(16):
                for t in range(16):
                    round_three[i][i][0] = round_three[i][i][0] + round_two[s][s][t][s][0]*DDT[t][i]*DDT[s][i]
        print(3)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    round_four[i][j][0] = round_four[i][j][0] + round_three[s][s][0]*DDT[s][i]*DDT[s][j]
        print(4)

        for i in range(16):
            for s in range(16):
                for t in range(16):
                    round_five[i][i][0] = round_five[i][i][0] + round_four[s][t][0]*DDT[s][i]*DDT[t][i]
        print(5)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    round_six[i][j][0] = round_six[i][j][0] + round_five[s][s][0]*DDT[s][i]*DDT[s][j]
        print(6)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        for m in range(16):
                            if DDT[m][i] != 0 and DDT[m][j] != 0 and DDT[m][t] != 0:
                                for n in range(16):
                                    round_seven[i][j][s][t][0] = round_seven[i][j][s][t][0] + round_six[m][n][0]*DDT[m][i]*DDT[m][j]*DDT[n][s]*DDT[m][t]
        print(7)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        Pr = Pr + round_seven[i][j][s][t][0]*(DDT[i][output + 1]**3)*(DDT[j][output + 1]**3)*(DDT[s][output + 1]**3)*DDT[t][output + 1]
        print(8)

        if Pr != 0:
            count = math.log(Pr, 2)
        else:
            count = Pr
        print(count)
        print("\n\n")
