"""
quiz_game.py
게임 전체 흐름을 관리하는 QuizGame 클래스.
- 메뉴 표시
- 퀴즈 풀기 / 추가 / 목록 / 점수 확인
"""

from quiz import Quiz
from default_quizzes import get_default_quizzes
from input_utils import read_int_in_range, read_nonempty_string


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.quizzes = get_default_quizzes()
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

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                print("\n👋  게임을 종료합니다. 안녕히 가세요!\n")
                break

    # ---------------------------------------------------------------
    # 1. 퀴즈 풀기
    # ---------------------------------------------------------------
    def play_quiz(self) -> None:
        if not self.quizzes:
            print("\nℹ️  등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        print(f"\n📝  퀴즈를 시작합니다! (총 {total}문제)\n")

        correct_count = 0
        for i, quiz in enumerate(self.quizzes, start=1):
            quiz.display(index=i)
            user_answer = read_int_in_range("정답 입력 (1-4): ", 1, 4)
            if quiz.is_correct(user_answer):
                print("✅  정답입니다!\n")
                correct_count += 1
            else:
                print(f"❌  오답입니다. 정답은 {quiz.answer}번 입니다.\n")

        score = int(correct_count / total * 100)

        print("=" * 40)
        print(f"🏆  결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        if score > self.best_score:
            self.best_score = score
            print("🎉  새로운 최고 점수입니다!")
        else:
            best_text = f"{self.best_score}점" if self.best_score >= 0 else "미기록"
            print(f"현재 최고 점수: {best_text}")
        print("=" * 40)

    # ---------------------------------------------------------------
    # 2. 퀴즈 추가
    # ---------------------------------------------------------------
    def add_quiz(self) -> None:
        print("\n📌  새로운 퀴즈를 추가합니다.\n")

        question = read_nonempty_string("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choice = read_nonempty_string(f"선택지 {i}: ")
            choices.append(choice)
        answer = read_int_in_range("정답 번호 (1-4): ", 1, 4)

        try:
            new_quiz = Quiz(question=question, choices=choices, answer=answer)
        except ValueError as e:
            print(f"⚠️  퀴즈 생성 실패: {e}")
            return

        self.quizzes.append(new_quiz)
        print("\n✅  퀴즈가 추가되었습니다!")

    # ---------------------------------------------------------------
    # 3. 퀴즈 목록
    # ---------------------------------------------------------------
    def show_quiz_list(self) -> None:
        if not self.quizzes:
            print("\nℹ️  등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋  등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)

    # ---------------------------------------------------------------
    # 4. 점수 확인
    # ---------------------------------------------------------------
    def show_best_score(self) -> None:
        print()
        if self.best_score < 0:
            print("ℹ️  아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어 보세요!")
        else:
            print(f"🏆  최고 점수: {self.best_score}점")
