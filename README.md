# deliveryAPI
simple Delivery Order API with Django Rest Framework

:gear: Requirements
-------------------
- Last version of Python and Django
- Create venv and pip install django to import the required modules.

:open_file_folder: File Structure
---------------------------------
```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── README.md
└── settings.py
```
:rocket: Quick Setup
--------------------
Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python3 -m venv venv; source venv/bin/activate; pip install django
```
Download this project template from GitHub
```
git clone https://github.com/abdibrokhim/deliveryAPI.git; cd Django-ORM
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Create super user, input name, email, password
```
python manage.py createsuperuser
```
Run the project, go to http://127.0.0.1:8000/
```
python manage.py runserver
```

Feel free to send pull requests if you want to improve this project.

:crystal_ball: Example
----------------------
After running Quick Start above: 

Code in db/models.py:
```
# Sample User model
class Order(models.Model):
    name = models.CharField(max_length=254, blank=True, choices=products)
    type = models.CharField(max_length=254, blank=True, choices=products_type)
    size = models.CharField(max_length=254, blank=True, choices=products_size)
    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=254, blank=True, null=True)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE)

    status = models.CharField(max_length=254, default="in_progress", choices=order_status)
    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
```

:mortar_board: Django Models
----------------------------

Link: [How to Use Django Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)
