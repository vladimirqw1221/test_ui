from enum import Enum


class PytestEnum(Enum):

    @classmethod
    def pytest_data(cls):
        return list(map(lambda x: x.value, cls))
