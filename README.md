![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Setup

#### Create Virtual Environment
``` bash
python -m venv venv
```

#### Activate Virtual Environment
``` bash
venv\Scripts\activate.ps1 # Powershell
venv\Scripts\activate.bat # CMD
source venv/bin/activate # Linux
```

#### Get Project Dependencies
``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Build Database
``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json
```

### Docker Option
``` bash
docker build -t <image_name> .
docker run -p 2002:2002 <image_name>
```

### Default Admin
```
username = admin
email = admin@admin.com
password = admin
```
