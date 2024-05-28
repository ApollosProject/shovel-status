# Shovel Status

Quickly reports overall health of the shovel.

## Usage

First define the environment variables in an `.env` file:

```bash
ASTRO_ORG_ID=your_org_id
ASTRO_WORKSPACE_ID=your_workspace_id
ASTRO_API_TOKEN=your_api_token
```

Then run the following commands:

```bash
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
flask --app api/index run --debug
```

Access the page at `http://localhost:5000/status`.
