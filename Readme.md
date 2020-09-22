# ГАЙД ПО ДЕПЛОЮ БОТА НА СЕРВЕРЕ AMAZON с WEBHOOK

## ЭТАП 1: РЕГИСТРАЦИЯ НА СЕРВЕРЕ АМАЗОН
Есть различные сервера. Amazon Web Services, Microsoft Azure, Alibaba Cloud, Google
Мы Выбираем Amazon Web Services
1. [Создаем аккаунт по ссылке](https://aws.amazon.com/ru/ "ссылка")
2. Заполняем. Тип аккаунта – *личный*.
3. Привязываем карту к аккаунту *(виртуальную Тинькофф лишь бы **1$** на счету был)*
4.	Выбираем Базовый план *(бесплатно)*
5.	Входим в консоль
##ЭТАП 2: СОЗДАЕМ ВИРТУАЛЬНУЮ МАШИНУ
1. Заходим в консоль Амазон.
2. Launch Instances - Launch instance
3. Step 1: Выбираем **Ubuntu Server 20.04 LTS (HVM), SSD Volume Type, 64-bit**. Далее **Select**
4. Step 2: Выбираем **t2.micro**. Именно он бесплатный. Нажимаем Next.
5. Step 3: Ничего не меняем, еще раз Next.
6. Step 4: Ничего не меняем, еще раз Next.
7. Step 5: Ничего не меняем, еще раз Next.
8. Step 6: Добавляем правила
* SSH – TCP -port 22 -Source 0.0.0.0/0
* Custom TCP – TCP – port 8080 – Source ::/0 – Webhook
* PostgreSQL – TCP – port 5432 - Source 0.0.0.0/0 - PostgreSQL
* Custom TCP - TCP - port 8443 - Source 0.0.0.0/0, ::/0 - Webhook
9. Step 7: **Launch**
10. Create a new key pair, Key pair name - gavrilka AWS *(можно своё)* 
11. **Download pair key** Запоминаем куда скачали.
12. **Launch instances**
13. Выбираем **View Instances**
## ЭТАП 3: ПОДКЛЮЧЕНИЕ К СЕРВЕРУ
### Вариант PuTTy
1. Записываем свой IPv4. 
2. Устанавливаем PuTTy
3. Запускаем PuTTygen. Conversions - Import key. Выбираем ранее скаченный ключ. Save Private Key. Да. Называем как хотим. Например aws
4. Запускаем PuTTy. Вбиваем ранее записанный IPv4
5. Connection - SSH - Auth - browse - вставляем ключ aws.ppk
6. Session - Saved sessions вбиваем своё название, например AWS и наживаем SAVE
7. Наживаем Open. Да. Вводим логин **ubuntu**.
### Вариант через PyCharm
1. Настраиваем права доступа к файлу ключа. Открываем папку с ключем gavrilkaAWS.pem, у меня это папка Downloads
2. Правый клик по файлу. Свойства - Безопасность - дополнительно. Отключить всё, удалить всё. 
Добавить. Выбрать субъект. 
Вбить имя пользователя на винде. Проверить имя. 
Полный доступ ОК. Применить. Ок.
3. Заходим в PyCharm. Открываем терминал(снизу). Вводим команду, аналогичную моей:
ssh -i E:/downloads/gavrilkaAWS.pem ubuntu@18.216.134.207
(В первый раз придётся еще ввести yes - enter)
## ЭТАП 4: КОМАНДЫ И НАСТРОЙКА СЕРВЕРА
### КОМАНДЫ
* ls **показать файл в текущей директории**
* cd **изменить директорию. Необходимо указать в какую**
* cd /bin **перейти в папку bin**
* cd .. **вернуться на директорую выше**
* mkdir /home/ubuntu/bots **создать папку bots**
* rm -r bots/ **рекурсивное (не пустые) удаление папки bots**
* rm -d bots/ **удалить пустую директорию bots**
* nano name.txt **создание файла name.txt в текущей директории**
* which python3 **где находиться python3**
* python3 -V **узнать версию python3**
* pip3 install -r req.txt Установить необходимые библиотеки
### НАСТРОЙКА
Прописывает данные команды в через SSH. По порядку.
* sudo apt-get update (*Апдейт сервера*)
* sudo apt install python3-pip
* pip3 install -r req.txt **Возможно не надо и докер сам установит всё**
#### Установка супервайзера (возможно не надо для webhook + docker)
* sudo su
* apt-get install supervisor -y
* exit
## ЭТАП 5: ЗАЛИВКА БОТА
### Вариант с git
1. Создаем репозиторий, добавляем весь код в открытый доступ.
2. git clone https:// (указываем ссылку на репозиторий)
### Скопировать всё из PyCharm по SSH
* scp -i E:/downloads/gavrilkaAWS.pem -r <полный путь папки для копирования> ubuntu@IP:/home/ubuntu
### WinSCP (мой выбор)
1. скачиваем WinSCP с офф сайта. Подключаемся используя сохраненное putty соединение.
## ЭТАП 6: УСТАНОВКА DOCKER
1. Убедитесь, что у вас установлен Git. Если нет, поиск google
2. [Скачать докер с офф сайта и установить](https://www.docker.com)
3. Подключаемся к нашему серверу:
ssh -i E:/downloads/gavrilkaAWS.pem ubuntu@18.216.134.207
4. Выполняем следующие команды по установке докере на сервере:
* sudo apt-get install docker docker-compose -y
## Установка PostgreSQL
Скачать с офф сайта и установить. Нам далее потребуется PgAdmin
## ЭТАП 7: СОЗДАНИЕ WEBHOOK КЛЮЧА
1. Подключаемся к серверу по SSH. Заходим под root:
* sudo su
2. Открываем файл ssl_generate.sh Копируем команды и вставляем:
openssl genrsa -out webhook_pkey.pem 2048 &&\
openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
Отвечаем на вопросы. Самое главное **Common name** надо ввести IPv4 сервера
Проверяем что сертификат и ключ создались командой **ls**
## ЗАПУСК DOCKER-COMPOSE
### Настроем дополнительно firewall:
* sudo ufw status
* sudo ufw enable
* sudo ufw allow 8443
* sudo ufw allow 22
### Запуск докера
Убедитесь, что файлы docker, docker-compose.yml загружены в папку бота.
* sudo docker-compose up
* sudo docker-compose up --build (Если были внесены изменения в боте)
### Команды для работы:
* CTRL + Z - отсоединиться от докера.
* Чтобы вернуться обратно в логи: sudo docker-compose up
* CTRL + C - остановить бота. Повторное нажатие убьёт эти процессы.

### Убедиться, что на сервере ничего не запущено:
* sudo su (зайти под root)
* docker ps -a (посмотреть что запущено)
* docker rm bot database (удалить что запущено)
* exit (выйти из root)

