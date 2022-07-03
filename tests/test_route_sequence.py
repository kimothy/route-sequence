from hypothesis import given, example
from hypothesis.strategies import integers
from pytest import raises

from route_sequence import RouteSequence


@given(integers(min_value=0, max_value=6760000))
def test_coversions(seed):
    assert int(RouteSequence(seed)) == seed


def test_generator_end_condition():
    route_sequence = RouteSequence('ZZ9998')

    assert next(route_sequence) == 'ZZ9999'

    with raises(StopIteration):
        next(route_sequence)

@given(integers(min_value=1, max_value=6760000))
def test_overflow_errors(value):
    with raises(OverflowError):
        RouteSequence('ZZ9999') + value

    with raises(OverflowError):
        RouteSequence('AA0000') - value

@given(integers(min_value=-6760000, max_value=-1))
def test_seed_out_of_range_lower(value):
    with raises(ValueError):
        RouteSequence(value)

@given(integers(min_value=6760000, max_value=6760000*2))
def test_seed_out_of_range_upper(value):
    with raises(ValueError):
        RouteSequence(value)

@given(integers(min_value=1, max_value=10))
def test_multiply(value):
    assert RouteSequence('AA0001') * value == 1 * value

@given(integers(min_value=1, max_value=10))
def test_divide(value):
    assert RouteSequence('AA0010') / value == 10 // value

@given(integers(min_value=1, max_value=10))
def test_add(value):
    assert RouteSequence('AA0010') + value == 10 + value

@given(integers(min_value=1, max_value=10))
def test_substract(value):
    assert RouteSequence('AA0010') - value == 10 - value

@given(integers(min_value=1, max_value=6760000))
def test_substract_out_of_range(value):
    with raises(OverflowError):
        RouteSequence(0) - value

@given(integers(min_value=1, max_value=6760000))
def test_add_out_of_range(value):
    with raises(OverflowError):
        RouteSequence('ZZ9999') + value