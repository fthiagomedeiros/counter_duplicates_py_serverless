import pytest

from src.business_logic.counter_duplicates import counter_duplicates


@pytest.mark.parametrize("name,expected", [("teste", {"t": 2, "e": 2}),
                                           ("wwook", {"w": 2, "o": 2}),
                                           ("", {}),
                                           ("abcd", {}),
                                           ("         ", {}),
                                           ("Brazil", {}),
                                           ])
def test_find_duplicates(name, expected):
    duplicates_output = counter_duplicates(name)
    assert duplicates_output == expected
