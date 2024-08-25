import time
class UrTube:
    users = []
    videos = []
    current_user = None
    def log_in(self, login: str, password: str) -> None:
        """Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с
        такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу."""
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
    def register(self, nickname: str, password: str, age: int) -> None:
        """Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
        "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически."""
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)
    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None."""
        self.current_user = None
    def add(self, *args):
        """Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит."""
        for movie in args:
            self.videos.append(movie)
    def get_videos(self, text: str) -> list:
        """Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке
        'Urban the best' (не учитывать регистр)."""
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie
    def watch_video(self, movie: str) -> None:
        """Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит, ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается."""
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
    def __str__(self):
        return f"{self.videos}"
class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = time_now  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)
    def __str__(self):
        return f"{self.title}"
class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname  # имя пользователя, строка
        self.password = password  # в хэшированном виде, число
        self.age = age  # возраст, число
    def __str__(self):
        return f'{self.nickname}'
    def __eq__(self, other):
        return self.nickname == other.nickname
    def __hash__(self):
        return hash(self.password)
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    ur.add(v1, v2)
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    ur.watch_video('Лучший язык программирования 2024 года!')