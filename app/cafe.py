from datetime import date
from typing import Dict
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:

        if "vaccine" not in visitor:
            name = visitor["name"]
            raise NotVaccinatedError(f"{name} is not vaccinated.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if not isinstance(expiration_date, date):
            raise ValueError("Expiration date must be a datetime.date object.")
        if expiration_date < date.today():
            raise OutdatedVaccineError(f"{visitor["name"]}'s"
                                       f" vaccine expired on"
                                       f" {expiration_date}.")

        wearing_a_mask = visitor.get("wearing_a_mask", False)
        if not wearing_a_mask:
            raise NotWearingMaskError(f"{visitor["name"]}"
                                      f" is not wearing a mask.")

        return f"Welcome to {self.name}"
