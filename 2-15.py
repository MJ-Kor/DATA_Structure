def reverse(remsg):
    alp = list(remsg)
    alp.reverse()
    print("".join(alp))


msg = input("문자열을 입력하세요 : ")
reverse(msg)
