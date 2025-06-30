import pandas as pd

def updateScore(score):
    if score >= 80:
        return score + 5
    elif score < 70:
        return score + (10 if score < 75 else 5)
    elif score < 60:
        return score + (10 if score < 65 else 5)
    elif score < 50:
        return score + (10 if score < 75 else 5)
    else:
        return score + (20.25 if score < 65 else 17.1)
    
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    else:
        return "D"
    
score = pd.read_excel("filexlsx/data-score.xlsx", sheet_name="TI24E")
score["New Score"] = score["Score"].apply(updateScore)
score["Grade"] = score["New Score"].apply(grade)
score.to_excel("filexlsx/data-score-updated.xlsx", index=False)