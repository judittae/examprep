# === Stage 1: Каркас модуля ===
# Project: ExamPrep
from datetime import date


@dataclass
class Topic:
    name: str
    subject: str
    level: str
    date: date


def create_demo_topics() -> list[Topic]:
    return [
        Topic("Арифметика", "Математика", "Базовый", date(2025, 9, 1)),
        Topic("Грамматика", "Английский язык", "Средний", date(2025, 9, 15)),
        Topic("История", "История", "Продвинутый", date(2025, 10, 1)),
    ]


def main() -> None:
    for topic in create_demo_topics():
        print(topic)


if __name__ == "__main__":
    main()
