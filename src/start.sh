#!/bin/bash

python3 -m venv venv >/dev/null 2>&1

source venv/bin/activate >/dev/null 2>&1

pip install --upgrade pip >/dev/null 2>&1
pip install -r requirements.txt >/dev/null 2>&1

python main.py "$@"

deactivate >/dev/null 2>&1
