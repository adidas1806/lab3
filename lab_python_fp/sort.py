from math import fabs


def lambda_sort(data):
    return sorted(data, key=lambda x: -fabs(x))


def key_sort(data):
    return sorted(data, key=fabs, reverse=True)
