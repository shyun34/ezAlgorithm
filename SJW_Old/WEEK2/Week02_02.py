
def solution(genres, plays):
    # output
    answer = []

    # 장르별 누적 재생횟수를 기록하기 위한 딕셔너리(java에서 map?)
    dic = {}

    # 주어진 list의 index에 따른 장르, 재생홧수를 저장하고 있는 리스트
    album_list = []

    # 장르별 재생횟수 누적 및  list에 album객체 추가
    for i in range(len(genres)):
        # dic.get(genres[i], 0) 여기서 0인자는 무엇일까?  https://wikidocs.net/16#key-valueget
        # 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴         트 값')을 사용하면 편리하다.
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]

        album_list.append(album(genres[i], plays[i], i))

    # 재생횟수 에 따른 장르 정렬? https://wikidocs.net/16#key-value-items
    # Key, Value 쌍 얻기(items)
    # >>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
    # >>> a.items()
    # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
    # items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
    # dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용할 수 있다.
    dic = sorted(dic.items(), key=lambda dic: dic[1], reverse=True)

    # 재생횟수에 따른 album 객체정렬 https://docs.python.org/ko/3/howto/sorting.html
    # 같은지 확인필요 album_list = sorted(album_list, key=lambda album:album[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        # 딕셔너리 pop 불가능 >>> 정렬하고 리스트로 형변환
        play_genre = dic.pop(0)
        #print(play_genre)

        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    #print("answer : ", answer)
    return answer


class album:
    # 생성자
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    # 객체를 만들고 서로의 크기를 비교하려고 할 때 위의 함수들을 구현하면 된다.
    # Java에서 객체를 만들고 Comparable 혹은 Comparator 를 implements 해서 CompareTo 혹은 compare 를 구현하는것과     유사하다.
    # --출처 : https://darkstart.tistory.com/180
    def __lt__(self, other):
        return self.play < other.play

    def __le__(self, other):
        return self.play <= other.play

    def __gt__(self, other):
        return self.play > other.play

    def __ge__(self, other):
        return self.play >= other.play

    def __eq__(self, other):
        return self.play == other.play

    def __ne__(self, other):
        return self.play != other.play

if __name__ == "__main__":
    genres =["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    solution(genres,plays)
