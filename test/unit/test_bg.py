import pytest

from sentencesegmenter import segment

# ruff: noqa: E501

tests = [
    (
        "В първата половина на ноември т.г. ще бъде свикан Консултативният съвет за национална сигурност, обяви държавният глава.",
        [
            "В първата половина на ноември т.г. ще бъде свикан Консултативният съвет за национална сигурност, обяви държавният глава."
        ],
    ),
    (
        "Компютърът е устройство с общо предназначение, което може да бъде програмирано да извършва набор от аритметични и/или логически операции. Възможността поредицата такива операции да бъде променяна позволява компютърът да се използва за решаването на теоретично всяка изчислителна/логическа задача. Обикновено целта на тези операции е обработката на въведена информация (данни), представена в цифров (дигитален) вид, резултатът от които може да се изведе в най-общо казано използваема форма.",
        [
            "Компютърът е устройство с общо предназначение, което може да бъде програмирано да извършва набор от аритметични и/или логически операции.",
            "Възможността поредицата такива операции да бъде променяна позволява компютърът да се използва за решаването на теоретично всяка изчислителна/логическа задача.",
            "Обикновено целта на тези операции е обработката на въведена информация (данни), представена в цифров (дигитален) вид, резултатът от които може да се изведе в най-общо казано използваема форма.",
        ],
    ),
    ('Пл. "20 Април"', ['Пл. "20 Април"']),
    (
        "Той поставя началото на могъща династия, която управлява в продължение на 150 г. Саргон надделява в двубой с владетеля на град Ур и разширява териториите на държавата си по долното течение на Тигър и Ефрат. Стойностни, вкл. български и руски",
        [
            "Той поставя началото на могъща династия, която управлява в продължение на 150 г. Саргон надделява в двубой с владетеля на град Ур и разширява териториите на държавата си по долното течение на Тигър и Ефрат.",
            "Стойностни, вкл. български и руски",
        ],
    ),
]


@pytest.mark.parametrize("text,expected_sentences", tests)
def test_segment(text, expected_sentences):
    assert list(segment("bg", text)) == expected_sentences
