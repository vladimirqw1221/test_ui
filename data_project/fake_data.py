from dataclasses import dataclass


@dataclass
class DataPerson:
    first_name: str = None
    last_name: str = None
    post_code: str = None
