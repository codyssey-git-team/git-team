def clamp(value, low, high):
    """
    값을 low와 high 사이의 범위로 제한한다.

    Args:
        value: 제한할 값
        low: 허용되는 최소값
        high: 허용되는 최대값

    Returns:
        value가 low보다 작으면 low,
        high보다 크면 high,
        범위 안에 있으면 value를 그대로 반환한다.

    Raises:
        ValueError: low가 high보다 큰 경우

    Examples:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(5, 0, 10)
        5
        >>> clamp(5, 10, 0)
        Traceback (most recent call last):
            ...
        ValueError: low must be less than or equal to high
    """

    # 최소값이 최대값보다 크면 유효하지 않은 범위이므로 예외를 발생시킨다.
    if low > high:
        raise ValueError("low must be less than or equal to high")

    # value를 low 이상 high 이하의 범위로 제한한다.
    return max(low, min(value, high))