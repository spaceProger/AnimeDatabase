import uvicorn

import utils as app_utils
import setup


app = setup.get_app()


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=app_utils.app_host(),
        port=app_utils.app_port(),
        workers=app_utils.app_workers(),
    )
