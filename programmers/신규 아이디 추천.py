import re


def getIdThatOperatedLevel1(_id):
    return _id.lower()


def getIdThatOperatedLevel2(_id):
    return re.sub(r"[^a-z0-9-_.]", "", _id)


def getIdThatOperatedLevel3(_id):
    return re.sub(r"\.{2,}", ".", _id)


def getIdThatOperatedLevel4(_id):
    return re.sub(r"^[.]|[.]$", "", _id)


def getIdThatOperatedLevel5(_id):
    return _id if _id else 'a'


def getIdThatOperatedLevel6(_id):
    if len(_id) < 16:
        return _id
    _id = _id[:15]
    return getIdThatOperatedLevel4(_id)


def getIdThatOperatedLevel7(_id):
    if len(_id) > 2:
        return _id
    return _id.ljust(3, _id[-1])


def solution(new_id):
    _id = getIdThatOperatedLevel1(new_id)
    _id = getIdThatOperatedLevel2(_id)
    _id = getIdThatOperatedLevel3(_id)
    _id = getIdThatOperatedLevel4(_id)
    _id = getIdThatOperatedLevel5(_id)
    _id = getIdThatOperatedLevel6(_id)
    _id = getIdThatOperatedLevel7(_id)

    return _id