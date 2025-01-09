from dataclasses import dataclass

class InvalidPostalCodeException(Exception):
    pass

@dataclass(frozen=True)
class PostalCode:
    value: str

    def __post_init__(self):
        if not self._is_valid_berlin_postal_code():
            raise InvalidPostalCodeException(
                f"{self.value} ist keine gültige Berliner PLZ"
            )

    def _is_valid_berlin_postal_code(self) -> bool:
        return (len(self.value) == 5 and self.value.startswith(('10','12','13')))
