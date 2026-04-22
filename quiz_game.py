"""
quiz_game.py
게임 전체 흐름을 관리하는 QuizGame 클래스 (초기 버전 - 메뉴만 구현).
"""

from input_utils import read_int_in_range


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.quizzes = []
        self.best_score = -1

    def show_menu(self) -> None:
        print()
        print("=" * 40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("=" * 40)

    def run(self) -> None:
        while True:
            self.show_menu()
            choice = read_int_in_range("선택: ", 1, 5)

            if choice == 5:
                print("\n👋  게임을 종료합니다. 안녕히 가세요!\n")
                break
            else:
                print("\n(아직 구현되지 않은 기능입니다.)")
