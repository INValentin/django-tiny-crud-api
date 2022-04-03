# django tiny CRUD api

## ABOUT

 - Inventory items management
 - Written in **Python** *Django*

**API** to:
 - Create, Read, Update, Delete `inventory items`

## GETTING STARTED

- CHANGE **`DATABASE_URL`** IN `.env` TO MATCH YOUR DB SPECIFICS IN THE FOLLOWING **FORMAT**:
  > - mysql://<user>:<password>@<host>:<port>/<dbname> - Example `mysql://root:@localhost:3306/inventory`

### Recommended

 - Start a virtual environment `python -m venv env` in your local repository
 - On windows run `.\env\Scripts\activate`

- The following command will install the packages according to the configuration file requirements.txt.

> pip install -r requirements.

- The following command will run all database migrations needed

> `pyhton manage.py migrate`
> Then test if it works `pyhton manage.py runserver`

## USAGE

 - Create a superuser using the following command
    > python manage.py createsuperuser 
 - Obtain a token at `POST /token/` with **username** and **password**
 - Use your **token** to access `POST, DELETE and PUT` endpoints(urls).
    > You can use `GET, HEAD, OPTIONS` endpoints without **AUTHENTICATION**
 - List of all *items* at `GET /items/`
 - Create new `items` at `POST /items/`
 - Retrieve item at `GET /items/<item id>/`
 - Update item at `PUT /items/<item id>/` - with fields you want to update
 - Delete item at `DELETE /items/<item id>/`


### Django rest framework will help you with a browsable api 

 > To disable the `browsable api` go to `inventory/setting.py` and `comment` lines `154 - 156` 

### Note THAT API is also acceble at `https://items-crud-api.herokuapp.com/`

## CONTACT

> "ISHIMWE Valentin <ishimwedeveloper@gmail.com>"