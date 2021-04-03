import json
import discord


async def count_command(user, command):
    user = str(user)
    with open('command_count.txt', 'r') as file:
        line = str(file.readline())

    loaded_data = json.loads(line)

    if user not in loaded_data.keys():
        loaded_data[user] = {}
    if command not in loaded_data[user].keys():
        loaded_data[user][command] = 1
    else:
        loaded_data[user][command] += 1
    with open('command_count.txt', 'w+') as file2:
        print(loaded_data)
        file2.truncate()
        json.dump(loaded_data, file2)


async def get_count(user, command):
    user = str(user)
    with open('command_count.txt', 'r') as file:
        line = str(file.readline())

    loaded_data = json.loads(line)
    if user not in loaded_data.keys():
        loaded_data[user] = {}
    if command not in loaded_data[user].keys():
        return 0
    return int(loaded_data[user][command])


async def easter_egg_animal_lover(user):
    animal_call_count = await get_count(user.id, "dog") + await get_count(user.id, "cat")
    if animal_call_count >= 5:
        role = discord.utils.get(user.guild.roles, name="Animal Lover")
        if role not in user.roles:
            await user.add_roles(role)