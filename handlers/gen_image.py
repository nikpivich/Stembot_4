from aiogram import Router, F, flags
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile
import keyboards.for_base
from kandinski.generate_image import generate
from keyboards import for_base
from states import Gen

router = Router()

@router.callback_query(F.data == 'generate_image')
async def cmd_gen_image(clb: CallbackQuery, state : FSMContext):
    await state.set_state(Gen.image_prompt)
    await clb.message.edit_text('Отправте текст запроса')
    await clb.message.answer('Флаг генерации', reply_markup=for_base.exit_keyboard)


@router.message(Gen.image_prompt)
@flags.chat_action('upload_photo')
async def generate_image(message:Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    prompt = (data["number"])
    await message.reply(f'Ваш промпт: {prompt}\nГенерирую...')
    photo_obj = FSInputFile(f"{generate(prompt)}")
    await message.delete()
    await message.answer_photo(photo_obj, caption="Вот ваше фото",
                               reply_markup=keyboards.for_base.iexit_keyboard)