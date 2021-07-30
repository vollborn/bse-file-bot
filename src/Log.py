from datetime import datetime


class Log:
    __path = "storage/bsefilebot.log"

    @classmethod
    def info(cls, message):
        log_message = "bsefilebot.INFO:    " + message
        cls.__write_log(log_message)

    @classmethod
    def warning(cls, message):
        log_message = "bsefilebot.WARNING: " + message
        cls.__write_log(log_message)

    @classmethod
    def error(cls, message):
        log_message = "bsefilebot.ERROR:   " + message
        cls.__write_log(log_message)

    @classmethod
    def __write_log(cls, message):
        log_message = "[" + cls.__get_timestamp() + "] " + message
        print(log_message)
        try:
            f = open(cls.__path, "a")
            f.write(log_message + "\n")
            f.close()
        except:
            pass

    @classmethod
    def __get_timestamp(cls):
        return datetime.today().strftime('%Y-%m-%d %H:%I:%S')
