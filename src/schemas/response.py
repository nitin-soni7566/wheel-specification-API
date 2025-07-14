from pydantic import BaseModel, Field
from datetime import date
from typing import Literal, Optional, Union, List, Dict
from src.schemas.default_schemas import *

class WheelSpecificationData(BaseModel):
    formNumber: str
    status: str
    submittedBy: str
    submittedDate: date

class CreateWheelSpecificationResponse(CreatedResponse):
    message: Literal["Wheel specification submitted successfully."]
    data: WheelSpecificationData


class CreateWheelSpecificationResponseBackendError(BaseModel):
    code: Literal["INTERNAL_SERVER_ERROR"]
    details: Union[
        Literal[
            "Failed to submit Wheel specification. Please contact developers if the issue persists."
        ],
    ]

class CreateWheelSpecificationErrorResponse(BackendErrorResponse):
    message: Union[
        Literal["INTERNAL_SERVER_ERROR"],
        Literal["Failed to submit Wheel specification."]
    ]
    error: CreateWheelSpecificationResponseBackendError

CREATE_WHEEL_SPECIFICATION_RESPONSE = {
    201: {"model": CreateWheelSpecificationResponse},
    400: {"model": BadRequestErrorResponse},
    500: {"model": CreateWheelSpecificationErrorResponse},
}

class WheelSpecificationListItem(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class GetWheelSpecificationListResponse(SuccessResponse):
    message: Literal["Filtered wheel specification forms fetched successfully."]
    data: List[WheelSpecificationListItem]

class GetWheelSpecificationListBackendError(BaseModel):
    code: Literal["INTERNAL_SERVER_ERROR"]
    details: Literal[
        "Failed to fetch wheel specification list. Please contact developers if the issue persists."
    ]

class GetWheelSpecificationListErrorResponse(BackendErrorResponse):
    message: Literal["INTERNAL_SERVER_ERROR", "Failed to fetch wheel specification list."]
    error: GetWheelSpecificationListBackendError

class GetWheelSpecificationNotFoundError(BaseModel):
    code: Literal["NOT_FOUND"]
    details: Literal["No wheel specifications found for the given filters."]

class GetWheelSpecificationNotFoundResponse(BackendErrorResponse):
    message: Literal["NOT_FOUND"]
    error: GetWheelSpecificationNotFoundError

GET_WHEEL_SPECIFICATION_LIST_RESPONSE = {
    200: {"model": GetWheelSpecificationListResponse},
    400: {"model": BadRequestErrorResponse},
    404: {"model": GetWheelSpecificationNotFoundResponse},
    500: {"model": GetWheelSpecificationListErrorResponse},
}
