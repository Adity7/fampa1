![Screenshot from 2022-08-29 17-21-28](https://user-images.githubusercontent.com/58148990/187277827-7e0de9d5-cbeb-4271-b38e-d8e6bed83a93.png)
# fampa1
An API to fetch latest videos from youtube sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

The server fetches latest videos async after every 10 minutes and saves it to the db.

This project is completely based on Django.

The following is a basic workflow that you can use as a quick reference for developing a Django Project.

# Setup

Within a new directory, create and activate a virtualenv.

Install Django

Create your project: django-admin.py startproject//

Create a new app: python manage.py startapp//

Add your app to the INSTALLED_APPS tuple.//

Add Basic URLs and Views

Map your Project’s urls.py file to the new app.

In your App directory, create a urls.py file to define your App’s URLs.

Add views, associated with the URLs, in your App’s views.py; make sure they return a HttpResponse object. Depending on the situation, you may also need to query the model (database) to get the required data back requested by the end user.

# Templates and Static Files

Create a templates and static directory within your project root.

Update settings.py to include the paths to your templates.

Add a template (HTML file) to the templates directory. Within that file, you can include the static file with - {% load static %}

Update the views.py file as necessary.

Models and Databases

Update the database engine to settings.py (if necessary, as it defaults to SQLite).

Create and apply a new migration.

Create a super user.

Add an admin.py file in each App that you want access to in the Admin.

Create your models for each App.

Create and apply a new migration. (Do this whenever you make any change to a model).

# Forms

Create a forms.py file at the App to define form-related classes; define your ModelForm classes here.

Add or update a view for handling the form logic - e.g., displaying the form, saving the form data, alerting the user about validation errors, etc.

Add or update a template to display the form.

Add a urlpattern in the App’s urls.py file for the new view.
