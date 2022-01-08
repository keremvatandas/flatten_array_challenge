from fastapi import HTTPException, status


CHECK_INPUT_MSG: str = "Please check the data you sent."
CHECK_INPUT_EXC = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=CHECK_INPUT_MSG)


EMPTY_ARRAY_MSG: str = "Please enter the array elements."
EMPTY_ARRAY_EXC = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=EMPTY_ARRAY_MSG)

