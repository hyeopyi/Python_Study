def sum(a, b):
    if type(a) != type(b):
        print("더하기를 할 수 없습니다.")
        return
    else:
        return a + b

if __name__ == "__main__": # 파이썬으로만 실행하고자 할때 메인추가
    print(sum(10, 20))