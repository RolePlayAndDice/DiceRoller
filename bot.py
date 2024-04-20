python
import discord
import random

PERMISSION_INTEGER = 534723950656
client = discord.Client(intents=discord.Intents.default(), permissions=PERMISSION_INTEGER)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/roll'):
        dice = message.content.split()[1].lower()
        num_rolls = 1
        modifier = 0

        if "+" in dice:
            dice, modifier = dice.split("+")
            modifier = int(modifier)
        elif "-" in dice:
            dice, modifier = dice.split("-")
            modifier = -int(modifier)

        if "d" in dice:
            num_dice, dice_type = map(int, dice.split("d"))
        else:
            num_dice = 1
            dice_type = int(dice)

        rolls = [random.randint(1, dice_type) for _ in range(num_dice)]
        total = sum(rolls) + modifier

        await message.channel.send(f"Rolling {num_dice}d{dice_type} + {modifier}...\nResult: {rolls} = {total}")

client.run('MTIyNjMyOTczMjQyNjI0MDAzMA.GoRbd5.dM-xiC_jS1YuP5euZfbO0SkimF797gUT7AxKpg')
