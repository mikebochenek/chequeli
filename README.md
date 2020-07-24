# Cheque.li backend
by Mike Bochenek

## Django basics
Standard Django commands:
```
virtualenv -p /usr/bin/python3 myenv
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser   # test/test
python manage.py runserver 3000
```

##  Auth0
Auth0 helps you to:
* Add authentication with [multiple authentication sources](https://docs.auth0.com/identityproviders),
either social like Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, among others,
or enterprise identity systems like Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider.
* Add authentication through more traditional [username/password databases](https://docs.auth0.com/mysql-connection-tutorial).
* Support for generating signed [JSON Web Tokens](https://docs.auth0.com/jwt) to call your APIs and **flow the user identity** securely.
* Check the [Django Quickstart](https://auth0.com/docs/quickstart/webapp/django) to better understand this sample.

## Tika
The [Apache Tika™](https://tika.apache.org/) toolkit detects and extracts metadata and text from over a thousand different file types
* https://cwiki.apache.org/confluence/display/TIKA/TikaServer
* ./tika start -p 9998
* https://cwiki.apache.org/confluence/display/TIKA/TikaOCR

## SQL
Currently using [PostgreSQL](https://www.postgresql.org/) but Django can be quickly reconfigured to use anything else
```
psql -h 127.0.0.1 -U test3 --password
create database chequelidev;
psql -h 127.0.0.1 -U test3 --password chequelidev
```

## Apache2
see config folder in this project 

## Jenkins
Currently [Jenkins](https://jenkins.bochenek.ch) runs the following build script which is triggered by a webhook
```
cd 01-Login
# ../myenv/bin/pip install -r requirements.txt
rm -rf static
../myenv/bin/python manage.py migrate
../myenv/bin/python manage.py collectstatic
# touch /var/lib/jenkins/workspace/mydjango/mydjango/wsgi.py
```

## Other commands
cd /var/lib/jenkins/workspace/chequeli