**Оповідач:** Ласкаво просимо, студенти, на першу лекцію нашого курсу веб-розробки Flask. Сьогодні ми розглянемо
основи створення програми Flask, включаючи встановлення Flask, визначення маршрутів і переглядів, використання шаблонів,
обслуговування статичні файли та обробка форм. Давайте розпочнемо.

**Встановити Flask**

[На екрані показано вікно терміналу з командою ]

**Оповідач:** Відкрийте термінал або командний рядок і встановіть Flask за допомогою pip.

```bash
pip install Flask
```

**Створіть додаток Flask**

[На екрані показано редактор коду з кодом Flask]

**Екранний диктор:** створіть новий файл під назвою `app.py` і напишіть наступний код, щоб створити базову програму
Flask.

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
	return 'Hello World!'


if __name__ == '__main__':
	app.run(debug=True)
```

**Запустіть програму**

[На екрані показано вікно терміналу з командою ]

**Оповідач:** У терміналі перейдіть до каталогу, що містить `app.py`, і виконайте наведену нижче команду, щоб запустити
додаток.

```bash
python app.py
```

**Шаблони**

[На екрані показано редактор коду з кодом шаблону Flask]

**Екранний диктор:** Давайте змінимо функцію `hello`, щоб використовувати шаблон замість повернення жорстко закодованого
рядка. Створіть новий
папку під назвою `templates`, а всередині цієї папки створіть новий файл під назвою `index.html`. Додайте наступний код.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
<h1>{{ message }}</h1>
</body>
</html>
```

[На екрані показано редактор коду з оновленим кодом Flask]

**Екранний диктор:** оновіть функцію `hello` в `app.py`, щоб використовувати новий шаблон.

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('index.html', message='Hello World!')


if __name__ == '__main__':
	app.run(debug=True)
```

**Запустіть програму**

[На екрані показано вікно терміналу з командою ]

**Екранний диктор:** збережіть зміни та в терміналі скористайтеся командою `Ctrl+C`, щоб зупинити попередню програму, а
потім
виконайте таку команду, щоб запустити оновлену програму.

```bash
python app.py
```

[На екрані показано вікно браузера з написом "Hello World!" повідомлення  ]

**Екранний диктор:** Відкрийте свій веб-браузер і перейдіть до `http://127.0.0.1:5000/`, щоб побачити оновлений "Hello
World!" повідомлення.

**Шаблони з даними**

[На екрані показано редактор коду з оновленим кодом шаблону Flask]

**Оповідач:** Давайте змінимо шаблон `index.html`, щоб приймати динамічні дані з програми Flask. Оновити
код шаблону наступним чином.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello {{ name }}</title>
</head>
<body>
<h1>Hello {{ name }}!</h1>
</body>
</html>
```

[На екрані показано редактор коду з оновленим кодом Flask]

**Екранний диктор:** оновіть функцію `hello` в `app.py`, щоб передати назву шаблону.

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello(name='World'):
	return render_template('index.html', name=name)


if __name__ == '__main__':
	app.run(debug=True)
```

[На екрані показано вікно браузера з написом "Hello World!" повідомлення оновлено на "Привіт [ваше ім'я]!" повідомлення]

**Екранний диктор:** збережіть зміни та оновіть веб-переглядач, щоб побачити оновлене повідомлення. Ви також можете
змінити `app.py`
файл для прийняття параметра запиту для передачі імені шаблону. Наприклад, `http://127.0.0.1:5000/?name=John` буде
відобразити "Hello John!" повідомлення.

**Статичні файли**

[На екрані показано редактор коду з кодом Flask для обслуговування статичних файлів]

**Оповідач:** Давайте модифікуємо програму Flask для обслуговування статичних файлів, таких як зображення, CSS і
JavaScript. Створити
нову папку під назвою `static`, а всередині цієї папки створіть новий файл під назвою `style.css`. Додайте наступний код
до `style.css`.

```css
body {
    color: #333;
    font-family: Arial, sans-serif;
}
```

[На екрані показано редактор коду з оновленим кодом Flask]

**Екранний диктор:** оновіть функцію `hello` в `app.py`, щоб обслуговувати файл `style.css`.

```python
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('index.html', message='Hello World!')


@app.route('/static/<path:filename>')
def send_file(filename):
	return send_from_directory('static', filename)


if __name__ == '__main__':
	app.run(debug=True)
```

[На екрані показано код шаблону з посиланням на статичний файл]

**Екранний диктор:** Оновіть шаблон `index.html`, включивши файл `style.css`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <link rel="stylesheet" href="{{ url_for('send_file', filename='style.css') }}">
</head>
<body>
<h1>{{ message }}</h1>
</body>
</html>
```

[На екрані показано вікно браузера з написом "Hello World!" повідомлення та застосований CSS]

**Екранний диктор:** збережіть зміни та оновіть веб-переглядач, щоб переглянути оновлене повідомлення із застосованим
CSS.

**Форми**

[На екрані показано редактор коду з кодом форми Flask]

**Оповідач:** Давайте створимо просту контактну форму в програмі Flask. Створіть новий файл під назвою `forms.py` і
додайте
наступний код.

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])


email = StringField('Email', validators=[DataRequired(), Email()])
submit = SubmitField('Send')
```

[На екрані показано редактор коду з оновленим кодом Flask]

**Екранний диктор:** Оновіть файл `app.py`, включивши файл `forms.py`, і створіть новий маршрут для обробки форми
подання.

```python
from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from forms import ContactForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	
	if form.validate_on_submit():
		# process the form data here
		# for example, send an email
		flash('Your message has been sent!')
		return 'Success!'
	return render_template('contact.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)
```

[На екрані показано редактор коду з оновленим кодом шаблону]

**Екранний диктор:** Оновіть шаблон `index.html`, щоб включити контактну форму.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <link rel="stylesheet" href="{{ url_for('send_file', filename='style.css') }}">
</head>
<body>
<h1>{{ message }}</h1>
<form method="post" action="/" enctype="multipart/form-data">
    {{ form.hidden_tag() }}
    <p>
        <label for="name">Name:</label>
        {{ form.name.label }}
        {{ form.name(size=32) }}
    </p>
    <p>
        <label for="email">Email:</label>
        {{ form.email.label }}
        {{ form.email(size=32) }}
    </p>
    <p>
        {{ form.submit() }}
    </p>
</form>
</body>
</html>
```

[На екрані показано редактор коду з оновленим кодом шаблону для контактної форми]

**Екранний диктор:** оновіть шаблон `contact.html`, щоб відобразити повідомлення про успішне виконання після надсилання
форми.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
    <link rel="stylesheet" href="{{ url_for('send_file', filename='style.css') }}">
</head>
<body>
{% if message %}
<p>{{ message }}</p>
{% endif %}
<form method="post" action="/" enctype="multipart/form-data">
    {{ form.hidden_tag() }}
    <p>
        <label for="name">Name :</label>
        {{ form.name.label }}
        {{ form.name(size=32) }}
    </p>
    <p>
        <label for="email">Email:</label>
        {{ form.email.label }}
        {{ form.email(size=32) }}
    </p>
    <p>
        {{ form.submit() }}
    </p>
</form>
</body>
</html>
```

[На екрані показано вікно браузера з написом "Hello World!" повідомлення та контактна форма]

**Екранний диктор:** збережіть зміни та оновіть веб-переглядач, щоб переглянути оновлене повідомлення та контактну
форму. Ви можете зараз
протестуйте контактну форму, заповнивши поля та відправивши форму.

**Резюме**

У цій лекції ми розглянули основи створення програми Flask, включаючи встановлення Flask, визначення маршрутів і
перегляди, використання шаблонів, обслуговування статичних файлів і обробки форм. Ми також розповіли, як створити просту
контактну форму
за допомогою Flask і WTForms. У наступній лекції ми розглянемо інтеграцію бази даних та автентифікацію користувачів.

**Оповідач:** Ось і все на сьогодні, студенти. Сподіваюся, ви знайшли цю лекцію інформативною. Якщо у вас є якісь
питання, відчувайте
можна вільно запитати на дискусійному форумі або під час сесії запитань і відповідей після лекції. До зустрічі на
наступній лекції!

**Оповідач:** Перш ніж завершити сьогоднішню лекцію, давайте розглянемо кілька додаткових прикладів і вправ, щоб ви
практикувати те, що ми навчилися.

**Приклад: обслуговування статичних файлів у підкаталозі**

[На екрані показано редактор коду з кодом Flask для обслуговування статичних файлів із підкаталогом]

**Оповідач:** Давайте модифікуємо програму Flask для обслуговування статичних файлів із підкаталогу під
назвою `static2`. Створити
нову папку під назвою `static2`, а всередині цієї папки створіть новий файл під назвою `image.jpg`.

```python
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/static/<path:filename>')
def send_file(filename):
	return send_from_directory('static', filename)


@app.route('/static2/<path:filename>')
def send_file2(filename):
	return send_from_directory('static2', filename)


if __name__ == '__main__':
	app.run(debug=True)
```

[На екрані показано код шаблону з посиланням на статичний файл у підкаталозі]

**Екранний диктор:** оновіть шаблон `index.html`, щоб включити посилання на зображення у підкаталозі.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <link rel="stylesheet" href="{{ url_for('send_file', filename='style.css') }}">
</head>
<body>
<h1>{{ message }}</h1>
<img src="{{ url_for('send_file2', filename='image.jpg') }}" alt="Image">
</body>
</html>
```

[На екрані показано вікно браузера з написом "Hello World!" повідомлення та зображення в підкаталозі]

**Екранний диктор:** збережіть зміни та оновіть веб-переглядач, щоб побачити оновлене повідомлення та зображення.

**Вправа: створити новий маршрут і шаблон**

[На екрані показано редактор коду з кодом Flask для створення нового маршруту та шаблону]

**Оповідач:** Давайте створимо новий маршрут і шаблон для сторінки «Про нас». Створіть новий файл під
назвою `about.html` папку `templates`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us</title>
    <link rel="stylesheet" href="{{ url_for('send_file', filename='style.css') }}">
</head>
<body>
<h1>About Us</h1>
<p>We are a team of passionate developers who love building web applications using Flask.</p>
</body>
</html>
```

[На екрані показано редактор коду з кодом Flask для визначення нового маршруту для сторінки «Про нас»]

**Екранний диктор:** оновіть файл `app.py`, щоб визначити новий маршрут для сторінки "Про нас".

```python
@app.route('/about')
def about():
	return render_template('about.html')
```

[На екрані показано вікно браузера зі сторінкою «Про нас» ]

**Екранний диктор:** Збережіть зміни та перейдіть до `http://127.0.0.1:5000/about` у веб-браузері, щоб переглянути нову
«Про
Сторінка нас».

**Вправа: створити форму з перевіркою електронної пошти**

[На екрані показано редактор коду з кодом форми Flask для створення форми з перевіркою електронної пошти]

**Оповідач:** Давайте змінимо контактну форму, щоб включити перевірку електронної пошти за допомогою Flask-WTF. Оновіть
клас `ContactForm`
у `forms.py`, щоб включити засіб перевірки `Електронна пошта`.

```python
class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Send')
```

**Екранний диктор:** збережіть зміни у `forms.py` та оновіть маршрут `contact` у `app.py`, щоб використовувати оновлений
клас `ContactForm`.

```python
@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		# process the form data here
		# for example, send an email
		flash('Your message has been sent!')
		return 'Success!'
	return render_template('contact.html', form=form)
```

[На екрані показано вікно браузера з контактною формою з підтвердженням електронної пошти]

**Екранний диктор:** збережіть зміни та оновіть веб-переглядач, щоб побачити оновлену контактну форму з підтвердженням
електронної пошти.

Це все на сьогоднішній лекції, студенти. Сподіваюся, ця вправа була для вас корисною. Якщо у вас виникли запитання, не
соромтеся
запитати на дискусійному форумі або під час сесії запитань і відповідей після лекції. У наступній лекції ми розглянемо
базу даних
інтеграція та аутентифікація користувачів.

**Оповідач:** Ось і все на сьогодні, студенти. Сподіваюся, ви знайшли цю лекцію інформативною. Якщо у вас є якісь
питання, відчувайте
можна вільно запитати на дискусійному форумі або під час сесії запитань і відповідей після лекції. До зустрічі на
наступній лекції!

**Оповідач:** Перш ніж перейти до наступної теми, давайте коротко нагадаємо, що ми розглянули на сьогоднішній лекції.

У цій лекції ми розглянули такі теми:

1. Обслуговування статичних файлів
2. Створення маршрутів і шаблонів
3. Обробка форм
4. Обслуговування статичних файлів із підкаталогу
5. Створення нового маршруту та шаблону
6. Використання перевірки електронної пошти у формах

[Екран показує фрагменти коду та приклади з лекції]

**Оповідач:** Ми почали з вивчення того, як обслуговувати статичні файли за допомогою вбудованої у Flask
функції `send_file`. Ми також
навчилися визначати маршрути та шаблони для відображення динамічного вмісту. Потім ми розглянули форми обробки за
допомогою Flask-WTF,
і як обслуговувати статичні файли з підкаталогу.

[Екран показує попередній перегляд теми наступної лекції]

**Оповідач:** У наступній лекції ми розглянемо інтеграцію бази даних і автентифікацію користувачів за допомогою
Flask-SQLAlchemy
і Flask-Login. Ми навчимося створювати схему бази даних, визначати моделі та виконувати CRUD (створення, читання,
оновлення,
Видалити) за допомогою Flask-SQLAlchemy. Ми також дізнаємося, як реалізувати автентифікацію та авторизацію користувачів
за допомогою
Flask-Логін.

[На екрані відображається кнопка із закликом до дії, щоб перейти до наступної лекції]

**Оповідач:** Якщо ви готові продовжити, натисніть кнопку «Перейти до наступної лекції» нижче. Якщо у вас є
запитання, не соромтеся ставити на дискусійному форумі або під час сесії запитань і відповідей після лекції.

**Оповідач:** Ось і все на сьогодні, студенти. Сподіваюся, ви знайшли цю лекцію інформативною. До зустрічі на наступній
лекції!

**Оповідач:** Перш ніж ми почнемо наступну лекцію, дозвольте мені нагадати вам, що це просунутий навчальний посібник із
Flask, і він
припускає, що ви добре розумієте програмування на Python і концепції веб-розробки. Якщо ви новачок у Flask або
веб-розробки, я б рекомендував почати з документації Flask і деяких вступних посібників для створення a
міцна основа.
[Екран показує короткий огляд тем, які будуть розглянуті в наступній лекції]

**Оповідач:** У цій лекції ми розглянемо такі теми:

1. Налаштування підключення до бази даних за допомогою Flask-SQLAlchemy
2. Визначення моделей і створення таблиць бази даних
3. Виконання операцій CRUD (Create, Read, Update, Delete) за допомогою Flask-SQLAlchemy
4. Реалізація автентифікації та авторизації користувача за допомогою Flask-Login

[На екрані показано редактор коду з налаштуванням Flask і встановленням Flask-SQLAlchemy]

**Екранний диктор:** Для початку давайте переконаємося, що всі необхідні пакети встановлено. Ми будемо використовувати
Flask-SQLAlchemy
для інтеграції бази даних і Flask-Login для автентифікації користувача. Якщо ви ще не встановили ці пакети, ви
їх можна встановити за допомогою pip.

```bash
pip install Flask Flask-SQLAlchemy Flask-Login
```

[На екрані показано редактор коду з налаштуванням програми Flask]

**Оповідач:** Давайте оновимо файл `app.py`, щоб включити Flask-SQLAlchemy та Flask-Login.

```python
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Import routes and templates here


db.create_all()
login_manager.login_view = 'login'


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)
```

[На екрані показано редактор коду з конфігурацією Flask-SQLAlchemy та Flask-Login]

**Оповідач:** Давайте оновимо конфігурацію, щоб налаштувати підключення до бази даних за допомогою Flask-SQLAlchemy. Ми
будемо використовувати
SQLite3 як механізм нашої бази даних для цього підручника.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
```

[На екрані показано редактор коду з визначенням моделі Flask-SQLAlchemy]

**Оповідач:** Давайте визначимо просту модель користувача за допомогою Flask-SQLAlchemy. Створіть новий файл під
назвою `models.py` і визначте
модель користувача.

```python
from flask_sqlalchemy import SQLAlchemy, UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)


def __repr__(self):
	return '<User %r>' % self.username
```

[На екрані показано редактор коду з ініціалізацією бази даних Flask-SQLAlchemy]

**Оповідач:** Давайте ініціалізуємо базу даних у `app.py`, додавши наступний рядок у кінці
файл `db.init_app(app)`

**Оповідач:** Тепер давайте створимо таблиці бази даних за допомогою методу `create_all` Flask-SQLAlchemy. Додайте
наступний рядок у кінці блоку `if __name__ == '__main__'` у `app.py`.

```python
db.create_all()
```

[На екрані показано редактор коду з операціями Flask-SQLAlchemy CRUD ]

**Оповідач:** Давайте виконаємо деякі основні операції CRUD (створення, читання, оновлення, видалення) за допомогою
Flask-SQLAlchemy. в
файл `app.py`, додайте наступні маршрути.

```python
@app.route('/add_user', methods=['POST'])
def add_user():
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	new_user = User(username=username, email=email, password=password)
	db.session.add(new_user)
	db.session.commit()
	flash('New user added!')
	return redirect(url_for('index'))


@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
	user = User.query.get_or_404(user_id)
	
	if request.method == 'POST':
		user.username = request.form['username']
	user.email = request.form['email']
	user.password = request.form['password']
	db.session.commit()
	flash('User updated!')
	return redirect(url_for('index'))


@app.route('/delete_user/<int:user_id>')
@login_required
def delete_user(user_id):
	user = User.query.get_or_404(user_id)
	
	if user == current_user:
		db.session.delete(user)
		db.session.commit()
		flash('User deleted!')
	return redirect(url_for('index'))
```

[На екрані показано редактор коду з налаштуванням автентифікації користувача Flask-Login]

**Оповідач:** Тепер давайте запровадимо автентифікацію користувача за допомогою Flask-Login. У файл `app.py` додайте
наступний код у
кінець.

```python
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
	if user and user.password == form.password.data:
		login_user(user)
		flash('Login successful.')
		return redirect(url_for('index'))
	return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	
	return redirect(url_for('index'))
```

[На екрані показано редактор коду з налаштуванням реєстрації користувача Flask-Login]

**Оповідач:** Давайте запровадимо реєстрацію користувачів за допомогою Flask-SQLAlchemy та Flask-Login. У файл `app.py`
додайте
наступний код в кінці.

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.password = generate_password_hash(form.password.data, method='sha256')
		db.session.add(user)
		db.session.commit()
		flash('Registration successful. Please log in.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)
```

[На екрані відображається кнопка із закликом до дії, щоб перейти до наступної вправи]

**Оповідач:** Це все для цієї лекції, студенти. У цій лекції ми розглянули
інтеграція бази даних і автентифікація користувачів за допомогою Flask-SQLAlchemy і Flask-Login. Ми навчилися створювати
базу даних схеми, визначати моделі та виконувати операції CRUD за допомогою Flask-SQLAlchemy. Ми також дізналися, як реалізувати
user автентифікація та авторизація за допомогою Flask-Login.
