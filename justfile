pull:
  python build_scripts/pull.py

clean:
  rm -r content/*

serve:
  hugo server -D
  
deps:
    uv pip compile requirements.in -o requirements.txt
    uv pip sync requirements.txt