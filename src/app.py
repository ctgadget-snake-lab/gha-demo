import time
import asyncio

from pydantic import BaseModel, validator
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    """
    Represents an item with a name and price.

    Attributes:
        name (str): The name of the item.
        price (float): The price of the item.

    """

    @validator("price")
    def price_must_be_positive(cls, value):
        """
        Validates that the price is a positive value.

        Args:
            value (float): The price to be validated.

        Returns:
            float: The validated price if it is positive.

        Raises:
            ValueError: If the price is not a positive value.
        """
        if value <= 0:
            raise ValueError(f"we expect price >= 0, we received {value}")
        return value


@app.get("/")
def root():
    """
    Root endpoint that returns a simple message.

    Returns:
        dict: A dictionary containing a "message" key with the value "hello world again".
    """
    return {"message": "hello world again"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    """
    Get information about a user by their user ID.

    Args:
        user_id (str): The unique identifier of the user.

    Returns:
        dict: A dictionary containing the "user_id" key with the provided user ID.
    """
    return {"user_id": user_id}


@app.post("/items/")
def create_item(item: Item):
    """
    Create a new item.

    Args:
        item (Item): The item to be created.

    Returns:
        Item: The created item.
    """
    return item


@app.get("/sleep_slow")
def sleep_slow():
    """
    Endpoint that sleeps for 1 second synchronously and then returns a status message.

    Returns:
        dict: A dictionary containing a "status" key with the value "done" after sleeping.
    """
    _ = time.sleep(1)
    return {"status": "done"}


@app.get("/sleep_fast")
async def sleep_fast():
    """
    Endpoint that sleeps for 1 second asynchronously and then returns a status message.

    Returns:
        dict: A dictionary containing a "status" key with the value "done" after sleeping.
    """
    _ = await asyncio.sleep(1)
    return {"status": "done"}
