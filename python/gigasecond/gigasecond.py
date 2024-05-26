from datetime import timedelta


def add(moment):
    seconds = timedelta(seconds=1_000_000_000)
    return moment + seconds
