import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Pega o primeiro contato da lista
    first_friend = client.get_user(client.friends[0].id)
    # Envia a mensagem pro primeiro amigo
    await first_friend.send("TESTE")

client.run('MTA2Njg0ODY5OTgwMTY3MzczOA.GmwN_V.NAD-1hGLtne1qmaRWLEbOswOswJMOV61Mzz3nI')
