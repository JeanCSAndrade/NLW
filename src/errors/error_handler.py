from src.views.http_types.http_response import HttpResponse
from  .error_types.http_unprecessable_entity import HttpUnprecessableEntity
def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprecessableEntity):
        return HttpResponse(
            status_code = error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )