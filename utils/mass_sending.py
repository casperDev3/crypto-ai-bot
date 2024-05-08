import json
import main


async def global_mass_sending(content, starter_cid):
    with open("db/admins.json", "r") as file:
        all_receivers = json.load(file)

    success_counter = 0
    fail_counter = 0

    for receiver in all_receivers:
        try:
            await main.bot.send_message(receiver, text=content)
            success_counter += 1
        except Exception as err:
            fail_counter += 1
            continue

    report_txt = (f"Звіт: \n"
                  f"Успішно надісланих листів: {success_counter} \n"
                  f"Не доставлено листів: {fail_counter}")

    await main.bot.send_message(starter_cid, report_txt)
