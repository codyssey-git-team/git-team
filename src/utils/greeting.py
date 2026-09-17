"""인사말 관련 헬퍼 함수 모음."""


def greet(name):
    """이름을 받아 인사말을 반환한다."""
    return "Hello, " + name


def farewell(name):
    """이름을 받아 작별 인사를 반환한다."""
    return "Goodbye, " + name


def welcome_team(names):
    """여러 이름에 대해 인사말 목록을 반환한다."""
    return [greet(n) for n in names]
