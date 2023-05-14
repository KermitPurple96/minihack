#!/bin/bash

source /home/kermit/TFG/minihack/env/bin/activate
flask --app app --debug run --host=0.0.0.0
