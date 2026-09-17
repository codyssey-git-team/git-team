def chunk(items, size=0):
    """리스트를 size 개씩 잘라 리스트의 리스트로 반환한다.

    마지막 조각은 남은 개수만큼만 담고, 빈 자리를 채우지 않는다.
    size 를 생략하거나 0 이면 자르지 않고 전체를 한 조각으로 반환한다.
    size 가 음수이면 ValueError 를 던진다.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([1, 2, 3])
    [[1, 2, 3]]
    >>> chunk([], 3)
    []
    >>> chunk([1, 2, 3], -1)
    Traceback (most recent call last):
        ...
    ValueError: size must not be negative, got -1
    """
    if size < 0:
        raise ValueError(f"size must not be negative, got {size}")
    if size == 0:
        return [items]
    return [items[i:i + size] for i in range(0, len(items), size)]
