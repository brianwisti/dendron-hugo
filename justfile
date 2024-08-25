pull:
  python build_scripts/pull.py

style:
  cp ~/dev/superkube/dist/superkube.css themes/dendron-superkube/static/css
  cp ~/dev/superkube/dist/superkube.css.map themes/dendron-superkube/static/css

clean:
  rm -r content/*

serve:
  hugo server -D
  
deps:
    uv pip compile requirements.in -o requirements.txt
    uv pip sync requirements.txt
