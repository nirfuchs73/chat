#!/bin/bash

export FLASK_APP=chat-server.py
python3 -m flask run --host=localhost --port=8080