from decorators import log_errors


@log_errors
def cpp_map(x1, y1, x2, y2, value):
    if x1 == y1:
        raise ValueError("Исходный отрезок не может быть вырожденным")

    # Вычисляем коэффициенты преобразования
    source_range = y1 - x1
    target_range = y2 - x2
    scale = target_range / source_range

    return int(x2 + (value - x1) * scale)