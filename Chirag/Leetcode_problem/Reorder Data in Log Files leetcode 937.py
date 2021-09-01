def reorderLogFiles( logs):
    def f(log):
        _id,rest = log.split(" ", 1)
        return (0, rest, _id) if rest[0].isalpha() else (1, )
    return sorted(logs, key = f)
