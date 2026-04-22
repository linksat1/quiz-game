"""
quiz.py
개별 퀴즈(문제)를 표현하는 Quiz 클래스를 정의한다.
"""


class Quiz:
    """단일 퀴즈(문제 1개)를 표현하는 클래스.

    Attributes:
        question (str): 문제 내용
        choices (list[str]): 선택지 4개
        answer (int): 정답 번호 (1~4)
    """

    def __init__(self, question: str, choices: list, answer: int):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제(question)는 비어있지 않은 문자열이어야 합니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지(choices)는 4개의 항목을 가진 리스트여야 합니다.")
        if not all(isinstance(c, str) and c.strip() for c in choices):
            raise ValueError("모든 선택지는 비어있지 않은 문자열이어야 합니다.")
        if not isinstance(answer, int) or not (1 <= answer <= 4):
            raise ValueError("정답(answer)은 1~4 사이의 정수여야 합니다.")

        self.question = question.strip()
        self.choices = [c.strip() for c in choices]
        self.answer = answer

    def display(self, index: int = None) -> None:
        """퀴즈를 화면에 출력한다.

        Args:
            index: 문제 번호(1부터 시작). None이면 번호를 표시하지 않는다.
        """
        print("-" * 40)
        if index is not None:
            print(f"[문제 {index}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")
        print()

    def is_correct(self, user_answer: int) -> bool:
        """사용자가 입력한 번호가 정답인지 확인한다."""
        return user_answer == self.answer

    def to_dict(self) -> dict:
        """JSON 저장을 위한 dict 변환."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        """dict 데이터로부터 Quiz 객체를 생성한다."""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
        )

    def __repr__(self) -> str:
        return f"Quiz(question={self.question!r}, answer={self.answer})"
