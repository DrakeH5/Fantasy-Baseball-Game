import random

def battlePredictor(fastballChance, curveballChance,
                    batterOddsSwingAtFastball, batterOddsSwingAtCurveball,
                    batterOddsHitFastball, batterOddsHitCurveball):
    pitcheOptions = ['fastball', "curveball"]
    pitchOrder = random.choices(pitcheOptions, weights=(fastballChance, curveballChance), k=6)
    count = [0, 0]
    run = False
    for i in pitchOrder:
        if(count[0] < 4 and count [1] < 3 and not run):
            if(i == "fastball"):
                if batterOddsSwingAtFastball <= random.random():
                    if batterOddsSwingAtFastball <= random.random():
                        run = True
                    else:
                        count[1]+=1
                else:
                    count[1]+=1
            elif(i == "curveball"):
                if batterOddsSwingAtCurveball <= random.random():
                    if batterOddsSwingAtCurveball <= random.random():
                        run = True
                    else:
                        count[1]+=1
                else:
                    count[1]+=1
    print(count, run)



battlePredictor(0.5, 0.3, 0.4, 0.4, 0.6, 0.2)