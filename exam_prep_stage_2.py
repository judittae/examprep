# === Stage 2: Проверка полей ===
# Project: ExamPrep
import re
from datetime import datetime


def normalize_input(value):
    if value is None:
        return ""
    if isinstance(value, (int, float)):
        value = str(value)
    text = value.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def validate_title(title):
    if title is None:
        return "Название не может быть пустым."
    normalized = normalize_input(title)
    if not normalized:
        return "Название не может быть пустым."
    if len(normalized) > 100:
        return "Название слишком длинное (максимум 100 символов)."
    return None


def validate_subject(subject):
    if subject is None:
        return "Предмет не может быть пустым."
    normalized = normalize_input(subject)
    if not normalized:
        return "Предмет не может быть пустым."
    if len(normalized) > 100:
        return "Предмет слишком длинный (максимум 100 символов)."
    return None


def validate_level(level):
    if level is None:
        return "Уровень не может быть пустым."
    normalized = normalize_input(level)
    if not normalized:
        return "Уровень не может быть пустым."
    allowed = {"базовый", "средний", "продвинутый"}
    normalized_lower = normalized.lower()
    if normalized_lower not in allowed:
        return "Уровень должен быть одним из: базовый, средний, продвинутый."
    return None


def validate_date(date_value):
    if date_value is None:
        return "Дата не может быть пустой."
    if isinstance(date_value, datetime):
        return None
    normalized = normalize_input(date_value)
    if not normalized:
        return "Дата не может быть пустой."
    formats = ("%d.%m.%Y", "%Y-%m-%d", "%Y.%m.%d", "%d %b %Y")
    for fmt in formats:
        try:
            datetime.strptime(normalized, fmt)
            return normalized
        except ValueError:
            continue
    return "Дата должна быть в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД."


def validate_topic_fields(topic):
    errors = []
    errors.append(validate_title(topic.get("название")))
    errors.append(validate_subject(topic.get("предмет")))
    errors.append(validate_level(topic.get("уровень")))
    errors.append(validate_date(topic.get("дата")))
    return errors
