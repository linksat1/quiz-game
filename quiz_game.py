"""
quiz_game.py
게임 전체 흐름을 관리하는 QuizGame 클래스를 정의한다.
- 메뉴 표시
- 퀴즈 풀기 / 추가 / 목록 / 점수 확인
- state.json 파일 저장/불러오기
"""

import json
import os

from quiz import Quiz
from default_quizzes import get_default_quizzes
from input_utils import read_int_in_range, read_nonempty_string


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스.

    Attributes:
        quizzes (list[Quiz]): 등록된 퀴즈 목록
        best_score (int): 최고 점수 (100점 만점 기준, 아직 풀지 않았으면 -1)
        state_path (str): state.json 파일 경로
    """

    DEFAULT_STATE_PATH = "state.json"

    def __init__(self, state_path: str = DEFAULT_STATE_PATH):
        self.state_path = state_path
        self.quizzes: list = []
        self.best_score: int = -1  # -1 == 아직 한 번도 풀지 않음
        self.load_state()

    # ---------------------------------------------------------------
    # 파일 입출력
    # ---------------------------------------------------------------
    def load_state(self) -> None:
        """state.json을 읽어 퀴즈/최고점수를 불러온다.

        - 파일이 없으면 기본 퀴즈를 사용한다.
        - JSON이 손상되었거나 형식이 이상하면 안내 후 기본 퀴즈로 복구한다.
        """
        if not os.path.exists(self.state_path):
            print("📂  저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = -1
            self.save_state()
            return

        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            quizzes_data = data.get("quizzes", [])
            best_score = data.get("best_score", -1)

            self.quizzes = [Quiz.from_dict(q) for q in quizzes_data]
            self.best_score = int(best_score) if best_score is not None else -1

            if not self.quizzes:
                print("ℹ️  저장된 퀴즈가 없어 기본 퀴즈를 불러왔습니다.")
                self.quizzes = get_default_quizzes()
                self.save_state()
            else:
                score_text = f"{self.best_score}점" if self.best_score >= 0 else "미기록"
                print(
                    f"📂  저장된 데이터를 불러왔습니다. "
                    f"(퀴즈 {len(self.quizzes)}개, 최고점수 {score_text})"
                )
        except (json.JSONDecodeError, ValueError, KeyError, TypeError) as e:
            print(f"⚠️  데이터 파일이 손상되었습니다({type(e).__name__}). 기본 퀴즈로 복구합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = -1
            self.save_state()
        except OSError as e:
            print(f"⚠️  데이터 파일을 읽는 중 오류가 발생했습니다: {e}")
            print("   기본 퀴즈로 시작합니다. (저장은 시도하지 않습니다.)")
            self.quizzes = get_default_quizzes()
            self.best_score = -1

    def save_state(self) -> None:
        """현재 상태(퀴즈 + 최고점수)를 state.json에 저장한다."""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(self.state_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"⚠️  데이터 저장 중 오류가 발생했습니다: {e}")

    # ---------------------------------------------------------------
    # 메뉴
    # ---------------------------------------------------------------
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
        """메인 게임 루프."""
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
                self.save_state()
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

        self.save_state()

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
        self.save_state()
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
