#!/usr/bin/env sh

python manage.py collectstatic --noinput
#python manage.py compilemessages
python manage.py makemigrations
python manage.py migrate --noinput

# https://stackoverflow.com/questions/39082768/what-does-set-e-and-exec-do-for-docker-entrypoint-scripts#:~:text=exec%20%22%24%40%22%20is%20typically%20used,to%20the%20command%20line%20arguments.
exec "$@"