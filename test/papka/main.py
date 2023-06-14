# Задача №1 unit-tests
# Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование»
# нужно написать тесты на любые 3 задания из Лекции 4. Необходимо использовать своё решение
# домашнего задания.

# При написании тестов не забывайте использовать параметризацию.
# Рекомендации по тестам.

# Если у вас в функциях информация выводилась(print), то теперь её лучше возвращать(return)
# чтобы можно было протестировать
import requests
# Задание №1

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
def better_web(stats):
  best = max(stats, key=stats.get)
  return best
# print(f'\nЗадание №1\n{better_web(stats)}')

# Задание №2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def my_list(ids):
  list_ = []
  list_ = list(set(ids['user1']) | set(ids['user3']) | set(ids['user2']))
  return list_
# print(f'\nЗадание №2\n{my_list(ids)}')
# Ответ:[98, 35, 213, 54, 119, 15]

# Задание №3

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def geo(geo_logs):
  geo_logg =[]
  for i in range (len(geo_logs)):
    if geo_logs[i]['visit'+str(i+1)][1] =='Россия':#print (geo_logs[i]['visit'+str(i+1)][0])
      geo_logg.append((geo_logs[i]['visit'+str(i+1)][0]))
  return geo_logg
                       
# print(f'\nЗадание №3\n{geo(geo_logs)}')
# Ответ:['Москва', 'Владимир', 'Тула', 'Тула', 'Курск', 'Архангельск']

# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий
# создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные
# отрицательные тесты на ответы с ошибкой

# Пример положительных тестов:

# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

token_ya = ''

def get_headers(token): #создаем аторизацию (токен и все дела)
    return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }
def get_foldres(): # Создаем папку на Ya диске
    foldres = 'new_foldres' #название папки
    file_url = 'https://cloud-api.yandex.net/v1/disk/resources/' # путь
    headers = get_headers(token_ya) #передаем токен
    res_d = requests.delete(f'{file_url}?path={foldres}',headers=headers) #удаление папки
    #print(res_d.status_code)
    res_c = requests.put(f'{file_url}?path={foldres}',headers=headers) # сам запрос

    #print(res_c.status_code)
    return res_c.status_code

get_foldres()