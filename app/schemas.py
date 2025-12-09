from pydantic import BaseModel

class ClientData(BaseModel):
    кредитный_рейтинг: float
    возраст: float
    стаж_в_банке: float
    баланс_депозита: float
    число_продуктов: int
    есть_кредитка: int
    активный_клиент: int
    оценочная_зарплата: float
    есть_баланс: int
    город: str
    пол: str