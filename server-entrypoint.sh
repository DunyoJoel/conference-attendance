#!/bin/sh

until cd ./
do
    echo "Waiting for server volume..."
done


until alembic stamp head
do
    echo "Alembic Database head run..."
    sleep 2
done

until alembic revision --autogenerate -m "database Tables"
do
    echo "Alembic Database tables creation Done..."
    sleep 2
done

until alembic upgrade head
do
    echo "Alembic Database head run..."
    sleep 2
done


python3 run.py
