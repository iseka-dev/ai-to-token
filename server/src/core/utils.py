import fastapi_vite
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="../client/templates")
templates.env.globals['vite_hmr_client'] = fastapi_vite.vite_hmr_client
templates.env.globals['vite_asset'] = fastapi_vite.vite_asset
