from dotenv import load_dotenv
from src.FileFetcher import FileFetcher
from src.FileCompare import FileCompare
from src.DiscordHook import DiscordHook
import os


class Kernel:
    def __init__(self):
        load_dotenv()
        self.username = os.getenv("MOODLE_USERNAME")
        self.password = os.getenv("MOODLE_PASSWORD")
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")

    def exec(self):
        fileFetcher = FileFetcher(self.username, self.password)
        current_courses = []
        if fileFetcher.login() and fileFetcher.get_courses():
            current_courses = fileFetcher.courses
        else:
            print("Login failed.")
            exit()

        fileCompare = FileCompare()
        new_courses = fileCompare.compare(current_courses)

        if self.discord_webhook:
            discordHook = DiscordHook(self.discord_webhook)
            discordHook.report_changes(new_courses)
