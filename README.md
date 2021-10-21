# karen

karen is a Discord Bot that will check for a list of forbiden words / expressions, removing the message that contains them and replying with another message. Everything is highly custumizable.

After you've created your Discord App, you should create a new `.env` file from `.env.example` and edit accordingly (or you can export all of the variables on `.env.example`).

- `DISCORD_TOKEN` will be used to authenticate your bot to Discord
- `BANNED_SENTENCES` is the list, without any quotation marks, comma-separated, of the words / expressions you want to look out for
- `RESPONSES` is the list, without any quotation marks, comma-separated, of the words / expressions you want to use as a reply. It will pick one sentence randomly
- `EMOJIS` is the list, without any quotation marks, comma-separated, of the emojis you want to append to your reply. It will pick one emoji randomly
