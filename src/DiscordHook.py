from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from src.Log import Log
import requests
import time


class DiscordHook:
    session = requests.Session()

    def __init__(self, webhook):
        self.webhook = webhook

    def report_changes(self, courses):
        if len(courses) == 0:
            Log.info("No file changes detected.")
            return

        Log.info("Sending data to discord webhook...")

        for course in courses:
            description = ""
            for resource in course.resources:
                description += "→ " + resource + "\n"

            Log.info("Sending course " + course.name + ": \n" + description)

            embed = DiscordEmbed(title=course.name, description=description, color='03b2f8')
            embed.set_author(name=datetime.today().strftime('%d.%m.%Y'))

            webhook = DiscordWebhook(url=self.webhook)
            webhook.add_embed(embed)
            response = webhook.execute()

            if response.status_code != 200:
                Log.error(
                    "Discord API returned status code "
                    + str(response.status_code)
                    + " with message \""
                    + response.text
                    + "\"."
                )

            # rate limit
            time.sleep(0.25)
