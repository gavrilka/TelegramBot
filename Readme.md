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
### НАСТРОЙКА
* sudo apt-get update (*Апдейт сервера*)
* sudo apt install python3-pip
## ЭТАП 5: СОЗДАНИЕ WEBHOOK КЛЮЧА
## ЭТАП 6: ЗАЛИВКА БОТА И ЗАПУСК DOCKER-COMPOSE





Security Groups:
Inbound rules:




