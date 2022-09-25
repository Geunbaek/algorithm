def solution(record):
    answer = []
    userInfo = {}

    for recordInfo in record:
        recordInfo = recordInfo.split()
        state = recordInfo[0]
        if state == "Enter":
            uid, nickname = recordInfo[1:]
            userInfo[uid] = nickname
            answer.append([uid, "님이 들어왔습니다."])
        elif state == "Leave":
            uid = recordInfo[1]
            answer.append([uid, "님이 나갔습니다."])
        else:
            uid, nickname = recordInfo[1:]
            userInfo[uid] = nickname

    return list(map(lambda x: "".join([userInfo[x[0]], x[1]]), answer))

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))