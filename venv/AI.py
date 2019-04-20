
import time
import logic
import numpy as np
stack=[]

Commands={"L":logic.left,"R":logic.right,"U":logic.up,"D":logic.down}
DepthLimit=2

def Next_step(mat):
    MaxScore=-1

    Score=Search(mat.copy(),"L")
    print("Left Score: ",Score)
    if Score>MaxScore:
        MaxScore=Score
        Max_Direction="Left"
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
    if MaxScore<0:
        Score = Search(mat.copy(), "R")
        print("Right Score: ", Score)
        if Score > MaxScore:
            MaxScore = Score
            Max_Direction = "Right"



    return Max_Direction


def Search(mat,Path):
    Direction=Path[-1]
    MaxScore=-1
    new_Matrix,done=Commands[Direction](mat)
    if len(Path)==DepthLimit:
        return FindScore(new_Matrix)
    if done:
        nPath=Path+"L"
        Score=Search(new_Matrix,nPath)
        if Score>MaxScore:
            MaxScore=Score
        nPath=Path+"R"
        Score = Search(new_Matrix,nPath)
        if Score > MaxScore:
            MaxScore = Score
        nPath = Path + "U"
        Score = Search(new_Matrix,nPath)
        if Score > MaxScore:
            MaxScore = Score
        nPath = Path + "D"
        Score = Search(new_Matrix,nPath)
        if Score > MaxScore:
            MaxScore = Score
    else:
        if(len(Path)==1):
            return -2
    return MaxScore



def FindScore(mat):
    reward = [[256,16,0.1,-1], [1024,4,0.125,-1], [4096,1,2,-1], [16384,0.5,0.25,-1]]
    Score=0

    for i in range(4):
        Score += np.multiply(reward[i],mat[i])

    Score = sum(Score)

    return Score
















