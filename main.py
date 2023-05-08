# мы импортируем из телебота types, она нужна для управления кнопочками
from telebot import types
#телебот сам нужен для работы с pyTelegramBotAPI
import telebot
#sqlite3 нужен для работы с базойданных на языке запросов SQL
import sqlite3
#Эту библиотеку мы добавляем, чтобы декодировать наши изображения в BLOB
#Можно декодировать любой ресурс в формат BLOB(base64) — массив двоичных данных. В СУБД(система управления базами данных) BLOB — специальный тип данных, предназначенный, в первую очередь, для хранения изображений, а также компилированного программного кода.
import base64
#Импортируем библиотеку эмоджи для взаимодействия с ними
import emoji
#Импортируем эту библиотеку для управления копочками.
from aiogram import types

#Класс - представляет собой шаблон для создания объектов, обеспечивающий начальные значения состояний: инициализация полей-переменных и реализация поведения функций или методов.
# Мы создаем класс db в котором инициализируем, как будет происходить соединение
class db:
  #Создаем функцию для инициализации с аргументами (сам, файл с бд)
  def __init__(self, db_file):
    #От себя настраиваем подключение к определенному файлу, который мы укажем позже
    self.connection = sqlite3.connect(db_file)
    # От себя настраиваем курсор, он нам нужен будет для выполнения запросов к базе данным на язке SQL
    self.cursor = self.connection.cursor()

#Подключаем нашего бота по токену выданного BotFather
bot = telebot.TeleBot('')
#Подключаем к нашей базе данных, а точнее к файлу database.db
db = db('database.db')

#Создаем массив с данными для последующего заполнения
addData =[]

#Создаем обработчик событий сообщения @bot.message_handler(commands=['start']), который принимает в себя аргумент команды старт, т.е мы вводим \start, и он это считывает,
# commands=['start'] - это аргумент
@bot.message_handler(commands=['start'])
#Если под обработчиком событий идет функция, то она выполнится после срабатывания обработчика
#Создаем функцию start(message), указываем аргумент message, т.к это стандартный аргумент, и он используется везде
def start(message):
  #Создаем объект markup, в который мы засовываем types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True),
  #row_width=3 - отвечает за количество кнопочек в строке,
  # resize_keyboard=True - отвечает за срабатывания клавиатуры только на 1 раз
  markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  #далее мы создаем объекты item1... и т.д., в которые мы засовывваем кнопки KeyboardButton
  #Уже в скобочках пишем (emoji.emojize('Свинина :pig_face:')),


  item1 = types.KeyboardButton(emoji.emojize('Свинина :pig_face:'))
  item2 = types.KeyboardButton(emoji.emojize('Говядина :cow:'))
  item3 = types.KeyboardButton(emoji.emojize('Баранина :ram:'))
  item4 = types.KeyboardButton(emoji.emojize('Рыба :fish:'))
  item5 = types.KeyboardButton(emoji.emojize('Море продукты :octopus:'))
  item6 = types.KeyboardButton(emoji.emojize('Курица :chicken:'))
  item7 = types.KeyboardButton(emoji.emojize('Выпечка :croissant:'))
  item8 = types.KeyboardButton(emoji.emojize('Салаты :green_salad:'))
  item9 = types.KeyboardButton(emoji.emojize('Супы :pot_of_food:'))
  item10 = types.KeyboardButton(emoji.emojize('Добавить рецепт'))
  #создаем строку markup.row, в нутри указыкаем аргуенты, которые указывают их расположение
  markup.row(item1, item2,item3)
  markup.row(item4, item5, item6)
  markup.row(item7, item8, item9)
  markup.row(item10)
  #я создал переменную с которую поместил текст, который будет использоваться в дальнейшем,<b>какой-то текст</b> обозначает, что какой-то текст между двумя тегами будет выделен жирным курсивом
  first_text = "! Здесь <b>Вы</b> откроете для себя необычные сочетания вкусов, большое пространство для творчества и возможность радовать себя и своих близких вкуснейшими блюдами! Чтобы найти нужный рецепт, введите в строку слово или словосочетание, (например: курица), либо нажмите подходящую кнопку меню. Бот покажет вам разные вариации и способы его приготовления! Так же вы можете делиться с ботом своими рецептами, а мы с удовольствием их опубликуем! Приятного аппетита"
  #далее от лица бота мы отправляем сообщение(первый аргумент - кому отправить, из объекта message, мы взяли чат, а из чата уже id; второй аргумент - какой текст мы хотим отправить, текст указываем в кавычках "Здравствуй, ",
  #знак плюс означает, что мы прибавляем данные переменной в нашем случаем имя пользователя, parse_mode="html" означает, что мы можем использовать некоторые html теги как выше я уже
  #указывал например тег <b>какой-то текст</b>, reply_markup=[markup] - означает, что мы будем использовать клавиатуру с названием которые мы указали выше markup
  bot.send_message(message.chat.id, "Здравствуй, " + str(message.from_user.first_name) + first_text, parse_mode="html",
                   reply_markup=[markup])
#создаем обработчик событий на сообщения и он принимает в виде аргуента вид контента текст, т.е если бы мы просто ввели какой либо текст в чате
@bot.message_handler(content_types=["text"])
#Создаем функцию gettext, в ней мы будем проверять какой текст был введен
def gettext(message):
  #если был введен внутри сообщения текст и он ровнется "Добавить рецепт", то будет происходить следующее действие
  #стрип означает, что могут допускаться проблелы справо и слева от искомого сообщения,он будет выпонять даже если пользователь укажет  "Добавить рецепт              "
  if(message.text.strip() == "Добавить рецепт"):
    #Обращаемся к функции, которую создали ниже с аргументом message
    addname(message)
  # Тут чуть по другому, иначеЕсли был введен внутри сообщения текст и он ровнется "Добавить рецепт", то будет происходить следующее действие
  #иначе если обрабатывается, если не было совпадение с обычным если
  #Ниже все аналогично
  elif(message.text == emoji.emojize('Свинина :pig_face:') or message.text.strip() =="Свинина"):
    #Мы задаем функцию checktype котора также была создана ниже и уже в ней указываем аргументы message, и передаем переменную
    # которую мы проверяем, ее значение используется в фунции для проверки данных с данными с запроса
    checktype(message, "Свинина")
  elif(message.text == emoji.emojize('Говядина :cow:') or message.text.strip() =="Говядина"):
    checktype(message, "Говядина")
  elif(message.text == emoji.emojize('Баранина :ram:') or message.text.strip() =="Баранина"):
    checktype(message, "Баранина")
  elif(message.text == emoji.emojize('Рыба :fish:') or message.text.strip() =="Рыба"):
    checktype(message, "Рыба")
  elif(message.text == emoji.emojize('Море продукты :octopus:') or message.text.strip() =="Море продукты"):
    checktype(message, "Море продукты")
  elif(message.text == emoji.emojize('Курица :chicken:') or message.text.strip() =="Курица"):
    checktype(message, "Курица")
  elif(message.text == emoji.emojize('Выпечка :croissant:') or message.text.strip() =="Выпечка"):
    checktype(message, "Выпечка")
  elif(message.text == emoji.emojize('Салаты :green_salad:') or message.text.strip() =="Салаты"):
    checktype(message, "Салаты")
  elif(message.text == emoji.emojize('Супы :pot_of_food:') or message.text.strip() =="Супы"):
    checktype(message, "Супы")
  #ELse указывает если ни одно из совпадений не срабатывает
  else:
    #В переменную msg мы запихиваем сообщение бота с определенным текстом
    msg = bot.send_message(message.chat.id, "Отправьте корректный ответ", parse_mode="html")
    #В данной функции, бот готовится к следующему шагу, а точнее он ждет ответ от пользователя, также он принимает аргументы(переменную, которую он проверяет на наличие ответа от
    # пользователя и 2 аргумент, это к какой функции он перейдет по завершению в нашем случае это gettext
    bot.register_next_step_handler(msg, gettext)

#Создаем функцию checktype(с локальными переменными message, txt, функция их потребует при инициализации
#def checktype(message, txt) это локальная функция, выше мы указывали ее уже в глобальном плане
#checktype(message, "Баранина") это означает что будет передано сообщение, а переменной txt будет присвоено значение "Баранина"
def checktype(message, txt):
  #Тут мы подключаемся к базе данных с именем database.db
  connect = sqlite3.connect('database.db')
  #Инициализируем курсор для запроса
  cursor = connect.cursor()
  #тут в новой локальной переменной, мы присваиваем значение аргумента функции txt и концертируем в текстовый формат
  type = str(txt)
  #Создаем в переменной запрос(cursor.execute), f указывает, что мы можем вставлять в запрос какую-либо переменную,
  #запрос принимает только 1 аргумент и это сам запрос, запрос находится в двойных кавычках
  #SELECT - означает, что мы делаем выборку; * - означает, что мы выбираем всех колонки из таблицы(можно указать просто название колонки),
  # FROM Menu - означает, что мы берем ИЗ таблицы Меню, таблицы создаются
  # через приложение SqliteStudio в базеданных; WHERE - используется для фильтрации(в прямом переводе ГДЕ), т.е где идет название колонки равное нашей вышеприведенной переменной type
  #По итогу получается: результат = инициализируем запрос(формат"ВЫБРАТЬ ВСЕ ИЗ таблицы меню ГДЕ тип равен значению в переменной тип
  pork_result = cursor.execute(f"SELECT * FROM Menu WHERE Type = '{type}'")
  #В переменную дата, мы засовываем результат запроса с всеми схождениями
  #fetchall() - показать все резуьтаты
  #fetchone() - показать первый результат
  #если посмотреть дата в данный момент то она будет иметь вид двумерного массива: data[[[id][имя]][[id][имя]][[id][имя]][[id][имя]][[id][имя]][[id][имя]]]
  #Если мы хотим обратиться к элементу первого результат то пишем data[0][сюда пишем число столбца, информацию которого мы хотим посмотреть]
  # Если хотим посмотреть id, тогда data[0][0] так как в программировании отчет идет от 0, и мы берем первую переменную и первый столбец
  data = pork_result.fetchall()
  #Здесь мы создаем цикл в котором есть i=0 и цикл будет выполнять пока(range), len() - выведет длину переменную внутри скобок, в скобках пишем какую переменную мы хотим считать
  for i in range(len(data)):
    #В переменную запихиваю путь к изображению
    file = "C:/Users/rykun/Desktop/test/image.jpg"
    #В переменную мы запихиваем переменную data[i][3], это означает, что мы берем 1 пользователя и берем 4-ую полонку, а в ней уже находится наша фотография
    file_base64 = data[i][3]
    #В новую переменную мы засовываем данные из функции base64 из установленной библиотеки, в ней используем декодирование по байтам, а в скобках указываем(переменную, котора хранит в себе
    # информацию для декодирования, изначально мы сохраняет в бд картинки в формате base64, тут уже мы декодируем из base64)
    image_64_decode = base64.decodebytes(file_base64)
    #В новой переменной, мы открываем файл в скобках указываем(название файла, 'wb' для его записи)
    image_result = open('image.jpg', 'wb')
    #К этой же переменной применяем метод write(записать), в скобках указываем, что хотим записать(в данном случае данные из переменной с декодированным текстом)
    # метод - это функция или процедура, принадлежащая какому-то классу или объекту
    image_result.write(image_64_decode)
    #И уже далее в переменную присваиваем открыйтый файл по пути указанный ниже, 'rb' - означает, что доступно только для чтения
    photo = open(f'C:/Users/rykun/Desktop/test/image.jpg', 'rb')
    #Выводим в чат имя блюда
    bot.send_message(message.chat.id, data[i][1])
    # Отравляем от лиц абота сообщение
    bot.send_photo(message.chat.id, photo)

  msg = bot.send_message(message.chat.id, 'Введите название блюда, рецепт которого вы хотите получить')

  bot.register_next_step_handler(msg, allresult)

# функция служит для вывода рецепта
def allresult(message):
  text = message.text
  #try означает что будет выполняться код, до его ошибки, когда вылезает ошибка, идет обращение к except:
  # except: - это обработчик событий при возникновении ошибки в try,
  try:
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    result = cursor.execute(f"SELECT * FROM Menu WHERE Name = '{text}'")
    data = result.fetchall()
    photo = open(f'C:/Users/rykun/Desktop/test/image.jpg', 'rb')
    bot.send_message(message.chat.id, data[0][1])
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, data[0][4])
    bot.send_message(message.chat.id, data[0][5])
  except:
    msg = bot.send_message(message.chat.id, "Вы неправильно ввели название блюда, повторите попытку")
    #Я указываю переобращение к этой же функции, для того, чтобы пользователь заново ввел названгие рецепта и уже функция пошла снова
    bot.register_next_step_handler(msg, allresult)



#Функция служит для запроса названия блюда от пользователя
def addname(message):
  try:
    msg1 = bot.send_message(message.chat.id, "Отправьте название блюда")
    bot.register_next_step_handler(msg1, addtype)
  except:
    msg1 = bot.send_message(message.chat.id, "Отправьте название блюда еще раз")
    bot.register_next_step_handler(msg1, addname)

#Функция служит для того, чтобы добавить тип блюда
def addtype(message):
  try:
    name = message.text
    #Если название блюда НЕ нет то выполняется следующий код
    if (name != None):
      name = message.text
      #Тут мы обращаемся к массиву addData, который былд создан в самом начале, и используем метод append() - добавить в конец, и в скобках указываем что хотим добавить
      addData.append(name)
      markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True,one_time_keyboard=True)
      item1 = types.KeyboardButton(emoji.emojize('Свинина :pig_face:'))
      item2 = types.KeyboardButton(emoji.emojize('Говядина :cow:'))
      item3 = types.KeyboardButton(emoji.emojize('Баранина :ram:'))
      item4 = types.KeyboardButton(emoji.emojize('Рыба :fish:'))
      item5 = types.KeyboardButton(emoji.emojize('Море продукты :octopus:'))
      item6 = types.KeyboardButton(emoji.emojize('Курица :chicken:'))
      item7 = types.KeyboardButton(emoji.emojize('Выпечка :croissant:'))
      item8 = types.KeyboardButton(emoji.emojize('Салаты :green_salad:'))
      item9 = types.KeyboardButton(emoji.emojize('Супы :pot_of_food:'))
      item10 = types.KeyboardButton(emoji.emojize('Добавить рецепт'))
      markup.row(item1, item2, item3)
      markup.row(item4, item5, item6)
      markup.row(item7, item8, item9)
      markup.row(item10)
      msg1 = bot.send_message(message.chat.id, "Отправьте название вида блюда", reply_markup=[markup])
      bot.register_next_step_handler(msg1, addphoto)
    else:
      msg1 = bot.send_message(message.chat.id, "Вы не заполнили название вида блюда, поробуйте еще раз")
      bot.register_next_step_handler(msg1, addtype)
  except:
    msg1 = bot.send_message(message.chat.id, "Вы не заполнили название вида блюда, поробуйте еще раз")
    bot.register_next_step_handler(msg1, addtype)

#Функция служит, для того чтобы добавить фото
def addphoto(message):
  try:
    type = message.text
    #Он проверяет, есть ли среди веденного типа текст с эмоджи и просто текст
    if (type == emoji.emojize('Свинина :pig_face:') or type.strip() == "Свинина"):
      #В переменную type присваивается значение которое мы сверяли
      type = "Свинина"
      #И также добавляем в конец массива
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Говядина :cow:') or type.strip() == "Говядина"):
      type = "Говядина"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Баранина :ram:') or type.strip() == "Баранина"):
      type = "Баранина"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Рыба :fish:') or type.strip() == "Рыба"):
      type = "Рыба"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Море продукты :octopus:') or type.strip() == "Море продукты"):
      type = "Море продукты"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Курица :chicken:') or type.strip() == "Курица"):
      type = "Курица"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Выпечка :croissant:') or type.strip() == "Выпечка"):
      type = "Выпечка"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Салаты :green_salad:') or type.strip() == "Салаты"):
      type = "Салаты"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    elif (type == emoji.emojize('Супы :pot_of_food:') or type.strip() == "Супы"):
      type = "Супы"
      addData.append(type)
      msg = bot.send_message(message.chat.id, "Отправьте фото блюда")
      bot.register_next_step_handler(msg, Ingredients)
    else:
      msg = bot.send_message(message.chat.id, "Выбран невертный тип блюда, повторите попытку")
      bot.register_next_step_handler(msg, addtype)
  except:
    msg = bot.send_message(message.chat.id, "Выбран невертный тип блюда, повторите попытку")
    bot.register_next_step_handler(msg, addphoto)



# Функция открытия изображения в бинарном режиме
def readImage(filename):
  #Открывает файл для чтения в двоичной системе
  fin = open(filename, "rb")
  #открывает считывание файла
  img = fin.read()
  #И возвращает значение
  return img

#Функция для добавления ингридиентов
def Ingredients(message):
  try:
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    #Считываем id(идентификационный номер) отправленного фото
    fileID = message.photo[-1].file_id
    #добавляем в переменную присвоенный файл бота
    file_info = bot.get_file(fileID)
    #В перменную добавляем скачивание файла
    downloaded_file = bot.download_file(file_info.file_path)
    #открываем изображение как новый файл
    with open("image.jpg", 'wb') as new_file:
      #и записываем информацию
      new_file.write(downloaded_file)
    image = open("image.jpg", 'rb')
    #Делаем считывание из файла
    image_read = image.read()
    #Кодируем данные из файла в base64
    image_64_encode = base64.encodebytes(image_read)
    #Добавляем в массив для последующей отправки на сервер
    addData.append(image_64_encode)

    msg = bot.send_message(message.chat.id, "Отправьте ингридиенты блюда")
    bot.register_next_step_handler(msg, Steps)
  except:
    msg = bot.send_message(message.chat.id, "Отправьте фото еще раз")
    bot.register_next_step_handler(msg, Ingredients)

#Функция для добавления Шагов приготовления
def Steps(message):
  #Считываем как сообщение
  Ingredients = str(message.text)
  #далее добавлем в массив
  addData.append(Ingredients)
  msg = bot.send_message(message.chat.id, "Отправьте шаги для приготовления")
  bot.register_next_step_handler(msg, AllAdd)

#Функция для отправки на сервер данных
def AllAdd(message):
  try:
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    Steps = message.text
    #Добавляем шаги в массив
    addData.append(Steps)
    #INSERT INTO(означает вставить в) название таблицы, указываем(названия столбцов), VALUES - означает что будет устанавливаться значения, Плейсхолдеры для значений(?, ?, ?, ?, ?) указываем ","
    #  чтобы далее указать переменные вместо плейсхолдеров которые будут использвоаться (addData[0], addData[1], addData[2], addData[3], addData[4])
    #Плейсхолдер - это текст, который имеет некоторые характеристики реального письменного текста, но является случайным набором слов или сгенерирован иным образом.
    cursor.execute(f'INSERT INTO Menu (Name, Type, Photo, Ingredients, Steps) VALUES(?, ?, ?, ?, ?)',
                   (addData[0], addData[1], addData[2], addData[3], addData[4]))
    #Отправляем потверждение на сервер, чтобы и там тоже все обновилось
    connect.commit()

    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    item1 = types.KeyboardButton(emoji.emojize('Свинина :pig_face:'))
    item2 = types.KeyboardButton(emoji.emojize('Говядина :cow:'))
    item3 = types.KeyboardButton(emoji.emojize('Баранина :ram:'))
    item4 = types.KeyboardButton(emoji.emojize('Рыба :fish:'))
    item5 = types.KeyboardButton(emoji.emojize('Море продукты :octopus:'))
    item6 = types.KeyboardButton(emoji.emojize('Курица :chicken:'))
    item7 = types.KeyboardButton(emoji.emojize('Выпечка :croissant:'))
    item8 = types.KeyboardButton(emoji.emojize('Салаты :green_salad:'))
    item9 = types.KeyboardButton(emoji.emojize('Супы :pot_of_food:'))
    item10 = types.KeyboardButton(emoji.emojize('Добавить рецепт'))
    markup.row(item1, item2, item3)
    markup.row(item4, item5, item6)
    markup.row(item7, item8, item9)
    markup.row(item10)
    bot.send_message(message.chat.id, "Спасибо, мы опубликуем ваш рецепт в ближайшее время.", reply_markup=[markup])
  except:
    msg = bot.send_message(message.chat.id, "Повторите все действия заново")
    bot.register_next_step_handler(msg, addname)





#Делаем так, чтобы бот работал без остановки
bot.polling(none_stop=True)