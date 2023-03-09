from aiogram import Router, F, filters, types
from aiogram.enums.chat_type import ChatType
from filters import ChatTypeFilter
from services.user_service import UserService 
from services.group_service import GroupService

users_router = Router()
user_service = UserService()
group_service = GroupService()

@users_router.message(filters.CommandStart())
async def start(message:types.Message):
    chat = message.chat
    group_service.addGroup(chat.id, chat.full_name, chat.type)
    await message.answer("Hello")

@users_router.message(
    ChatTypeFilter(chat_type=ChatType.PRIVATE),
    filters.Command("register")
)
async def register(message:types.Message):
    user = message.from_user
    user_service.addUser(user.id, user.full_name, user.username)
    await message.answer("You have been registered!")

@users_router.message(F.text)
async def echo(message:types.Message):
    await message.answer(message.text)


