# -*- coding: utf-8 -*-
import pytest

from src.CalcRating import RatingType
from src.FirstQuartile import FirstQuartile


class TestFirstQuartile:

    @pytest.fixture()
    def rating(self) -> RatingType:
        return {
            "A": 45.0,
            "B": 61.67,
            "C": 62.0,
            "D": 69.0,
            "E": 76.67,
            "F": 79.0,
            "G": 85.33,
            "H": 87.0,
            "I": 95.5,
            "J": 95.67,
        }

    def test_quartiles(self, rating: RatingType) -> None:
        q1, q2, q3 = FirstQuartile(rating).quartiles()
        assert q1 == pytest.approx(62.0)
        assert q2 == pytest.approx(77.835)
        assert q3 == pytest.approx(87.0)

    def test_first_quartile_students(self, rating: RatingType) -> None:
        students = FirstQuartile(rating).get_first_quartile_students()
        assert sorted(students) == ["A", "B", "C"]

    def test_odd_count(self) -> None:
        fq = FirstQuartile({"A": 10.0, "B": 20.0, "C": 30.0})
        assert fq.quartiles() == (10.0, 20.0, 30.0)
        assert fq.get_first_quartile_students() == ["A"]

    def test_single_student(self) -> None:
        fq = FirstQuartile({"A": 50.0})
        assert fq.quartiles() == (50.0, 50.0, 50.0)
        assert fq.get_first_quartile_students() == ["A"]

    def test_empty_rating_raises(self) -> None:
        with pytest.raises(ValueError):
            FirstQuartile({}).quartiles()
