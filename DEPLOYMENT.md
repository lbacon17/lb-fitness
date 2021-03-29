#### To deploy the app to Heroku using Gitpod.

1. Install the Heroku toolbelt via the terminal with the command ```npm install -g heroku``` and login by typing ```heroku login -i``` and entering the e-mail address and password you use for your Heroku account
    * Note that Heroku doesn't support the use of underscores (_) in app names, so if your GitHub repository contains these characters, you may wish to replace these with dashes (-) or something similar

1. Before deploying, go to your Heroku dashboard and provision a new Postgres database by selecting the Resources tab in the app's dashboard and searching for 'Heroku Postgres' in the add-ons search bar
    * Select the free plan called 'Hobby Dev'

1. To use Postgres, install dj-database-url and psycopg2 in Gitpod by entering the respective commands ```pip3 install dj_database_url``` and ```pip3 install psycopg2-binary```

1. To ensure that Heroku installs these packages when deploying the app, freeze these packages into your requirements.txt file with the command ```pip3 freeze > requirements.txt```

1. To set up the new database, type ```import dj_database_url``` in the settings.py file just below ```import os```

1. In the DATABASE variable of the settings file, replace the default database with a call to the dj_database_url.parse() method and pass in the database URL from Heroku, which can be found in the settings tab of the app's dashboard by clicking 'Reveal Config Vars'
    * ```
        DATABASES = {
	        ‘default’: dj_database_url.parse(‘<DATABASE_URL>’),
        }
        ``` 

1. To connect Postgres to Django, re-run the app's migrations by firstly typing ```python3 manage.py makemigrations``` followed by ```python3 manage.py migrate```
    * To preview the migrations before making them, you can enter the commands ```python3 manage.py makemigrations --dry-run``` and ```python3 manage.py migrate --plan```

1. If your datasets are in any JSON files, import the data into the database with the command ```python3 manage.py loaddata <fixturename>```
    * The name of the dataset being loaded should match the name of the JSON file before the .json extension e.g. if your product data was stored in a file called products.json, you would import the data by typing ```python3 manage.py loaddata products```
    * If you have multiple JSON files, you will need to import each file with a separate command

1. Create a superuser to log into the Django admin panel with the command ```python3 manage.py createsuperuser``` and enter a desired username and password. This will also be your password to log into the application itself as the superuser.

1. To avoid your database URL ending up in version control, store this as an environment variable in your env.py file as ```os.environ['DATABASE_URL'] = '<database_url>'``` and replace the URL with the pathname in settings.py. Your DATABASES variable should now be set to ```'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))```
    * Make sure you have imported the environment into your settings file, otherwise it won't be able to retrieve the variable. You should have the following statements in your settings file:
        * ```from os import path```
        * ```from pathlib import Path```
        * ```
            if path.exists('env.py'):
                import env
            ```

1. Wrap the DATABASES variable in an if/else block so that we connect to Postgres when the app is running on Heroku (where the environment variable is defined), and otherwise to the default configuration
    * ```
        if ‘DATABASE_URL’ in os.environ:
	        DATABASES = {
            ‘default’: dj_database_url.parse(os.environ.get(‘DATABASE_URL’))
            }
        else:
            DATABASES = {
                ‘default’: {
                    ‘ENGINE’: ‘django.db.backends.sqlite3’,
                    ‘NAME’: os.path.join(BASE_DIR, ‘db.sqlite3’),
                }
            }
        ```

1. Install the Gunicorn package, which will act as a web server, with the command ```pip3 install gunicorn``` and freeze this into the requirements file (```pip3 freeze > requirements.txt```)

1. Create a Procfile so that Heroku detects that the application is based on Python and input ```web: gunicorn app_name.wsgi:application```
    * To create the Procfile, enter the command ```touch Procfile``` (the P must be capitalised)
    * If there is a blank line at the end of the Procfile, remove it as this can cause Heroku problems in locating the file

1. To prevent Heroku collecting static files when deploying the app (we'll use AWS for this later), set the DISABLE_COLLECTSTATIC config variable to 1 by entering the command ```heroku config:set DISABLE_COLLECTSTATIC=1 --app app-name

1. Add the hostname of the Heroku app to the allowed hosts in settings.py alongside the localhost to ensure that we can still work on the app locally
    * ```ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']```

1. To attempt deployment, commit and push your changes to GitHub using ```git add .```, ```git commit -m "message"``` and ```git push``` and initialise a Heroku repository with the command ```heroku git:remote -a app-name```
    * To verify that Heroku has created a git repository, type the command ```git remote -v``` to view the remote URLs. There should be four in total:
        * ```heroku https://git.heroku.com/app-name.git (fetch)```
        * ```heroku https://git.heroku.com/app-name.git (push)```
        * ```origin https://github.com/githubusername/repository_name.git (fetch)```
        * ```origin https://github.com/githubusername/repository_name.git (push)```

1. If you haven't done so already, create a .gitignore file in Gitpod with ```touch .gitignore``` and add:
    * ```env.py```
    * ```*.sqlite3```
    *```.pyc```
    *```__pycache__/```
    * These will not be included in any commits. **Do not push these files to GitHub as your secret keys will be publicly available and compromise the security of your app.**

1. In your Heroku dashboard, go to the Deploy tab and select GitHub as your deployment method, typing in your GitHub repository name to connect it to Heroku

1. In the Automatic Deploys section, click the Enable Automatic Deploys button so that your code is automatically deployed to Heroku each time you push it to GitHub.

1. In Gitpod, enter the command ```git push heroku master``` to deploy to Heroku
    * This command may fail and return the error ```src refspec master does not match any```. If this is the case, try the comamnd ```git push heroku HEAD``` instead

1. The deployment may take a few minutes. Once complete, the message: "Build succeeded" will appear. Go to Settings, scroll down to Domains and click your app's URL to view the deployed app in a new browser tab.

1. Create a SECRET_KEY config var in Heroku by clicking the Settings tab and selecting Reveal Config Vars, and add a path to this in settings.py by inputting ```SECRET_KEY = os.environ.get('SECRET_KEY', '')```
    * You can use the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) to generate a random secret key

#### To store static and media files using AWS

1. To use Amazon Web Services (AWS), head to https://aws.amazon.com/ and create an account by completing the registration process

1. Once logged into AWS, select S3 from the AWS services box (you'll find it under the storage heading) and click 'Create Bucket'
    * It is recommended that the bucket's name matches the app's Heroku name

1. Uncheck 'block all public access' and acknowledge that the bucket will be public, as it needs to be to allow public access to static files

1. In the bucket, turn on static website hosting under the Properties tab, and fill in ```index.html``` and ```error.html``` as the default values for the index and error documents respectively

1. In the Permissions section, paste in the following code under the Cross-origin resource sharing section:
    * ```
        [
            {
                “AllowedHeaders”: [
                    “Authorization”
                ],
                “AllowedMethods”: [
                    “GET”
                ],
                “AllowedOrigins”: [
                    “*”
                ],
                “ExposeHeaders”: []
            }
        ]
        ```

1. In the Bucket policy section, click on Policy generator:
    * select S3 bucket policy as the policy type
    * Input '*' into Principals
    * Copy the Bucket ARN from the Permissions tab and paste it into the Amazon Resource Name field
    * Click Add Statement followed by Generate Policy
    * Copy the policy from the pop-up box into the Bucket Policy Editor
    * Add "/*' onto the end of the Resource key value to allow access to all the resources in the bucket
        * The ARN should be have the format ```arn:aws:s3:::bucket-name```
    * Click save changes
    * In the Access control list section under Permissions, go to Public Access and set the check the List permission in the Everyone field

1. Go back to the console and select IAM (you'll find it under Security, Identity & Compliance)

1. Go to Groups and select Create new group
    * Enter a group name and skip through to the end

1. Go to Policies and select Create policy
    * Go to the JSON tab, click on Import managed policy and select AmazonS3FullAccess to import
    * Get the ARN from the Bucket Policy page and copy this twice into the Resource key, adding "/*" onto the end of the second value
        * ```
            "Resource": [
                "arn:aws:s3:::bucket-name", 
                "arn:aws:s3:::bucket-name/*"
            ]
            ```
    * Click through to Review policy and give the policy a name and description
        * The name should be similar to the app name e.g. app-name-policy
        * The description should be something like "access to S3 bucket for app-name static files"
    * Click Create policy

1. Go back to Groups, select your group and click Attach policy under the Permissions tab
    * Your policy should be in the list of policies. Select it and click Attach policy
        * If you can't see your policy, type its name or part of its name into the search bar to reduce the number of visible policies

1. Go to Users, click Add user and enter a desired username
    * It is recommended that the username indicates that the user is a static files user for your app
    * Check Programmatic access under Access type
    * Click through to the end and select Create user

1. Download the CSV file generated
    * You must download this file before exiting the page as it contains the user and secret access keys that we use to authenticate the user from Django, and it can't be re-downloaded later in the process

1. To connect Django to S3, install the boto3 and django-storages packages in Gitpod, using ```pip3 install boto3``` and ```pip3 install django-storages```
    * Add 'storages' to INSTALLED_APPS in settings.py

1. Add an if statement to the settings file to check if an environment variable exists called USE_AWS, as Django should only be connected to S3 on Heroku
    * If the variable exists, define the AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY variables
    * Add these values to the config variables in Heroku using the same keys and set USE_AWS to True
    * ```
        if ‘USE_AWS’ in os.environ:
            AWS_STORAGE_BUCKET_NAME = 'bucket-name'
            AWS_S3_REGION_NAME = 'eu-west-2'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        ```
    * The AWS key values come from the downloaded CSV file

1. In settings.py, add a variable AWS_S3_CUSTOM_DOMAIN to tell Django which URL our static files come from in production
    * ```AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com')```

1. Create a new file custom_storages.py using ```touch custom_storages.py``` and enter the following code:
    * ```
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage


        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION
        ```

1. In settings.py, create the following variables underneath the AWS keys within the above if statement:
    ```
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'
        
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

1. For cache control, add a setting AWS_S3_OBJECT_PARAMATERS at the very top of the if statement that tells the browser to effectively cache static files permanently
    * ```
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 23:59:59 GMT',
            'CacheControl': 'max-age=94608000'
        }
        ```

1. Go back to your S3 bucket, create a new folder called media, select Upload > Add files and upload all the app's media files from your device
    * In the Access control list section, check the Read boxes under Everyone to grant public read access

1. Log into the Django admin and confirm the e-mail address for the superuser you created by selecting E-mail addresses followed, clicking on the user's e-mail address and checking the Verified box
    * It is also possible to get an e-mail confirmation link from the Heroku app logs, but this way is quicker
    * This step is essential as you won't be able to log into your application without verifying your e-mail

1. If your app is using Stripe to process payments, log into Stripe, select API Keys from the Developers section copy the publishable and secret keys and add these as config variables in Heroku as STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY respectively

1. Select Webhooks and create a new endpoint, entering the URL for your Heroku app and whatever path you use to allow users to check out and create a webhook (this is usually /checkout/wh/ but could be anything)
    * The endpoint URL should be similar to ```https://app-name.herokuapp.com/checkout/wh/```
        * Don't forget to enter the trailing forward slash in the URL, otherwise it may not work
    * Under Events to send, click receive all events
    * Under Signing secrets, click the reveal button, copy the key and add to your Heroku config variables as STRIPE_WH_SECRET

1. The app should now be successfully deployed and anyone should be able to make a purchase using a credit card

#### Emails

1. If you have a Gmail account, to enable automated e-mails log into Gmail, go to Settings > Accounts and import > Other Google account settings > Security > Signing into Google and turn on two-step verification
    * This lets us create a Django-specific app password that lets it authenticate and use your Gmail account to send e-mails

1. Select Mail as the app, and select Other as device type, and enter 'Django' to generate a 16-character password

1. Copy this password and add it as a config variable to Heroku as EMAIL_HOST_PASS, and add your Gmail address as EMAIL_HOST_USER

1. In settings.py, enter the following code:
    * ```
        if 'DEVELOPMENT' in os.environ:
            EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
            DEFAULT_FROM_EMAIL = 'appname@example.com'
        else:
            EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            EMAIL_USE_TLS = True
            EMAIL_PORT = 587
            EMAIL_HOST = 'smtp.gmail.com'
            EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
            EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
            DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    * You can test that e-mail verification and confirmation works by obtaining a temporary e-mail address from [https://temp-mail.org/](temp-mail.org) and using it to register for your app

1. Deploy to Heroku again, and you should have a fully functional application that sends e-mails.