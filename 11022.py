# A+B - 8

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

t = int(input())  # 먼저 입력 받음

for i in range(1, t + 1):
    n = input().split()  # 그리고 또 입력받은 값을 쪼갠다. 입력된 값이 1 1일 경우, [1,1]이 된다.

    a = int(n[0])  # 쪼갠 값을 정수로 변환하고, 변수 a, b에 각각 넣어준다.
    b = int(n[1])

    sum = a + b
    print("Case #%d: %d + %d = %d" % (i, a, b, sum))