from routing import Route
from constants import HTTP_METHODS
import method_handlers

routes = [
    Route(HTTP_METHODS.GET, '/', method_handlers.handle_index),
    Route(HTTP_METHODS.POST, '/post/', method_handlers.post),
    Route(HTTP_METHODS.GET, '/delete/', method_handlers.delete)
]