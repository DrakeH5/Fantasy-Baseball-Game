import numpy as np

def prediction(bat, pit):
    expectedMatchupKPercent = bat * pit / (0.84 * bat * pit + 0.16)
    kPercent = np.exp(.9427*np.log(bat) + .9254*np.log(pit) + 1.5268)
    BBPercent = np.exp(.906*np.log(bat) + .8644*np.log(pit) + 1.9975)	
    FirstBasePercent = np.exp(1.01*np.log(bat) + 1.017*np.log(pit) + 1.943)
    SecondBasePercent = .9206*bat + .95779*pit - .03968
    ThirdBasePercent = np.exp(.8435*np.log(bat) + .8698*np.log(pit) + 3.8809)	
    HomeRunPercent = np.exp(.9576*np.log(bat) + .9268*np.log(pit) + 3.2129)	
    HBPPercent = np.exp(.8761*np.log(bat) + .7623*np.log(pit) + 2.995)	
    BABIP = 1.0403*bat + .9135*pit - .2573

    return [expectedMatchupKPercent, kPercent, BBPercent, FirstBasePercent, SecondBasePercent, ThirdBasePercent, HomeRunPercent, HBPPercent, BABIP]

print(prediction(0.15, 0.30))