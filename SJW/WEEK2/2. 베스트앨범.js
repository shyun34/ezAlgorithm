function solution(genres, plays) {
    var answer = [];

    let albumMap = [];
    
    for(let i = 0 ; i < genres.length;i++){
        albumMap.push({     //장르, 재생횟수, 고유번호 순으로 객체 생성
            genre : genres[i],
            play : plays[i],
            num : i
        });
    }

    let groupByGenres = groupBy(albumMap, arr => arr.genre); //장르별로 그룹바이

    
    
    groupByGenres.forEach(Item => {
        
        Item.sort((a, b) => b.play- a.play); //곡수 내림차순 정렬

        if(Item.length > 2){    //2개이상이면 짜르기
            Item.splice(2,Item.length-2);
        }

    });


    groupByGenres.forEach(Item => {
        
       for(let a in Item){
           answer.push(Item[a].num);
       }

    });


    return answer;
}



function groupBy(list, keyGetter) {
    const map = new Map();
    list.forEach((item) => {
         const key = keyGetter(item);
         const collection = map.get(key);
         if (!collection) {
             map.set(key, [item]);
         } else {
             collection.push(item);
         }
    });
    return map;
}

solution(["classic", "pop", "classic", "classic", "pop", "pop"], [500, 600, 150, 800, 2500, 5000]);