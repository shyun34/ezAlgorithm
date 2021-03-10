function solution(tickets) {
    var answer = [];

    let strAirPort = "ICN";  //시작공항

    answer.push(strAirPort);

    while (tickets.length > 0) {
        
        let filteredItems  = tickets.filter(item => item[0] == strAirPort);
        

        filteredItems.sort(function(a, b) { // 오름차순정렬
            return a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0;
        });
        
        let firstItem = [];

        for(let i = 0 ; i <filteredItems.length; i++){
            if(tickets.filter(item => item[0] == filteredItems[i][1]).length > 0 )
            {
             firstItem = filteredItems[i];
             break;
            }
        }

        strAirPort = firstItem[1];
    
        answer.push(strAirPort);
        
        tickets = arrayRemove(tickets, firstItem);
    }


    return answer;
}

function arrayRemove(arr, value) { 
    
    return arr.filter(function(ele){ 
        return ele != value; 
    });
}


solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]);