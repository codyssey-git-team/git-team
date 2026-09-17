def format_price(amount):
    """금액을 정수로 반올림하고 천 단위 쉼표를 붙여 문자열로 변환한다."""
    return f"{round(amount):,}원"


def format_percent(value):
    """비율을 퍼센트 문자열로 변환한다."""
    return str(value * 100) + "%"
