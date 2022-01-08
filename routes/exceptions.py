from fastapi import HTTPException, status


NOT_FOUND_MSG: str = "Resource not found."
NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MSG)
