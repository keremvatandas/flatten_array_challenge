from collections.abc import Iterable
from typing import Any, List


async def flatten_array(array: List[Any]) -> List[int]:
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    flat_array: List[int] = []
    for item in array:
        if isinstance(item, Iterable):
            # flat_array += flatten_array(item)
            flat_array.extend(await flatten_array(item))
        else:
            flat_array.append(item)
    return flat_array


def flatten_array2(array: List[Any]):
    for item in array:
        if not isinstance(item, Iterable):
            yield item
        else:
            yield from flatten_array2(item)
