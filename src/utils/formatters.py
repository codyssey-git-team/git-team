def format_price(amount):
    """금액을 정수로 반올림해 문자열로 변환한다."""
    return str(round(amount)) + "원"


def format_percent(value):
    """비율을 퍼센트 문자열로 변환한다."""
    return str(value * 100) + "%"
