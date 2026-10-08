from typing import Any, Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def success_response(data: Any, message: str = "Sukses", status_code: int = 200) -> JSONResponse:
    """Standard format JSON success response ala Laravel"""
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder({
            "status": "success",
            "message": message,
            "data": data
        })
    )

def error_response(message: str, errors: Optional[Any] = None, status_code: int = 400) -> JSONResponse:
    """Standard format JSON error response ala Laravel"""
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder({
            "status": "error",
            "message": message,
            "errors": errors
        })
    )
