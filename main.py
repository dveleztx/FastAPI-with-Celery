#!/usr/bin/python
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 08/23/2021
# Description : FastAPI and Celery Project
###############################################################################

# Imports
from project import create_app
from project.data import db_session

app = create_app()


@app.on_event("startup")
async def setup_db():
    await db_session.global_init()
