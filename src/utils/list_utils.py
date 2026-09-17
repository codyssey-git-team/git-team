def chunk(items, size):
    """리스트를 size 개씩 잘라 리스트의 리스트로 반환한다.

    마지막 조각은 남은 개수만큼만 담고, 빈 자리를 채우지 않는다.
    size 가 0 이하이면 ValueError 를 던진다.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([], 3)
    []
    >>> chunk([1, 2, 3], 0)
    Traceback (most recent call last):
        ...
    ValueError: size must be positive, got 0
    """
    if size <= 0:
        raise ValueError(f"size must be positive, got {size}")
    return [items[i:i + size] for i in range(0, len(items), size)]
