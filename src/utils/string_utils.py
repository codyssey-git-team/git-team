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
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_camel_case(text: str) -> str:
    """
    스네이크 표기법(snake_case) 문자열을 카멜 표기법(camelCase)으로 변환합니다.
    선행 및 후행 밑줄은 private 관례 유지를 위해 그대로 보존됩니다.

    Example:
        >>> to_camel_case("hello_world")
        'helloWorld'
        >>> to_camel_case("my_project_name")
        'myProjectName'
        >>> to_camel_case("_private_variable")
        '_privateVariable'
        >>> to_camel_case("hello_world_v2")
        'helloWorldV2'
    """
    if not text:
        return text

    # 선행/후행 밑줄 개수 계산
    leading_underscores = "_" * (len(text) - len(text.lstrip('_')))
    trailing_underscores = "_" * (len(text) - len(text.rstrip('_')))
    
    stripped = text.strip('_')
    if not stripped:
        return text  # "_" 또는 "__" 같은 경우 그대로 반환

    components = [c for c in stripped.split('_') if c]
    if not components:
        return text

    # 첫 단어는 소문자 유지, 이후 단어는 첫 글자만 대문자화(capitalize)
    camel = components[0].lower() + ''.join(x.capitalize() for x in components[1:])
    return f"{leading_underscores}{camel}{trailing_underscores}"

def to_pascal_case(text: str) -> str:
    """
    스네이크 표기법(snake_case) 문자열을 파스칼 표기법(PascalCase)으로 변환합니다.
    선행 및 후행 밑줄은 그대로 보존됩니다.

    Example:
        >>> to_pascal_case("hello_world")
        'HelloWorld'
        >>> to_pascal_case("my_project_name")
        'MyProjectName'
        >>> to_pascal_case("_private_class")
        '_PrivateClass'
    """
    if not text:
        return text

    leading_underscores = "_" * (len(text) - len(text.lstrip('_')))
    trailing_underscores = "_" * (len(text) - len(text.rstrip('_')))
    
    stripped = text.strip('_')
    if not stripped:
        return text

    components = [c for c in stripped.split('_') if c]
    pascal = ''.join(x.capitalize() for x in components)
    return f"{leading_underscores}{pascal}{trailing_underscores}"
