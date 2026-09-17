def format_price(amount):
    """금액에 천 단위 쉼표를 붙여 문자열로 변환한다."""
    return f"{amount:,}원"


def format_percent(value):
    """비율을 퍼센트 문자열로 변환한다."""
    return str(value * 100) + "%"
