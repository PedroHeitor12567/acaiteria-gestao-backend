from enum import Enum


class CommandStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    CANCELED = "CANCELED"

class ProductCategory(str, Enum):
    ACAI = "ACAI"
    SORVETE = "SORVETE"
    GUARACAI = "GUARACAI"
    OUTROS = "OUTROS"