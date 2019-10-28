#!/usr/bin/env bash

cd "$(dirname "$0")"

git pull

cd frontend

npm i

npm run build

cp base.htaccess dist/.htaccess

cd ..

python3.6 manage.py migrate

touch wedding/wsgi.py

