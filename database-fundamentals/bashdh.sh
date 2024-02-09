#!/bin/bash

db_set() {
    (
        flock 9 && echo "$1,$2" >> database && sync -d database
    ) 9>database.lock
}

db_get() {
    (
        flock -s 9 && grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
    ) 9>database.lock
}

db_set 500 '{"movie": "Airplane!", "rating": 9}'
db_set 111 '{"movie": "Tokio Drift", "rating": 6}'
db_get 500