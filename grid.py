from blah import *
n, k, char = 5, 5, 'm'  # input().split(' ')

g = grid(int(n), int(k), char)

cb = [0, 0]


cb[1] = cb[1]+1
cb[0] = cb[0]+1

while(True):
    if input() == "yes":
        x, y = cb
        cb[0] = cb[0]+1
        g[x+1][y] = '0'

        # change the array
        # should be +1
        # put dot

        # move dot left

        # print error if move dot too far

        # g[middle_n]
        pprintGrid(g)
