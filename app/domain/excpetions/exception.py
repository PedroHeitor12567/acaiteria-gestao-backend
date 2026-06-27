class DomainError(Exception):
    pass


class CommandNotFoundError(DomainError):
    pass


class ProductNotFoundError(DomainError):
    pass


class CommandItemNotFoundError(DomainError):
    pass


class CommandNotOpenError(DomainError):
    pass


class EmptyCommandError(DomainError):
    pass


class InvalidQuantityError(DomainError):
    pass


class InvalidValueError(DomainError):
    pass


class InactiveProductError(DomainError):
    pass