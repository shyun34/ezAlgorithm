import copy

def rDFS(path,tTickets, totalPath):
    totalPath.append(path)

    if len(totalPath) == ticektsLen+1:
        #print("path : ", path)
        #print("tTickets : ", tTickets)
        #print("totalPath : ", totalPath)
        results.append(totalPath)
        return

    for i in range(len(tTickets)):
        if tTickets[i][0] == path:
            tmpTickets = copy.deepcopy(tTickets)
            tmpTickets.remove(tTickets[i])
            tTotalPath = copy.deepcopy(totalPath)
            #print("tmpTickets : ", tmpTickets)
            #print("tTickets[i] : ", tTickets[i])
            #print("tTickets[i][1] : ", tTickets[i][1])
            #print("tTotalPath : ", tTotalPath)
            rDFS(tTickets[i][1],tmpTickets,tTotalPath)

def solution(tickets):
    answer = []

    global results
    global ticektsLen

    results = []
    ticektsLen = len(tickets)

    rDFS("ICN",tickets,[])
    results.sort()

    return results[0]


if __name__ := '__main__':

    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print("answer :",solution(tickets))