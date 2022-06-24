PI = 3.141592

class Math:
    def solve(self, r): # self는 무조건 들어가야한다 math에 속한다는것을 의미
        return PI * (r**2)
    def sum(self, a, b):
        return a + b

if __name__ == "__main__":  # 메인
    print(PI)
    a = Math()
    print(a.solve(2))
    print(a.sum(PI, 4.4))