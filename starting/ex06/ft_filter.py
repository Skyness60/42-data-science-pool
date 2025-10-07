from typing import Iterable, Any, Callable


def ft_filter(function: Callable[[Any], bool],
              iterable: Iterable[Any]) -> Iterable[Any]:
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
