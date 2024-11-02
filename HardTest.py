import hashlib       # Имортируем модуль для хэширования паролей
import time          # Имортируем модуль для работы с временем


class User:                                                                   # Класс пользователя
    def __init__(self, nickname, password, age):                             # Конструктор класса
        self.nickname = nickname                                            # Никнейм пользователя
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod                                                             # Статический метод для хэширования пароля
    def hash_password(password):                                             # Метод для хэширования пароля
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)       # Возвращаем хэшированное значение пароля


class Video:    # Класс видео
    def __init__(self, title, duration, adult_mode=False):    # Конструктор класса
        self.title = title                                   # Название видео
        self.duration = duration                            # Длительность видео
        self.time_now = 0                                  # Текущее время
        self.adult_mode = adult_mode                      # Режим для взрослых


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):       # Метод для входа в аккаунт
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)       # Хэшируем пароль и сравниваем с хэшем из базы
        for user in self.users:                                                       # Проверяем всех пользователей
            if user.nickname == nickname and user.password == hashed_password:       # Если пароли совпадают, авторизуем пользователя
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user                                             # Автоматический вход после регистрации

    def log_out(self):                                                         # Метод для выхода из аккаунта
        self.current_user = None                                             # Отключаем текущего пользователя

    def add(self, *videos):                                                # Метод для добавления видео
        for video in videos:                          # Проверяем, не добавлено ли видео с таким же названием уже в базу
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, keyword):                                        # Метод для получения видео по ключевому слову
        keyword_lower = keyword.lower()                                     # Приводим ключевое слово к нижнему регистру
        return [video.title for video in self.videos if keyword_lower in video.title.lower()]    # Возвращаем список найденных видео

    def watch_video(self, title):                                                            # Метод для просмотра видео
        if not self.current_user:                                 # Если пользователь не авторизован, выходим из функции
            print("Войдите в аккаунт, чтобы смотреть видео")      # Выходим из функции
            return

        video = next((v for v in self.videos if v.title == title), None)     # Находим видео по названию

        if not video:                                                        # Если видео не найдено, выходим из функции
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:       # Если видео является для взрослых и пользователь моложе 18 лет, выходим из функции
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        while video.time_now < video.duration:             # Если время просмотра меньше длительности видео
            print(video.time_now + 1)                     # Выводим текущее время просмотра
            time.sleep(0.5)                              # Пауза в половину секунды для имитации просмотра
            video.time_now += 1

        print("Конец видео")
        video.time_now = 0                         # Сброс времени просмотра


# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
