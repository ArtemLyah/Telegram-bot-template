from aiogram import Router, Bot
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter 
from aiogram.filters.chat_member_updated import IS_NOT_MEMBER, IS_MEMBER 
from aiogram.types import ChatMemberUpdated
from services.group_service import GroupService
from keyboards.inline.inline_keyboard import inline_keyboard

group_router = Router()
group_service = GroupService()

@group_router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=(IS_NOT_MEMBER >> IS_MEMBER)
    )
)
async def join_group(event: ChatMemberUpdated, bot: Bot):
    chat = event.chat
    group_service.addGroup(chat.id, chat.full_name, chat.type)
    await bot.send_message(chat.id, "Hello", reply_markup=inline_keyboard)