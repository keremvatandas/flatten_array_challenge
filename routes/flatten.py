from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from starlette.requests import Request

from core.config import API_PREFIX
from core.constants import FLATTEN_ARRAY_URL
from core.utils import flatten_array
from routes.exceptions import NOT_FOUND


router = APIRouter(prefix=API_PREFIX)


@router.post(FLATTEN_ARRAY_URL)
async def flatten_array_service(data: Request) -> JSONResponse:
    req_body = await data.json()
    if req_body.get("input"):
        result: List[int] = await flatten_array(req_body.get("input"))
        return JSONResponse(status_code=status.HTTP_200_OK, content={"output": result})
    else:
        raise NOT_FOUND
