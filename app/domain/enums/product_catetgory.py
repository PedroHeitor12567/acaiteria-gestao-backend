from enum import Enum

class ProductCategory(str, Enum):
    ACAI = "ACAI"
    SORVETE = "SORVETE"
    GUARACAI = "GUARACAI"
    OUTROS = "OUTROS"