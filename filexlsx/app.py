import pandas as pd

def updateScore(score):
    newscore = score + 20
    return score + newscore

def grade(score):
    if score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    else:
        return "D"
    
scores = pd.read_excel("filexlsx/data-score.xlsx", "TI24E")
scores["New Score"] = scores["Score"].apply(updateScore)
scores["Grade"] = scores["New Score"].apply(grade)
scores.to_excel("filexlsx/data-score-updated.xlsx", index=False)