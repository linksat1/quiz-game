"""
input_utils.py
숫자/문자열 입력을 안전하게 받기 위한 공통 함수들.
- 앞뒤 공백 제거
- 숫자 변환 실패 처리
- 허용 범위 밖 숫자 처리
- 빈 입력 처리
"""


def read_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    """min_value ~ max_value 사이의 정수를 입력받을 때까지 반복한다.

    공백 제거, 빈 입력, 숫자 변환 실패, 범위 밖 숫자 모두 처리한다.
    EOFError/KeyboardInterrupt는 호출자에게 전달(상위에서 일괄 처리).
    """
    while True:
        raw = input(prompt)
        value = raw.strip()

        if value == "":
            print("⚠️  빈 입력입니다. 숫자를 입력해 주세요.\n")
            continue

        try:
            number = int(value)
        except ValueError:
            print(f"⚠️  잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.\n")
            continue

        if not (min_value <= number <= max_value):
            print(f"⚠️  잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.\n")
            continue

        return number


def read_nonempty_string(prompt: str) -> str:
    """비어있지 않은 문자열을 입력받을 때까지 반복한다."""
    while True:
        raw = input(prompt)
        value = raw.strip()
        if value == "":
            print("⚠️  빈 입력입니다. 내용을 입력해 주세요.\n")
            continue
        return value
