#!/bin/bash
python ./manage.py migrate || true
python ./manage.py runserver 0.0.0.0:64646
