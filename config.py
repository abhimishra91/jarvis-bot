#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 8080
    APP_ID = os.environ.get("MicrosoftAppId", "{APP ID AFTER REGISTERING THE APP ON AZURE}")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "{APP PASSWORD REGISTERING THE APP ON AZURE}")
