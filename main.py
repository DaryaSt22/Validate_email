import re
from aiohttp import web


log = []  # Список. В него будут добавляться результаты всех проверок

# Далее создаю регулярное выражение (re)
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

async def validate_email(request):
    data = await request.json()
    email = data.get("email", "")
    valid = EMAIL_REGEX.match(email) is not None

    log.append({"email": email, "valid": valid})
    return web.json_response({"valid": valid})


async def get_log(request):
    return web.json_response(log)


app = web.Application()
app.router.add_post('/validate-email', validate_email)
app.router.add_get('/log', get_log)


if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)


