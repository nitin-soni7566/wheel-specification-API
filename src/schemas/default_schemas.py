from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from typing import Dict, List, Literal, TypedDict, Union

class UserData(BaseModel):
    email: str
    first_name: str
    last_name: str
    role: str
    client_account_name: str
    last_logged_in: datetime


class SuccessfulResponse(BaseModel):
    success: bool = True
    message: str = "This is initial route of Weel Specification api"
    data: None


class CreatedResponse(BaseModel):
    success: bool = True
    message: str = "Created"
    data: None


class AcceptedResponse(BaseModel):
    success: bool = True
    message: str = "Accepted"
    data: None


class BadRequestError(BaseModel):
    code: Literal["BAD_REQUEST"]
    details: Literal[
        "The request could not be understood or was missing required parameters."
    ]


class BadRequestErrorResponse(BaseModel):
    success: bool = False
    message: str = "Bad Request"
    data: None
    error: BadRequestError


class NotFoundError(BaseModel):
    code: Literal["NOT_FOUND"]
    details: Literal[
        "data with the provided id does not exist. Please contact developers if the issue persists."
    ]


class NotFoundErrorResponse(BaseModel):
    success: bool = False
    message: Literal["data not found"]
    data: None
    error: NotFoundError

class BackendError(BaseModel):
    code: Literal["INTERNAL_SERVER_ERROR"]
    details: Literal[
        "Something went wrong. Please contact developers if the issue persists."
    ]


class BackendErrorResponse(BaseModel):
    success: bool = False
    message: str = "Internal Server Error"
    data: None
    error: BackendError

class SuccessResponse(BaseModel):
    success: Literal[True]
    message: str

HOME_RESPONSE_MODEL = {
    200: {"model": SuccessfulResponse},
    500: {"model": BackendErrorResponse},
}