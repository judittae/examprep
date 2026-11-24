# === Stage 3: Хранилище в памяти ===
# Project: ExamPrep
"""ExamPrep: хранилище тем в памяти (этап 3)."""


class Topic:
    def __init__(self, topic_id, name, subject, level, date):
        self.id = topic_id
        self.name = name
        self.subject = subject
        self.level = level
        self.date = date

    def __repr__(self):
        return f"Topic(id={self.id!r}, name={self.name!r}, subject={self.subject!r}, level={self.level!r}, date={self.date!r})"


class TopicStore:
    def __init__(self):
        self._topics = {}
        self._counter = 0

    def add_topic(self, name, subject, level, date):
        self._counter += 1
        topic = Topic(self._counter, name, subject, level, date)
        self._topics[topic.id] = topic
        return topic

    def get_topic(self, topic_id):
        return self._topics.get(topic_id)

    def list_topics(self):
        return list(self._topics.values())


if __name__ == "__main__":
    store = TopicStore()
    store.add_topic("Алгебра", "Математика", "Базовый", "2025-06-01")
    store.add_topic("Классификация", "Биология", "Повышенный", "2025-06-02")
    found = store.get_topic(1)
    print(found)
    print(store.list_topics())
