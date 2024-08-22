pull:
  python build_scripts/pull.py

clean:
  rm -r content/*

serve:
  hugo server -D