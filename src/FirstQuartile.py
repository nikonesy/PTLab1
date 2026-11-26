# -*- coding: utf-8 -*-
from CalcRating import RatingType

# Кортеж из трех квартилей распределения: Q1, Q2 (медиана), Q3.
QuartilesType = tuple[float, float, float]


class FirstQuartile:
    """Определяет студентов, чей рейтинг попадает в первую квартиль.

    Квартили рассчитываются методом "шарниров" (Tukey's hinges):
    Q2 — медиана всего распределения, Q1 — медиана нижней половины,
    Q3 — медиана верхней половины выборки.
    """

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating

    @staticmethod
    def _median(values: list[float]) -> float:
        count = len(values)
        middle = count // 2
        if count % 2 == 1:
            return values[middle]
        return (values[middle - 1] + values[middle]) / 2.0

    def quartiles(self) -> QuartilesType:
        values = sorted(self.rating.values())
        count = len(values)

        if count == 0:
            raise ValueError("Rating is empty")
        if count == 1:
            return values[0], values[0], values[0]

        middle = count // 2
        q2 = self._median(values)
        lower = values[:middle]
        upper = values[middle:] if count % 2 == 0 else values[middle + 1:]
        q1 = self._median(lower) if lower else values[0]
        q3 = self._median(upper) if upper else values[-1]
        return q1, q2, q3

    def get_first_quartile_students(self) -> list[str]:
        q1, _, _ = self.quartiles()
        return [name for name in self.rating
                if self.rating[name] <= q1]
