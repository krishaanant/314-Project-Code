We need definitions
- for an asset, we need to define it under `defs = Definitions()` to add it to the DAG

python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
dagster dev
https://didactic-funicular-x755jj5r5793prjv-3000.app.github.dev/locations/314_project/assets