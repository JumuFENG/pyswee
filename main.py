import uvicorn

from app.lofig import Config, logger
from fastapi import FastAPI

cfg = Config.client_config()
app = FastAPI(title=cfg.get('app_name', 'pyswee'))


@app.get("/")
def root():
    return {"app": cfg.get('app_name', 'pyswee')}


if __name__ == '__main__':
    logger.info("Starting server...")
    uvicorn.run("main:app", host="0.0.0.0", port=cfg.get('port', 8000), reload=True)

