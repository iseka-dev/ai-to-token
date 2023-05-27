from fastapi.templating import Jinja2Templates
import fastapi_vite

templates = Jinja2Templates(directory="../client/templates")
templates.env.globals['vite_hmr_client'] = fastapi_vite.vite_hmr_client
templates.env.globals['vite_asset'] = fastapi_vite.vite_asset
