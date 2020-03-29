________________________________________________________________

**ЗАПУСК**
________________________________________________________________

Terminal 1:  
cd backend  
py devmanage.py runserver

Terminal 2:  
cd frontend  
npm run serve

________________________________________________________________

**УСТАНОВКА**
________________________________________________________________

-Директорию backend сделать Source Root:  
Settings -> Project Settings -> Project Structure -> Sources

-Создание и запуск виртуального окружения:  
cd backend  
py -m venv dvenv  
Settings -> Project Settings -> Project Interpreter -> dvenv

-Устнаовка зависимостей:  
pip install django djangorestframework django-cors-headers

-Миграции в БД:  
py devmanage.py makemigrations main  
py devmanage.py migrate

---Linux---
-Установка NVM:  
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash  
source ~/.profile  
nvm ls-remote  
nvm install v12.12.0

-Создание node_modules:  
npm install
------

-Установка vue-cli:  
vue create frontend

-Сборка front  
cd frontend  
npm run build

________________________________________________________________

**ДОПОЛНИТЕЛЬНО**
________________________________________________________________

-Команды Django:  
py devmanage.py createsuperuser  
py devmanage.py dumpdata > dump.json  
py devmanage.py loaddata dump.json

-Создать requirements.txt:  
pip freeze > requirements.txt

-Установить пакеты из requirements.txt:  
pip install -r requirements.txt

-Сборка docker
docker-compose build

-Вывод образов
docker images | head

-Dump docker
docker save drf_vuejs_app:latest > dump.docker

-Отправка на сервер
scp dump.docker root@255.255.255.255:/dump.docker