import pytest

from src.decorators import error_function, log, my_function


def test_error_function_type_error():
    with pytest.raises(TypeError):
        my_function((1, 2), {})
    with pytest.raises(ValueError):
        error_function(1, 0)
