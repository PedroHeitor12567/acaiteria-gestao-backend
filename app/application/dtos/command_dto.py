from dataclasses import dataclass


@dataclass
class AddCommandItemInput:
    product_id: int
    quantity: int