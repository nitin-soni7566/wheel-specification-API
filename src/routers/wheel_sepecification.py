from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.schemas.response import (
    CREATE_WHEEL_SPECIFICATION_RESPONSE,
    GET_WHEEL_SPECIFICATION_LIST_RESPONSE,
    CreateWheelSpecificationResponse,
    GetWheelSpecificationListResponse,
)
from src.schemas.requests import (
    GetWheelSpecificationQuery,
    AddWheelSpecificationPayload,
)
from src.database.connect import get_db
from src.controllers.wheel_sepecification_services import (
    submit_wheel_specification_api,
    get_wheel_specifications_api,
)

router = APIRouter(tags=["Wheel Specification"])


@router.post(
    "/api/forms/wheel-specifications",
    response_model=CreateWheelSpecificationResponse,
    responses=CREATE_WHEEL_SPECIFICATION_RESPONSE,
    status_code=201
)
def submit_wheel_specification(
    payload: AddWheelSpecificationPayload,
    db: Session = Depends(get_db),
):
    """
    Submit a new wheel specification form.
    """
    return submit_wheel_specification_api(payload, db)


@router.get(
    "/api/forms/wheel-specifications",
    response_model=GetWheelSpecificationListResponse,
    responses=GET_WHEEL_SPECIFICATION_LIST_RESPONSE,
)
def get_wheel_specifications(
    payload: GetWheelSpecificationQuery = Depends(),
    db: Session = Depends(get_db),
):
    """
    Fetch wheel specification forms filtered by form number, submitted by, or submitted date.
    """
    return get_wheel_specifications_api(payload, db)
