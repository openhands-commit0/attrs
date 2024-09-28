import functools
import types
from ._make import _make_ne
_operation_names = {'eq': '==', 'lt': '<', 'le': '<=', 'gt': '>', 'ge': '>='}

def cmp_using(eq=None, lt=None, le=None, gt=None, ge=None, require_same_type=True, class_name='Comparable'):
    """
    Create a class that can be passed into `attrs.field`'s ``eq``, ``order``,
    and ``cmp`` arguments to customize field comparison.

    The resulting class will have a full set of ordering methods if at least
    one of ``{lt, le, gt, ge}`` and ``eq``  are provided.

    Args:
        eq (typing.Callable | None):
            Callable used to evaluate equality of two objects.

        lt (typing.Callable | None):
            Callable used to evaluate whether one object is less than another
            object.

        le (typing.Callable | None):
            Callable used to evaluate whether one object is less than or equal
            to another object.

        gt (typing.Callable | None):
            Callable used to evaluate whether one object is greater than
            another object.

        ge (typing.Callable | None):
            Callable used to evaluate whether one object is greater than or
            equal to another object.

        require_same_type (bool):
            When `True`, equality and ordering methods will return
            `NotImplemented` if objects are not of the same type.

        class_name (str | None): Name of class. Defaults to "Comparable".

    See `comparison` for more details.

    .. versionadded:: 21.1.0
    """
    pass

def _make_init():
    """
    Create __init__ method.
    """
    pass

def _make_operator(name, func):
    """
    Create operator method.
    """
    pass

def _is_comparable_to(self, other):
    """
    Check whether `other` is comparable to `self`.
    """
    pass

def _check_same_type(self, other):
    """
    Return True if *self* and *other* are of the same type, False otherwise.
    """
    pass