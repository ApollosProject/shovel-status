import os

import requests
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

ORG_ID = os.getenv("ASTRO_ORG_ID")
WORKSPACE_ID = os.getenv("ASTRO_WORKSPACE_ID")
API_TOKEN = os.getenv("ASTRO_API_TOKEN")

app = Flask(__name__)


@app.route("/status")
def status():
    num_active_dags = requests.get(
        f"https://api.astronomer.io/v1alpha1/organizations/{ORG_ID}/workspaces/{WORKSPACE_ID}/dags",
        params={
            "numRuns": 14,
            "isPaused": False,
            "tag__in": "delta",
        },
        headers={"Authorization": f"Bearer {API_TOKEN}"},
    ).json()["totalCount"]
    if num_active_dags == 0:
        return {"num_active_dags": 0, "status": "unknown"}
    num_failed_dags = requests.get(
        f"https://api.astronomer.io/v1alpha1/organizations/{ORG_ID}/workspaces/{WORKSPACE_ID}/dags",
        params={
            "numRuns": 14,
            "lastRunState__in": "failed",
            "isPaused": False,
            "tag__in": "delta",
        },
        headers={"Authorization": f"Bearer {API_TOKEN}"},
    ).json()["totalCount"]
    percent_failed = num_failed_dags / num_active_dags * 100
    healthy = percent_failed < 10
    return {
        "num_active_dags": num_active_dags,
        "num_failed_dags": num_failed_dags,
        "percent_failed": percent_failed,
        "status": "healthy" if healthy else "unhealthy",
    }
