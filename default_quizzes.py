"""
default_quizzes.py
state.json 파일이 없거나 손상된 경우 사용하는 기본 퀴즈 데이터.
주제: 우주/과학 상식
"""

from quiz import Quiz


def get_default_quizzes() -> list:
    """우주/과학 상식 기본 퀴즈 리스트를 반환한다."""
    return [
        Quiz(
            question="태양계에서 가장 큰 행성은 무엇일까요?",
            choices=["지구", "토성", "목성", "해왕성"],
            answer=3,
        ),
        Quiz(
            question="빛이 진공에서 1초 동안 이동하는 거리는 약 얼마일까요?",
            choices=["3만 km", "30만 km", "300만 km", "3,000만 km"],
            answer=2,
        ),
        Quiz(
            question="인류 최초로 달에 착륙한 사람은 누구일까요?",
            choices=["유리 가가린", "닐 암스트롱", "버즈 올드린", "마이클 콜린스"],
            answer=2,
        ),
        Quiz(
            question="물(H2O) 분자 1개는 몇 개의 원자로 이루어져 있을까요?",
            choices=["2개", "3개", "4개", "5개"],
            answer=2,
        ),
        Quiz(
            question="블랙홀의 존재를 이론적으로 예측한 일반 상대성 이론을 발표한 과학자는 누구일까요?",
            choices=["아이작 뉴턴", "닐스 보어", "알버트 아인슈타인", "스티븐 호킹"],
            answer=3,
        ),
        Quiz(
            question="우리 은하(Milky Way)의 중심부에 있다고 알려진 천체의 종류는?",
            choices=["중성자별", "초대질량 블랙홀", "백색왜성", "펄서"],
            answer=2,
        ),
        Quiz(
            question="DNA의 이중 나선 구조를 1953년에 함께 발표한 두 과학자는?",
            choices=[
                "왓슨과 크릭",
                "다윈과 멘델",
                "퀴리와 러더퍼드",
                "파스퇴르와 코흐",
            ],
            answer=1,
        ),
    ]
