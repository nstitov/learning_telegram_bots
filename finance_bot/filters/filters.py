import re
from typing import Literal

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsCorrectTransaction(BaseFilter):
    async def __call__(
        self, message: Message
    ) -> bool | dict[Literal["expense_name", "cost"], str | float]:
        # TODO: expense name can consist two and more words, need other regular expr
        transaction_pattern = r"\w+\s\d+[.,]?\d*?"
        if re.fullmatch(transaction_pattern, message.text):
            expense_name, cost = message.text.split()
            cost = float(cost.replace(",", "."))
            transaction = {"expense_name": expense_name.capitalize(), "cost": cost}
            return transaction
        return False
