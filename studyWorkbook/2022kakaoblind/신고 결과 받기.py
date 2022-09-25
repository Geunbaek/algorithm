from collections import defaultdict

def solution(id_list, report, k):
    ban = defaultdict(int)
    ids = {}
    for user_id in id_list:
        ids[user_id] = set()

    for report_info in report:
        user, ban_user = report_info.split()
        if ban_user not in ids[user]:
            ids[user].add(ban_user)
            ban[ban_user] += 1

    ret = [0 for _ in range(len(id_list))]
    for user_id, ban_user in ids.items():
        for baned_id in ban_user:
            if ban[baned_id] >= k:
                ret[id_list.index(user_id)] += 1

    return ret
