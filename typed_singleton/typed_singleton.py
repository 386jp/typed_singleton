"""typed_singleton package.

This package provides a decorator to create singletons.
"""

import threading
from collections.abc import Callable
from typing import Generic, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


class Singleton(Generic[T, P]):
    """Decorator to create singletons."""

    def __init__(self, cls: Callable[P, T]) -> None:
        """Initialize the Singleton class.

        Args:
        ----
            cls (Callable[P, T]): class to be singleton.

        """
        self._cls = cls
        self._instance: T | None = None
        self._lock = threading.Lock()

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        """Return the singleton instance of the class.

        Returns
        -------
            T: Singleton instance of the class.

        """
        with self._lock:
            if self._instance is None:
                self._instance = self._cls(*args, **kwargs)
            return self._instance
