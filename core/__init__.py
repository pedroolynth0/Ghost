import datetime
import locale


class SystemInfom:
    def __init__(self):
        pass
   

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e  {} minutos.'.format(now.hour,now.minute)
        return answer

    @staticmethod
    def get_date():
        locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day,now.strftime('%B'),now.year)
        return answer