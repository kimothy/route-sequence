# route-sequence

A number range between 0 to 6759999 represented as AA0000 to ZZ9999.

## Usecase
This number series is used as menomic number series that has two benefits over integers.
Easier to remember, and over 6 times as many unique combinations (~6.7 mill instead 1 mill). The series also have a
fixed with of 6 chars, which makes it uniform when printed.


## Usage

~~~ python
>>> from route_sequence import RouteSequence
>>> route_sequence = RouteSequence('AZ9998')
RouteSequence(AZ9998)

>>> for route in route_sequence:
>>>     if route == 'BA0001':
>>>         break


>>> print(route_sequence)
RouteSequence(BA0001)
~~~

You can also work with integers. Interally calculations and state is stored as an integer.

~~~ python
from route_sequence import RouteSequence

route_sequence = RouteSequence(1000)
for route in route_sequence:
    if route == 923300:
        break
        
>>> print(route_sequence)
RouteSequence(DO3300)
~~~

The RouteSequence can also be used with zip.
~~~ python
from route_sequence import RouteSequence

>>> print(list(zip([1, 2, 3], RouteSequence('FG9032'))
[(1, RouteSequence(FG9032)), (2, RouteSequence(FG9033), (3, RouteSequence(FG9034))]
~~~

Iterationg using next()
~~~ python
from route_sequence import RouteSequence

route_sequence = RouteSequence()
next(route_sequence)

>>> print(route_sequence)
RouteSequence(AA0001)
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
The RouteSequence object can be compared with both itegers and valid strings. This is handy since interally programs can use the integer values which is faster, while from a user interface perspective the string representation can be used as is. Interally the string representation is allways converted to and integer.

~~~ python
>>> from route_sequence import RouteSequence

>>> RouteSequence('AB0000') == 'AB0000'
True

>>> RouteSequence('AB0000') == 1000
True

>>> RouteSequence('AB0000') > 999
True
~~~



