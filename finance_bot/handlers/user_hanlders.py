from datetime import date
from typing import Literal

from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.filters import IsCorrectTransaction
from handlers.command_handlers import FSMAddTransaction

router = Router()


@router.message(StateFilter(FSMAddTransaction.fill_transaction))
@router.message(IsCorrectTransaction())
async def process_correct_transaction(
    message: Message,
    transaction: dict[Literal["expense_name", "cost"], str | float],
    i18n: dict[str, str],
    state: FSMContext,
):
    created_date = date.today().isoformat()
    await state.update_data(
        expense_name=transaction["expense_name"],
        cost=transaction["cost"],
        created_date=created_date,
        amount=1,
        comment=None,
    )
    await state.set_state(FSMAddTransaction.confirm_transaction)
    await message.answer(
        text=i18n["transaction_info"].format(
            expense_name=transaction["expense_name"],
            category_name=category_name,
            cost=transaction["cost"],
            amount=1,
            created_date=created_date,
            comment="",
        )
    )
