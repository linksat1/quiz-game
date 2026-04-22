"""
main.py
퀴즈 게임의 진입점.
Ctrl+C (KeyboardInterrupt) 및 입력 스트림 종료(EOFError)를
일괄 처리하여 비정상 종료를 방지한다.
"""

from quiz_game import QuizGame


def main() -> None:
    game = QuizGame()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\n⏹️   Ctrl+C 감지. 종료합니다.")
    except EOFError:
        print("\n\n⏹️   입력이 종료되었습니다. 종료합니다.")


if __name__ == "__main__":
    main()
