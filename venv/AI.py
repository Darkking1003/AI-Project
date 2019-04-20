
import time
import logic

stack=[]

Commands={"L":logic.left,"R":logic.right,"U":logic.up,"D":logic.down}
DepthLimit=5

def Next_step(mat):

    Score=Search(mat,"L")
    print(Score)
    return "Up"


def Search(mat,Path):
    Direction=Path[-1]
    MaxScore=-1
    new_Matrix,done=Commands[Direction](mat)
    if len(Path)==DepthLimit:
        return FindScore(new_Matrix)
    if done:
        nPath=Path+"L"
        Score=Search(new_Matrix,Path)
        if Score>MaxScore:
            MaxScore=Score
        nPath=Path+"R"
        Score = Search(new_Matrix, Path)
        if Score > MaxScore:
            MaxScore = Score
        nPath = Path + "U"
        Score = Search(new_Matrix, Path)
        if Score > MaxScore:
            MaxScore = Score
        nPath = Path + "D"
        Score = Search(new_Matrix, Path)
        if Score > MaxScore:
            MaxScore = Score
        return MaxScore



def FindScore(mat):
    return 1000















