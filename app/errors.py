class VaccineError(Exception):
    """Базовый класс для ошибок, связанных с вакцинацией."""
    pass


class NotVaccinatedError(VaccineError):
    """Исключение для посетителей без вакцины."""
    pass


class OutdatedVaccineError(VaccineError):
    """Исключение для просроченной вакцины."""
    pass


class NotWearingMaskError(Exception):
    """Исключение для посетителей без маски."""
    pass
