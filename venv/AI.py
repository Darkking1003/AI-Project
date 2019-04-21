import time
import logic
import numpy as np

stack = []

Commands = {"L": logic.left, "R": logic.right, "U": logic.up, "D": logic.down}
DepthLimit = 3


def Next_step(mat):
    MaxScore = -2

    Score = Search(mat.copy(), "L")
    print("Left Score: ", Score)
    if Score > MaxScore:
        MaxScore = Score
        Max_Direction = "Left"
    Score = Search(mat.copy(), "D")
    print("Down Score: ", Score)
    if Score > MaxScore:
        MaxScore = Score
        Max_Direction = "Down"

    Score = Search(mat.copy(), "U")
    print("Up Score: ", Score)
    if Score > MaxScore:
        MaxScore = Score
        Max_Direction = "Up"
    if MaxScore < 0:
        Score = Search(mat.copy(), "R")
        print("Right Score: ", Score)
        if Score > MaxScore:
            MaxScore = Score
            Max_Direction = "Right"

    return Max_Direction


def Search(mat, Path):
    Direction = Path[-1]
    MaxScore = -1
    ScoreL = 0
    ScoreR = 0
    ScoreU = 0
    ScoreD = 0
    Count = 0
    new_Matrix, done = Commands[Direction](mat)
    if len(Path) == DepthLimit:
        if done:
            return FindScore(new_Matrix)
        else:
            return -1
    if done:
        for i in range(4):
            for j in range(4):
                if new_Matrix[i][j] == 0:
                    Count += 1
                    tmpmat = new_Matrix.copy()
                    tmpmat[i][j] = 2

                    nPath = Path + "L"
                    ScoreL += Search(tmpmat, nPath)

                    nPath = Path + "R"
                    ScoreR += Search(tmpmat, nPath)

                    nPath = Path + "U"
                    ScoreU += Search(tmpmat, nPath)

                    nPath = Path + "D"
                    ScoreD += Search(tmpmat, nPath)

    else:
        if (len(Path) == 1):
            return -2
    MaxScore = ScoreL
    if ScoreD > MaxScore:
        MaxScore = ScoreD
    if ScoreR > MaxScore:
        MaxScore = ScoreR
    if ScoreU > MaxScore:
        MaxScore = ScoreU
    if Count != 0:
        return MaxScore / Count
    else:
        return MaxScore


def FindScore(mat):
    reward = [[256, 16, 0.1, -1], [1024, 4, 0.125, -1], [4096, 1, 2, -1], [16384, 0.5, 0.25, -1]]
    Score = 0

    for i in range(4):
        Score += np.multiply(reward[i], mat[i])

    Score = sum(Score)

    return Score

