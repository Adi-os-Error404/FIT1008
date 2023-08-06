from __future__ import annotations

from ctypes import py_object
from typing import TypeVar, Generic

T = TypeVar("T")


class ArrayR(Generic[T]):
    def __init__(self, length: int) -> None:
        """Creates an array of references to objects of the given length
        :complexity: O(length) for best/worst case to initialise to None
        :pre: length > 0
        """
        if length < 0:
            raise ValueError("Array length should be larger than or equal to 0.")
        self.array = (length * py_object)()  # initialises the space
        self.array[:] = [None for _ in range(length)]

    def __len__(self) -> int:
        """Returns the length of the array
        :complexity: O(1)
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """Returns the object in position index.
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """Sets the object in position index to value
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        self.array[index] = value

    def index(self, item: T) -> T:
        for index, arr_item in enumerate(self.array):
            if arr_item == item:
                return index
        else:
            raise ValueError("Value does not exist")

    def __str__(self) -> str:
        ret_str = "["
        for i, item in enumerate(self.array):
            ret_str += str(item)
            ret_str += ", "

        ret_str = ret_str[:-2] + "]"
        return ret_str

    @classmethod
    def from_list(cls, l: list[T]) -> ArrayR[T]:
        ret = ArrayR(len(l))
        for x in range(len(l)):
            ret[x] = l[x]
        return ret

    def to_list(self) -> list[T]:
        ret = []
        for x in range(len(self)):
            ret.append(self[x])
        return ret
