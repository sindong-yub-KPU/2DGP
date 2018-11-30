
# 레이어 0 : 배경
# 레이어 1 : 앞에 오브젝트
objects = [[],[]]


def add_object(o,  layer):
    objects[layer].append(o)



def remove_object(o):
    for i in range(len(objects) -1,0,-1):
        if o in objects[i]:

            objects[i].remove(o) #그룹에서 뻄

            del o                   #메모리에서삭제
# 정확한 리스트의 개수 리스트를 몇 개 추가해도 상관없게


def clear():
    for o in all_objects():
        del o
    objects.clear()
    #다 삭제하는 함수

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o
            #모든 오브젝트를 꺼내어본다.