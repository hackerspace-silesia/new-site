# HS Silesia new-site

## install

```bash
# venv or sth (python mastah)
git submodule update --init
pip install -r requirements.txt
pelican content  # tada - your content is on 
```

## What is editable?

* `content` dir
* `pelicanconf.py` file

## Still confused?

* https://docs.getpelican.com/en/stable/
* https://docs.getpelican.com/en/stable/content.html

## Dev mode

```
pelican listen
```

This command create a devserver on localhost:8000

Warning: you still need `pelican content` command to generate content
