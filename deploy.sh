#!/usr/bin/env bash

cd "$(dirname "$0")"
git pull

cd frontend
npm i
npm run build

cd ..
python3.6 manage.py migrate

cd frontend
rm -r dist
mkdir dist
cp base.htaccess dist/.htaccess
cp -r dist_tmp/* dist

cd ..
touch wedding/wsgi.py

