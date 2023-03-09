from aiogram.filters.callback_data import CallbackData

class SendExtraData(CallbackData, prefix="extra"):
    message: str
    type_: str