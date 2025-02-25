from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from orienteer.general.config import TOKEN_PURCHASE
from orienteer.general.data.orienteer.services.transactions import get_balance, spend
from orienteer.general.data.ss14.repositories.player import get_user_id

router = APIRouter()

@router.post("/api/purchases")
async def handle_purchase(request: Request):
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN_PURCHASE}":
        raise HTTPException(status_code=401, detail="Wrong token")

    # Получение данных из запроса. Может измениться сам запрос позже (название предмета куда-то бы надо впихнуть)
    data = await request.json()
    ckey = data.get("ckey")
    price = data.get("price")

    if not ckey or price is None:
        raise HTTPException(status_code=400, detail="Incorrect data")

    # Получение user_id по ckey (С ССки приходит именно Ckey. Как я понял, нам нужно его преобразовывать к UUID)
    user_id = await get_user_id(ckey)
    if user_id is None:
        raise HTTPException(status_code=404, detail="No player with this ckey")

    # Проверка баланса (Запасная. В игре тоже будет, но чтобы избежать каких-то махинаций от злоумышлинников. Может временно уберу, так как хост бота медленный)
    current_balance = await get_balance(user_id)
    if current_balance < price:
        return JSONResponse(
            content={"Success": False, "Message": "Not enough money", "NewBalance": float(current_balance)},
            status_code=400
        )

    # Списание ориентиков
    await spend(user_id, price)
    new_balance = await get_balance(user_id)  # Сохраняем новый баланс, чтобы вернуть потом это в игру

    return JSONResponse(
        content={"Success": True, "Message": "Purchase completed!!! Yey!", "NewBalance": float(new_balance)}, # Message мне нужна пока для логирования внутри клиента ССки, чтобы понимать где какая ошибка. Может даже лучше будет оставить навсегда
        status_code=200
    )