#!/bin/bash

gunicorn apartamentos.wsgi:application --bind 127.0.0.1:8001 --proxy-protocol