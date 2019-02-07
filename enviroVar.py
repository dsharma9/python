#!/usr/bin/env python3.7

import os

stage=os.environ["STAGE"].upper()

output=f"We are working on {stage} enviroment"

if stage.startswith('PROD'):
    output="Danger !!! " + output

print(output)
