import pytest

from src.business_logic.counter_duplicates import counter_duplicates


@pytest.mark.parametrize("name,expected", [("teste", {"t": 2, "e": 2}),
                                           ("wwook", {"w": 2, "o": 2}),
                                           ("abcd", {}),
                                           ("         ", {}),
                                           ("Brazil", {}),
                                           ("BrazilBrazilBrazilB", {"B": 4, "r": 3, "a": 3, "z": 3, "i": 3, "l": 3}),
                                           ("", {})
                                           ])
def test_find_duplicates(name, expected):
    duplicates_output = counter_duplicates(name)
    assert duplicates_output == expected
