T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    copy_passcode = []
    result = []
    for item in passcode:
        copy_passcode.append(item)

    for i in range(N):
        if len(copy_passcode) >= 1 and len(sample) >= 1:
            if copy_passcode[0] != sample[0]:
                sample.pop(0)
            elif copy_passcode[0] == sample[0]:
                sample.pop(0)
                result.append(copy_passcode.pop(0))
    if passcode == result:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

    # while len(sample) >= len(passcode):
    #     if passcode[0] == sample[0]:
    #         passcode.pop(0)
    #     sample.pop(0)
    #
    #     if len(passcode) == 0:
    #         print(f"#{t}: 1")
    #         break
    #
    # else:
    #     print(f"#{t}: 0")

    # while True:
    #     if passcode[0] == sample[0]:
    #         passcode.pop(0)
    #         result.append(sample.pop(0))
    #     elif passcode[0] != sample[0]:
    #         sample.pop(0)
    #     if len(sample) < len(passcode):
    #         print(0)
    #         break
    #     elif len(sample) == 0:
    #         print(1)
    #         break






# T = int(input())
# for t in range(1, T + 1):
#     N, K = map(int, input().split()) # sample의 길이 N, passcode의 길이 K
#     SAMPLE = list(map(int, input().split()))
#     PASSCODE = list(map(int, input().split()))
#     SAMPLE_lst = []
#     lst = []
#     SAMPLE_lst.append(SAMPLE[0])
#     for i in range(1, N):
#         if SAMPLE[i] != SAMPLE[i - 1]:
#             SAMPLE_lst.append(SAMPLE[i])
#     p = 0
#     while True:
#         if p + K <= len(SAMPLE_lst):
#             lst.append(SAMPLE_lst[p : p + K])
#         p += 1
#         if p + K == len(SAMPLE_lst):
#             break
#     if PASSCODE in lst:
#         print(f'#{t} 1')
#     else:
#         print(f'#{t} 0')