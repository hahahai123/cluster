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
        round_minone = np.zeros((2**4, 2**4, 2**4, 2**4, 2**4, 2**4, 2**4, 1))
        round_zero = np.zeros((2**4, 2**4, 2**4, 2**4, 2**4, 1))
        round_one = np.zeros((2**4, 2**4, 2**4, 1))
        round_two = np.zeros((2**4, 2**4, 2**4, 1))
        round_three = np.zeros((2**4, 2**4, 2**4, 2**4, 1))
        round_four = np.zeros((2**4, 2**4, 2**4, 2**4, 2**4, 1))
        round_five = np.zeros((2**4, 2**4, 2**4, 1))
        round_six = np.zeros((2**4, 2**4, 2**4, 1))
        round_seven = np.zeros((2**4, 2**4, 2**4, 2**4, 2**4, 1))
        round_eight = np.zeros((2**4, 2**4, 2**4, 2**4, 1))
        round_nine = np.zeros((2**4, 2**4, 2**4, 1))
        round_ten = np.zeros((2**4, 2**4, 2**4, 1))
        round_eleven = np.zeros((2**4, 2**4, 2**4, 2**4, 2**4, 1))
        Pr = 0

        '''for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        round_minone[i][j][s][t][j][s][t][0] = round_minone[i][j][s][t][j][s][t][0] + DDT[input+1][i]*DDT[input+1][j]*DDT[input+1][s]*DDT[input+1][t]*DDT[input+1][j]*DDT[input+1][s]*DDT[input+1][t]
        print(-1)
        
        for i in range(16):
            for j in range(16):
                for n in range(16):
                    if DDT[n][i] != 0 and DDT[n][j] != 0:
                        for t in range(16):
                            if DDT[t][j] != 0:
                                for m in range(16):
                                    if DDT[m][i] != 0:
                                        for s in range(16):
                                            round_zero[i][j][i][j][i][0] = round_zero[i][j][i][j][i][0] + round_minone[s][t][m][n][t][m][n][0]*DDT[n][i]*DDT[t][j]*DDT[m][i]*DDT[n][j]*DDT[s][i]
        print(0)
    
        for i in range(16):
            for j in range(16):
                round_zero[i][j][i][j][i][0] = round_zero[i][j][i][j][i][0] + (DDT[input+1][i]**3)*(DDT[input+1][j]**2)
        print(0)
    
        for i in range(16):
            for j in range(16):
                for t in range(16):
                    if DDT[t][i] != 0 and DDT[t][j] != 0:
                        for s in range(16):
                            round_one[i][j][i][0] = round_one[i][j][i][0] + round_zero[s][t][s][t][s][0]*DDT[s][i]*DDT[t][j]*DDT[t][i]
        print(1)'''

        for i in range(16):
            for j in range(16):
                round_one[i][j][i][0] = round_one[i][j][j][0] + DDT[input+1][i]*DDT[input+1][i]*DDT[input+1][j]
        print(1)

        for i in range(16):
            for j in range(16):
                for s in range(16):
                    if DDT[s][i] != 0 and DDT[s][j] != 0:
                        for t in range(16):
                            round_two[i][j][i][0] = round_two[i][j][i][0] + round_one[s][t][s][0]*DDT[s][i]*DDT[s][j]*DDT[t][i]
        print(2)

        for i in range(16):
            for j in range(16):
                for k in range(16):
                    for s in range(16):
                        if DDT[s][i] != 0 and DDT[s][k] != 0:
                            for t in range(16):
                                round_three[i][j][k][k][0] = round_three[i][j][k][k][0] + round_two[s][t][s][0]*DDT[s][i]*DDT[t][j]*DDT[s][k]*DDT[t][k]
        print(3)

        for i in range(16):
            for j in range(16):
                for t in range(16):
                    if DDT[t][i] != 0 and DDT[t][j] != 0:
                        for s in range(16):
                            for k in range(16):
                                round_four[i][j][j][i][j][0] = round_four[i][j][j][i][j][0] + round_three[k][s][t][t][0]*DDT[t][i]*DDT[t][j]*DDT[t][j]*DDT[s][i]*DDT[k][j]
        print(4)

        for i in range(16):
            for j in range(16):
                for k in range(16):
                    for t in range(16):
                        if DDT[t][i] != 0 and DDT[t][k] != 0:
                            for s in range(16):
                                round_five[i][j][k][0] = round_five[i][j][k][0] + round_four[s][t][t][s][t][0]*DDT[t][i]*DDT[s][j]*DDT[t][k]
        print(5)

        for i in range(16):
            for j in range(16):
                for k in range(16):
                    if DDT[k][i] != 0:
                        for s in range(16):
                            if DDT[s][j] != 0:
                                for t in range(16):
                                    round_six[i][j][i][0] = round_six[i][j][i][0] + round_five[k][s][t][0]*DDT[t][i]*DDT[s][j]*DDT[k][i]
        print(6)

        for i in range(16):
            for j in range(16):
                for k in range(16):
                    for s in range(16):
                        if DDT[s][i] != 0 and DDT[s][k] != 0:
                            for t in range(16):
                                round_seven[i][j][k][k][k][0] = round_seven[i][j][k][k][k][0] + round_six[s][t][s][0]*DDT[s][i]*DDT[t][j]*DDT[s][k]*DDT[s][k]*DDT[t][k]
        print(7)

        for i in range(16):
            for j in range(16):
                for t in range(16):
                    if DDT[t][i] != 0 and DDT[t][j] != 0:
                        for s in range(16):
                            if DDT[s][i] != 0:
                                for k in range(16):
                                    round_eight[i][j][i][j][0] = round_eight[i][j][i][j][0] + round_seven[k][s][t][t][t][0]*DDT[t][i]*DDT[t][j]*DDT[s][i]*DDT[k][j]
        print(8)

        '''for i in range(16):
            for j in range(16):
                Pr = Pr + round_eight[i][j][i][j][0]*DDT[j][output + 1]*DDT[i][output + 1]*DDT[j][output + 1]
        print(9)'''


        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        round_nine[i][j][j][0] = round_nine[i][j][j][0] + round_eight[s][t][s][t][0]*DDT[t][i]*DDT[s][j]*DDT[t][j]
        print(9)

        for i in range(16):
            for j in range(16):
                Pr = Pr + round_nine[i][j][j][0]*DDT[j][output + 1]*DDT[i][output + 1]*DDT[j][output + 1]
        print(10)

        '''for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        round_ten[i][i][j][0] = round_ten[i][i][j][0] + round_nine[s][t][t][0]*DDT[t][i]*DDT[s][i]*DDT[t][j]
        print(10)
    
        for i in range(16):
            for j in range(16):
                Pr = Pr + round_ten[i][i][j][0]*DDT[j][output + 1]*DDT[i][output + 1]*DDT[i][output + 1]*DDT[j][output + 1]*DDT[j][output + 1]
        print(11)
        
        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        for n in range(16):
                            if DDT[n][j] != 0 and DDT[n][t] != 0 and DDT[n][i] != 0:
                                for m in range(16):
                                    round_eleven[i][j][s][t][j][0] = round_eleven[i][j][s][t][i][0] + round_ten[m][m][n][0]*DDT[n][i]*DDT[m][j]*DDT[m][s]*DDT[n][t]*DDT[n][j]
        print(11)
        
        for i in range(16):
            for j in range(16):
                for s in range(16):
                    for t in range(16):
                        Pr = Pr + round_eleven[i][j][s][t][j][0]*DDT[j][output + 1]*DDT[s][output + 1]*DDT[t][output + 1]*DDT[j][output + 1]*DDT[s][output + 1]*DDT[t][output + 1]*DDT[i][output + 1]
        print(12)'''


        if Pr != 0:
            count = math.log(Pr, 2)
        else:
            count = Pr
        print(count)
        print("\n\n")
