
import time
import logic

stack=[]

Commands={"L":logic.left,"R":logic.right,"U":logic.up,"D":logic.down}
DepthLimit=5

def Next_step(mat):
    MaxScore=-1

    Score=Search(mat,"L")
    print("Left Score: ",Score)
    if Score>MaxScore:
        MaxScore=Score
        Max_Direction="Left"
    Score = Search(mat, "R")
    print("Right Score: ", Score)
    if Score > MaxScore:
        MaxScore = Score
        Max_Direction = "Right"
    Score = Search(mat, "U")
    print("Up Score: ", Score)
    if Score > MaxScore:
        MaxScore = Score
        Max_Direction = "Up"
    Score = Search(mat, "D")
    print("Down Score: ", Score)
    if Score > MaxScore:
        MaxScore = Score
        Max_Direction = "Down"

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
    return 1000















