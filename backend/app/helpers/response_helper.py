from typing import Any, Optional, Dict
from fastapi.responses import JSONResponse

def success_response(data: Any, message: str = "Sukses", status_code: int = 200) -> JSONResponse:
    """Standard format JSON success response ala Laravel"""
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "success",
            "message": message,
            "data": data
        }
    )

def error_response(message: str, errors: Optional[Any] = None, status_code: int = 400) -> JSONResponse:
    """Standard format JSON error response ala Laravel"""
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": message,
            "errors": errors
        }
    )
