from datetime import date


def days_between(d1, d2):
    """날짜 순서와 관계없이 두 날짜 사이의 절대 일수를 반환한다.

    >>> days_between(date(2026, 1, 1), date(2026, 1, 11))
    10
    >>> days_between(date(2026, 1, 11), date(2026, 1, 1))
    10
    """
    return abs((d2 - d1).days)
