## File to handle send & pull req from theblueallience.com
from ast import Str
from xmlrpc.client import DateTime
import requests
from datetime import date, datetime
import time

from constants import _TBAKEY , _TEAMKEY

MatchNum = 0

def getReq(key,link):
    headers = {
        "accept":"application/json",
        "X-TBA-Auth-Key":key
    }
    req = requests.get("https://www.thebluealliance.com/api/v3"+link, headers=headers)
    if req.status_code == 200:
        return req.json()
    else: return None

class TBAAPI:
    def __init__(self):
        self.key = _TBAKEY
        curEvent = getReq(self.key,"/team/" + _TEAMKEY + "/events/" + str(datetime.now().year) + "/simple")
        #print(curEvent)
        match = {}
        for teamdata in curEvent:
            #print("\n\n")
            #print(teamdata["start_date"])

            start = datetime.strptime(teamdata["start_date"], '%Y-%m-%d')
            end = datetime.strptime(teamdata["end_date"], '%Y-%m-%d')
            if start <= datetime.strptime(teamdata["end_date"], '%Y-%m-%d') <= end:
                match = teamdata
                print(teamdata["name"] + " Works!")
                break
            else: print(teamdata["name"] + " N/A")
        
        print(match)
        self.match = match

    def getEventMatches(self):
        if self.match == {}: return
        matchData = getReq(self.key,"/event/" + self.match["key"] + "/matches/simple")
        return matchData

    def getCurMatch(self):
        ms = round(time.time() * 1000)
        matches = sorted(self.getEventMatches(), key=lambda d: d['match_number']) 
        for match in matches:
            t = (match["actual_time"] - ms)
            print(str(match["match_number"]) + " has started? : " + str(t))
            if(t <= 250):
                global MatchNum
                MatchNum = match["match_number"]



api = TBAAPI()
api.getCurMatch()
print(MatchNum)