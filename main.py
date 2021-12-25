#!/usr/bin/python
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 08/23/2021
# Description : FastAPI and Celery Project
###############################################################################

# Imports
import asyncio

from project import create_app
from project.data import db_session

app = create_app()
celery = app.celery_app


def celery_worker():
    from watchgod import run_process
    import subprocess

    def run_worker():
        subprocess.call(
            ["celery", "-A", "main.celery", "worker", "--loglevel=info"]
        )

    run_process("./project", run_worker)


@app.on_event("startup")
async def init():
    await db_session.global_init()
