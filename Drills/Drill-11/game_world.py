
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]] #게임 월드에 담겨있는 모든 객체들을
#담고 있는 리스트
#Drawing Layer에 따라서 분류


def add_object(o, layer):
    objects[layer].append(o)  #게임 월드에 객체 추가


def remove_object(o): # 게임 월드에서 객체 제거
    for i in range(len(objects)):
        if o in objects[i]: # for 문 돌려서 제거
            objects[i].remove(o)
            del o


def clear(): #게임 월드의 모든 객체 제거
    for o in all_objects():
        del o
    objects.clear()


def all_objects(): #게임 월드의 모든 객체들을 하나씩 꺼내오기
    for i in range(len(objects)):
        for o in objects[i]:
            yield o # yield 는 수열

