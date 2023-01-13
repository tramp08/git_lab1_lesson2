# вторая задача
import pytest
from yandex_testing_lesson import reverse


def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_reverse():
    assert reverse('abc') == 'cba'

def test_empty():
    assert reverse('') == ''
