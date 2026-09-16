# src/utils/string_utils.py
import re

def to_snake_case(text: str) -> str:
    """
    카멜 표기법(camelCase)이나 파스칼 표기법(PascalCase) 문자열을 스네이크 표기법(snake_case)으로 변환합니다.

    Example:
        >>> to_snake_case("helloWorld")
        'hello_world'
        >>> to_snake_case("MyProjectName")
        'my_project_name'
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_camel_case(text: str) -> str:
    """
    스네이크 표기법(snake_case) 문자열을 카멜 표기법(camelCase)으로 변환합니다.

    Example:
        >>> to_camel_case("hello_world")
        'helloWorld'
        >>> to_camel_case("my_project_name")
        'myProjectName'
    """
    components = text.split('_')
    # 첫 글자는 소문자로, 나머지는 대문자로 시작하여 합침
    return components[0] + ''.join(x.title() for x in components[1:])