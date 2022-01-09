from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.core.constants import FLATTEN_ARRAY_URL, API_PREFIX
from app.core.utils import flatten_array
from app.routes.exceptions import CHECK_INPUT_EXC, EMPTY_ARRAY_EXC


router = APIRouter(prefix=API_PREFIX)


@router.post(FLATTEN_ARRAY_URL)
async def flatten_array_service(data: Request) -> JSONResponse:
    try:
        req_body = await data.json()
        inputs = req_body.get("input")
        if inputs:
            result: List[int] = await flatten_array(inputs)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"output": result})
        else:
            raise CHECK_INPUT_EXC
    except Exception:
        raise CHECK_INPUT_EXC
