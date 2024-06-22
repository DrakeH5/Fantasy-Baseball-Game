'''from pybaseball import  playerid_lookup
from pybaseball import  statcast_pitcher
from pybaseball import statcast_batter

playerInfo = playerid_lookup('greinke', 'zack')
print(playerInfo["key_mlbam"][0])
kershaw_stats = statcast_pitcher('2008-04-01', '2017-07-15', playerInfo["key_mlbam"][0])
print(kershaw_stats)'''