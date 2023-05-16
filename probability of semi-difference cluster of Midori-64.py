import numpy as np
import math
from numpy import *
DDT = array([
    [1.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.125, 0.250, 0.000, 0.125, 0.125, 0.125, 0.000, 0.125, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.000],
    [0.000, 0.250, 0.000, 0.000, 0.250, 0.000, 0.000, 0.000, 0.000, 0.250, 0.000, 0.000, 0.250, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.125, 0.000, 0.250, 0.125, 0.125, 0.125, 0.000, 0.000, 0.000, 0.125, 0.000, 0.125],
    [0.000, 0.125, 0.250, 0.125, 0.125, 0.125, 0.000, 0.000, 0.125, 0.000, 0.000, 0.125, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.125, 0.000, 0.000, 0.125, 0.000, 0.000, 0.250, 0.000, 0.125, 0.250, 0.000, 0.125, 0.000, 0.000, 0.000],
    [0.000, 0.125, 0.000, 0.250, 0.000, 0.000, 0.000, 0.125, 0.125, 0.000, 0.000, 0.000, 0.125, 0.125, 0.000, 0.125],
    [0.000, 0.000, 0.000, 0.125, 0.000, 0.250, 0.125, 0.000, 0.000, 0.000, 0.000, 0.125, 0.000, 0.250, 0.125, 0.000],
    [0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.125, 0.000, 0.000, 0.125, 0.000, 0.125, 0.125, 0.000, 0.125, 0.000],
    [0.000, 0.000, 0.250, 0.125, 0.000, 0.125, 0.000, 0.000, 0.125, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.250, 0.000, 0.000, 0.000, 0.000, 0.250, 0.000, 0.000, 0.250, 0.000, 0.250],
    [0.000, 0.000, 0.000, 0.000, 0.125, 0.000, 0.000, 0.125, 0.125, 0.125, 0.000, 0.250, 0.000, 0.125, 0.000, 0.125],
    [0.000, 0.000, 0.250, 0.000, 0.000, 0.125, 0.125, 0.000, 0.125, 0.125, 0.000, 0.000, 0.125, 0.000, 0.125, 0.000],
    [0.000, 0.000, 0.000, 0.125, 0.000, 0.000, 0.125, 0.250, 0.000, 0.000, 0.250, 0.125, 0.000, 0.000, 0.125, 0.000],
    [0.000, 0.125, 0.000, 0.000, 0.000, 0.000, 0.000, 0.125, 0.125, 0.000, 0.000, 0.000, 0.125, 0.125, 0.250, 0.125],
    [0.000, 0.000, 0.000, 0.125, 0.000, 0.000, 0.125, 0.000, 0.000, 0.000, 0.250, 0.125, 0.000, 0.000, 0.125, 0.250]])


for input in range(15):
    for output in range(15):
        print("input difference of active S-boxes = ", input + 1)
        print("output difference of active S-boxes = ", output + 1)
        round_one = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        round_two = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        round_three = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        round_four = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        round_five = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        round_six = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        round_seven = np.zeros((2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 1))
        Pr = 0
        print("0x", input+1)
        for i in range(16):
            for j in range(16):
                round_one[i][j][i][j][0] = round_one[i][j][i][j][0] + DDT[input + 1][i]*DDT[input + 1][j]*DDT[input + 1][i]*DDT[input+1][j]
        print(1)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    if DDT[s][i] != 0 and DDT[s][j] != 0:
                        for t in range(16):
                            round_two[i][j][j][i][0] = round_two[i][j][j][i][0] + round_one[s][t][s][t][0]*DDT[t][i]*DDT[s][j]*DDT[t][j]*DDT[s][i]
        print(2)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        for m in range(16):
                            if DDT[m][s] != 0 and DDT[m][j] != 0:
                                for n in range(16):
                                    round_three[i][j][s][t][0] = round_three[i][j][s][t][0] + round_two[m][n][n][m][0]*DDT[n][i]*DDT[m][j]*DDT[m][s]*DDT[n][t]
        print(3)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        for m in range(16):
                            if DDT[m][t] != 0 and DDT[m][j] != 0 and DDT[m][s] != 0:
                                for n in range(16):
                                    if DDT[n][t] != 0 and DDT[n][j] != 0 and DDT[n][i] != 0:
                                        for p in range(16):
                                            if DDT[p][t] != 0 and DDT[p][s] != 0 and DDT[p][i] != 0:
                                                for q in range(16):
                                                    round_four[i][j][s][t][0] = round_four[i][j][s][t][0] + round_three[m][n][p][q][0]*DDT[n][i]*DDT[q][j]*DDT[p][s]*DDT[m][t]*DDT[n][j]*DDT[q][i]*DDT[p][t]*DDT[m][s]*DDT[p][i]*DDT[m][j]*DDT[n][t]*DDT[q][s]
        print(4)

        for m in range(16):
            for n in range(16):
                for i in range(16):
                    if DDT[i][m] != 0:
                        for j in range(16):
                            if DDT[j][m] != 0:
                                for s in range(16):
                                    if DDT[s][n] != 0:
                                        for t in range(16):
                                            round_five[m][n][m][n][0] = round_five[m][n][m][n][0] + round_four[i][j][s][t][0]*DDT[j][m]*DDT[s][n]*DDT[i][m]*DDT[t][n]
        print(5)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    if DDT[s][j] != 0 and DDT[s][i] != 0:
                        for t in range(16):
                            round_six[i][j][j][i][0] = round_six[i][j][j][i][0] + round_five[s][t][s][t][0]*DDT[t][i]*DDT[s][j]*DDT[t][j]*DDT[s][i]
        print(6)

        for i in range(16):
            for j in range(16):
                Pr = Pr + round_six[i][j][j][i][0]*(DDT[i][output + 1]**2)*(DDT[j][output + 1]**2)
        print(7)

        '''    for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        for m in range(16):
                            if DDT[m][s] != 0 and DDT[m][j] != 0:
                                for n in range(16):
                                    round_seven[i][j][s][t][0] = round_seven[i][j][s][t][0] + round_six[m][n][n][m][0]*DDT[n][i]*DDT[m][j]*DDT[m][s]*DDT[n][t]
        print(7)
    
        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        Pr = Pr + round_seven[i][j][s][t][0]*(DDT[i][output + 1]**3)*(DDT[j][output + 1]**3)*(DDT[s][output + 1]**3)*(DDT[t][output + 1]**3)
        print(8)'''


        if Pr != 0:
            count = math.log(Pr, 2)
        else:
            count = Pr
        print(count)
        print("\n\n")
