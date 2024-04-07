python
import discord
import random
import re

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/roll'):
        try:
            dice_expr = message.content.split(' ')[1]
            results = []
            total = 0
            for match in re.finditer(r'(\d+d\d+|\d+|d4|d6|d8|d10|d12|d20)', dice_expr):
                dice_str = match.group()
                if 'd' in dice_str:
                    if dice_str.startswith('d'):
                        num_sides = int(dice_str[1:])
                        roll = random.randint(1, num_sides)
                        results.append(roll)
                        total += roll
                        await message.channel.send(f'Rolled d{num_sides}: {roll}')
                    else:
                        num_dice, num_sides = map(int, dice_str.split('d'))
                        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
                        results.extend(rolls)
                        total += sum(rolls)
                        await message.channel.send(f'Rolled {num_dice}d{num_sides}: {rolls}')
                else:
                    modifier = int(dice_str)
                    total += modifier
                    await message.channel.send(f'Added modifier: {modifier}')

            await message.channel.send(f'Total: {total} [{results}]')
        except:
            await message.channel.send('Invalid input. Please use the format /roll [dice_expression]')

client.run('DISCORD_TOKEN')
