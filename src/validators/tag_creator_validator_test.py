from .tag_creator_validator import tag_creator_validator
from src.errors.error_types.http_unprecessable_entity import HttpUnprecessableEntity

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validador():
    req = MockRequest(json={"product_code": "12345"})
    response = tag_creator_validator(req)
    
def test_tag_creator_validador_with_error():
    req = MockRequest(json={"product_code": 12345})
    
    try:
        response = tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprecessableEntity)