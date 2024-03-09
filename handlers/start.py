from aiogram import types, Router, F
from aiogram.filters.command import Command
from states import TestStates
from keyboards.start_kb import start_kb
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}', reply_markup=start_kb())

@router.callback_query(F.data=='btn1')
async def button_one_pressed(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(TestStates.state_one)
    await call.message.edit_text('Ты нажал на кнопку 1')

@router.callback_query(F.data=='btn2')
async def button_two_pressed(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(TestStates.state_two)
    await call.message.edit_text('Ты нажал на кнопку 2')


