serve:
    hugo server --buildDrafts --buildFuture --disableFastRender

pull:
    python build_scripts/pull.py

deps:
    uv pip compile requirements.in -o requirements.txt
    uv pip sync requirements.txt