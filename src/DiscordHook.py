from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import requests


class DiscordHook:
    session = requests.Session()

    def __init__(self, webhook):
        self.webhook = webhook

    def report_changes(self, courses):
        for course in courses:
            description = ""
            for resource in course.resources:
                description += "→ " + resource + "\n"

            embed = DiscordEmbed(title=course.name, description=description, color='03b2f8')
            embed.set_author(name=datetime.today().strftime('%d.%m.%Y'))

            webhook = DiscordWebhook(url=self.webhook)
            webhook.add_embed(embed)
            webhook.execute()
