## For setup project do:

- cloning:
```
git clone https://gitverse.ru/space_verse/AnimeDatabase.git
```

- installing uv:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- uv sync:
```
cd AnimeDatabase
uv sync
```

## For run dev server:

```
uv run fastapi dev src/main.py
```

After it the server will run at http://127.0.0.1:8000/
OpenAPI docs you can find at http://127.0.0.1:8000/docs/
