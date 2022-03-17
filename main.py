from javascript import require

discord = require("discord.js")

client = discord.Client()

client.on("ready", lambda: print("ready"))

