import pytest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows

def test_ft():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities

def test_ft_empty():
    assert fit_transform([]) == []

def test_name():
    name = ['Andrey', 'Nikita', 'Andrey', 'Vlad']
    exp_transformed_name = [
        ('Andrey', [0, 0, 1]),
        ('Nikita', [0, 1, 0]),
        ('Andrey', [0, 0, 1]),
        ('Vlad', [1, 0, 0]),
    ]
    assert fit_transform(name) == exp_transformed_name

def test_subject():
    subject = ['Python','Statistic','SQL','SQL', 'ML']
    exp_transformed_subject = [
        ('Python', [0, 0, 0, 1]),
        ('Statistic', [0, 0, 1, 0]),
        ('SQL', [0, 1, 0, 0]),
        ('SQL', [0, 1, 0, 0]),
        ('ML', [1, 0, 0, 0])
    ]
    assert fit_transform(subject) == exp_transformed_subject

def test_Exception():
    with pytest.raises(TypeError):
        x = fit_transform(100)
