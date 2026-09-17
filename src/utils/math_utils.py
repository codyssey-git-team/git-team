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

    Examples:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(5, 0, 10)
        5
    """

    upper_limited = min(value, high)

    return max(low, upper_limited)