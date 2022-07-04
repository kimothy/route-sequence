# route-sequence

A number range between 0 to 6759999 represented as AA0000 to ZZ9999.

## Usecase
route-sequence is intended to be used as a mnemonic number series that has some distinct benefits over integers.

1. Easy to remember due to the combination of letters and numbers.
2. Over 6 times as many combinations availible compared to 6 digit integers.
3. Fixed width.

Some practical use cases could be a unique id for a configuration line, order number etc.

Even though the number series supports mathmatical operations, the intention is to provide
a unique number series.

## Usage

~~~ python
>>> from route_sequence import RouteSequence
>>> route_sequence = RouteSequence('AZ9998')
RouteSequence(AZ9998)

>>> for route in route_sequence:
>>>     if route == 'BA0001':
>>>         break
RouteSequence(BA0001)
~~~

You can also work with integers. Interally calculations and state is stored as an integer.

~~~ python
>>> from route_sequence import RouteSequence

>>> route_sequence = RouteSequence(1000)
>>> for route in route_sequence:
>>>     if route == 923300:
>>>         break
RouteSequence(DO3300)
~~~

The RouteSequence can also be used with zip.
~~~ python
from route_sequence import RouteSequence

>>> print(list(zip([1, 2, 3], RouteSequence('FG9032'))
[(1, RouteSequence(FG9033)), (2, RouteSequence(FG9034), (3, RouteSequence(FG9035))]
~~~

Iteration using next()
~~~ python
>>> from route_sequence import RouteSequence

>>> route_sequence = RouteSequence()
RouteSequence(AA0000)

>>> next(route_sequence)
RouteSequence(AA0001)
~~~

It's important to node the the first iteration will be the next value after the seed.
If there is a need to use the seed value as the first in a generated sequence, you can
substract 1 from the route sequence.

~~~ python
>>>from route_sequence import RouteSequence

>>>route_sequence = RouteSequence()
RouteSequence(AA0000)

>>>next(RouteSequence('ZB0001') - 1)
RouteSequence(ZB0001)
~~~

## Mathmatical Operations

Basic mathmatical operations are supported. The number series is basically an integer range from
0 to 6759999, represented as AA0000 to ZZ9999.

~~~ python
>>> import RouteSequence

>>> RouteSequence(AA0000) + 1
RouteSequence(AA0001)

>>> RouteSequence(ZZ9999) + 1
OverflowError: Upper limit of 6759999 / ZZ9999 surpassed

>>> RouteSequence(BA0000) - 1
RouteSequence(AZ9999)

>>> RouteSequence(AA0000) - 1
OverflowError: Lower limit of 0 / AA0000 surpassed
~~~


Multiplications and divisions also work as expected, however divisions are floored since the number series does not support floating point numbers.
As with additions and substractions and OverflowError will be raised if the resulting number is out of the valid range, and ZeroDivisionError if divided by 0.

~~~ python
>>> from route_sequence import RouteSequence

>>> RouteSequence(0) * 0
RouteSequence(AA0000)

>>> RouteSequence(AB0000) * (AA0002)
RouteSequence(AC0000)

>>> RouteSequence(10) / 3
RouteSequence(AA0003)
~~~


## Comparisons
The RouteSequence object can be compared with both integers and valid strings. This is handy since interally programs can use the integer values which is faster and simple, while from a user interface perspective the string representation can be used as is. Interally the string representation is allways converted to an integer.

~~~ python
>>> from route_sequence import RouteSequence

>>> RouteSequence('AB0000') == 'AB0000'
True

>>> RouteSequence('AB0000') == 1000
True

>>> RouteSequence('AB0000') > 999
True
~~~



