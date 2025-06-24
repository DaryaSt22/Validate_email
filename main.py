from fastapi import FastAPI, Request
from pydantic import BaseModel
import re


app = FastAPI()

log = []  # Список. В него будут добавляться результаты всех проверок

# Далее создаю регулярное выражение (re)
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

class EmailRequest(BaseModel):
    email: str



