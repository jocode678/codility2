# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")


# Successful answer in Codility:


def solution(N):
    # write your code in Python 3.6
    for i in range(1,(N + 1)):
        # divisble by 2 and 3 and 5
        if i%2 == 0 and i%3 == 0 and i%5 == 0:
            print('CodilityTestCoders')
        elif i%2 == 0 and i%3 == 0:
            print('CodilityTest')
        elif i%3 == 0 and i%5 == 0:
            print('TestCoders')
        elif i % 2 == 0 and i % 5 == 0:
            print('CodilityCoders')
        # if divisible by 2
        elif i%2 == 0:
            print('Codility')
        # if divisble by 3
        elif i%3 == 0:
            print('Test')
        # if divisble by 5
        elif i%5 == 0:
            print('Coders')
        else:
            print(i)

# Don't paste these parts into Codility!
N = 24
solution(N)

# Other attempts:
# def solution(N):
#     # write your code in Python 3.6
#     start = 1
#     end = N + 1
#     for i in range(start,end):
#         # divisble by 2 and 3 and 5
#         if i%2 == 0 and i%3 == 0 and i%5 == 0:
#             print('CodilityTestCoders')
#         elif i%2 == 0 and i%3 == 0:
#             print('CodilityTest')
#         elif i%3 == 0 and i%5 == 0:
#             print('TestCoders')
#         elif i % 2 == 0 and i % 5 == 0:
#             print('CodilityCoders')
#         # if divisible by 2
#         elif i%2 == 0:
#             print('Codility')
#         # if divisble by 3
#         elif i%3 == 0:
#             print('Test')
#         # if divisble by 5
#         elif i%5 == 0:
#             print('Coders')
#         else:
#             print(i)
#


#
# Other attempt started using lists:
# def solution(N):
#     list = []
#     for i in range(1, (N + 1)):
#         if i%2 == 0 and i%3 == 0 and i%5 == 0:
#             list.append('Codility')
#         elif i%2 == 0 and i%3 == 0:
#             list.append('CodilityTest')
#         elif i%3 == 0 and i%5 == 0:
#             list.append('TestCoders')
#         elif i % 2 == 0 and i % 5 == 0:
#             list.append('CodilityCoders')
#         # if divisible by 2
#         elif i%2 == 0:
#             list.append('Codility')
#         # if divisble by 3
#         elif i%3 == 0:
#             list.append('Test')
#         # if divisble by 5
#         elif i%5 == 0:
#             list.append('Coders')
#         else:
#             list.append(i)
#         return list
#
#
# N = 24
# print(solution(N))
