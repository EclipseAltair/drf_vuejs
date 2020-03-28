________________________________________________________________

**ЗАПУСК**
________________________________________________________________

Terminal 1:  
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

-Устнаовка плагинов:  
pip install django djangorestframework django-cors-headers

-Миграции в БД:
py devmanage.py makemigrations main  
py devmanage.py migrate

-Скачать nodejs

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
