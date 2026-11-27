# === Stage 4: Редактирование записей ===
# Project: ExamPrep
def edit_topic(topic_id, subject, level, name, date):
    allowed = {'subject', 'level', 'name', 'date'}
    changes = {
        'subject': subject,
        'level': level,
        'name': name,
        'date': date,
    }
    valid = all(key in allowed for key in changes)
    if not valid:
        raise ValueError('Можно менять только допустимые поля')
    if not isinstance(subject, str) or not isinstance(name, str):
        raise TypeError('Название и предмет должны быть строками')
    if level not in ('легкий', 'средний', 'сложный'):
        raise ValueError('Уровень не из допустимого списка')
    for key in ('subject', 'level', 'name', 'date'):
        setattr(topic_id, key, changes[key])
    return topic_id


def validate_level(value):
    return value in ('легкий', 'средний', 'сложный')


def validate_date(value):
    if not isinstance(value, str):
        return False
    try:
        from datetime import datetime
        return datetime.strptime(value, '%Y-%m-%d') is not None
    except ValueError:
        return False


def validate_str(value):
    return isinstance(value, str) and len(value) > 0


def apply_edits(topic_id, subject, level, name, date):
    if not validate_str(subject):
        raise ValueError('Предмет должен быть непустой строкой')
    if not validate_str(name):
        raise ValueError('Название должно быть непустой строкой')
    if not validate_level(level):
        raise ValueError('Уровень не допустим')
    if not validate_date(date):
        raise ValueError('Дата не в формате YYYY-MM-DD')
    topic_id.subject = subject
    topic_id.level = level
    topic_id.name = name
    topic_id.date = date
    return topic_id
