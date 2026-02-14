from fastapi import FastAPI
from pydantic import BaseModel, computed_field, Field, field_validator
from typing import Annotated, Literal
from model.categories import categories


class Userinput(BaseModel):
    price: Annotated[int, Field(..., ge=1, lt=10000000,
                                description="Price of an item")]
    qty_ordered: Annotated[int,
                           Field(..., ge=1, lt=10, description="Quantity")]
    category_name_1: Annotated[str, Field(..., description="Enter category")]

    Month: Annotated[int, Field(..., description="Month")]
    date: Annotated[int, Field(..., description="Date")]

    @field_validator("category_name_1")
    @classmethod
    def validate_category(cls, v: str) -> str:
        v = v.strip()
        for cat in categories:
            if v.lower() == cat.lower():
                return cat  # Return the correct spelling from the list

        raise ValueError(f"Invalid Category: {v}. Allowed: {categories}")

    # @computed_field
    # @property
    # def calculated_mv(self) -> int:
    #     return self.grand_total + self.discount_amount

    # @computed_field
    # @property
    # def total_items_value(self) -> int:
    #     return self.price * self.qty_ordered

    # @computed_field
    # @property
    # def real_extra_fees(self) -> int:
    #     return self.grand_total * self.total_items_value
