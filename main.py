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
        # Ctrl+C로 종료 요청
        print("\n\n⏹️   Ctrl+C 감지. 현재 상태를 저장하고 종료합니다.")
        game.save_state()
    except EOFError:
        # 입력 스트림이 닫힘 (파이프 종료 등)
        print("\n\n⏹️   입력이 종료되었습니다. 현재 상태를 저장하고 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()
