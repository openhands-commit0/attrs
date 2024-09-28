"""
Commonly used hooks for on_setattr.
"""
from . import _config
from .exceptions import FrozenAttributeError

def pipe(*setters):
    """
    Run all *setters* and return the return value of the last one.

    .. versionadded:: 20.1.0
    """
    pass

def frozen(_, __, ___):
    """
    Prevent an attribute to be modified.

    .. versionadded:: 20.1.0
    """
    pass

def validate(instance, attrib, new_value):
    """
    Run *attrib*'s validator on *new_value* if it has one.

    .. versionadded:: 20.1.0
    """
    pass

def convert(instance, attrib, new_value):
    """
    Run *attrib*'s converter -- if it has one -- on *new_value* and return the
    result.

    .. versionadded:: 20.1.0
    """
    pass
NO_OP = object()