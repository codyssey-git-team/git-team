from datetime import date


def days_between(d1, d2):
    """두 날짜 사이의 일수를 반환한다.

    >>> days_between(date(2026, 1, 1), date(2026, 1, 11))
    10
    """
    return abs((d2 - d1).days)
