# 파이썬 리스트로 구현한 자료구조 리스트 ADT
                                                    # 1. list()
items = []
                                                    # 2. insert(pos, e)
def Insert(pos, e):
    items.insert(pos, e)
                                                    # 3. delete(pos)
def Delete(pos):
    return items.pop(pos)
                                                    # 4. isEmpty()
def IsEmpty():
    if len(items) == 0:
        return True
    else:
        return False
                                                    # 5. getEntry(pos)
def GetEntry(pos):
    return items[pos]
                                                    # 6. size()
def Size():
    return len(items)
                                                    # 7. clear()
def Clear():
    items.clear()
    # 아니면
    # global items
    # items=[]
                                                    # 8. find(item)
def Find(item):
    return items.index(item)
                                                    # 9. replace(pos, item)
def Replace(pos, item):
    items[pos]=item
                                                    # 10. sort()
def Sort():
    items.sort()
                                                    # 11. merge(lst)
def Merge(lst):
    items.extend(lst)
                                                    # 12. display()
def Display(msg="ArrayList"):
    print(msg, Size(), items)
                                                    # 13. append(e)
def Append(e):
    items.append(e)

Display('파이썬 리스트로 구현한 리스트 테스트:')
Insert(0,10);Insert(0,20);Insert(1,30);Insert(Size(),40);Insert(2,50)
Display('데이터 삽입x5:')
Sort()
Display('리스트 정렬:')
Replace(2,90)
Display('데이터 변경:')
Delete(2);Delete(Size()-1);Delete(0)
Display('데이터 삭제:')
lst = [1,2,3]
Merge(lst)
Display('리스트 합병:')
Clear()
Display('리스트 정리:')