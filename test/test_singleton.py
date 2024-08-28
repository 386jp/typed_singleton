from typed_singleton import singleton


@singleton
class SingletonTest1:
    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value


@singleton
class SingletonTest2:
    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value


def test_singleton_in_same_class():
    instance_1 = SingletonTest1(1)
    instance_2 = SingletonTest1(2)
    assert instance_1 is instance_2


def test_not_singleton_in_different_class():
    instance_1 = SingletonTest1(1)
    instance_2 = SingletonTest2(2)
    assert instance_1 is not instance_2  # type: ignore[comparison-overlap]


def test_always_use_first_instance():
    instance_1 = SingletonTest1(1)
    instance_2 = SingletonTest1(2)
    assert instance_1.get_value() == 1
    assert instance_2.get_value() == 1
