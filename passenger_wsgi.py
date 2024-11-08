from a2wsgi import ASGIMiddleware
from app.api import app

application = ASGIMiddleware(app)