#!/bin/bash

for i in {0..12} ; do
    flask db upgrade && break
    echo "Error running migrations. Sleeping 5 seconds"
    sleep 5
done
exec gunicorn -b :5000 - flaskapp:app