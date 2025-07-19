from fastapi import HTTPException
from src.schemas.requests import (
    GetWheelSpecificationQuery,
    AddWheelSpecificationPayload,
)
from fastapi.responses import JSONResponse
from src.schemas.response import (
    WheelSpecificationData,
    CreateWheelSpecificationResponse,
    WheelSpecificationListItem,
)
from src.database.models import WheelSpecification
from sqlalchemy.orm import Session
import json
from src.services.logger import logger


def submit_wheel_specification_api(payload: AddWheelSpecificationPayload, db: Session):
    """
    Submits a new wheel specification form to the database.

    Args:
        payload (AddWheelSpecificationPayload): The data submitted by the user.
        db (Session): The database session.

    Returns:
        CreateWheelSpecificationResponse: Response data with status, message, and created form data.
    """
    try:
        existing_spec = (
            db.query(WheelSpecification)
            .filter(WheelSpecification.formNumber == payload.formNumber)
            .first()
        )

        if existing_spec:
            return JSONResponse(
                status_code=409,
                content={
                    "success": False,
                    "message": "Form number already exists.",
                    "error": {
                        "code": "DUPLICATE_FORM_NUMBER",
                        "details": f"A wheel specification with formNumber '{payload.formNumber}' already exists.",
                    },
                },
            )

        # Create new entry
        wh_specification = WheelSpecification(
            formNumber=payload.formNumber,
            submittedBy=payload.submittedBy,
            submittedDate=payload.submittedDate,
            fields=json.dumps(payload.fields.dict()),
            status="Saved",
        )

        db.add(wh_specification)
        db.commit()
        db.refresh(wh_specification)

        response_data = WheelSpecificationData(
            formNumber=wh_specification.formNumber,
            status=wh_specification.status,
            submittedBy=wh_specification.submittedBy,
            submittedDate=wh_specification.submittedDate,
        )

        return CreateWheelSpecificationResponse(
            data=response_data,
            message="Wheel specification submitted successfully.",
            success=True,
        )

    except Exception as e:
        logger.error(f"Error while submitting wheel specification: {e}")
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Failed to submit wheel specification."
        )


def get_wheel_specifications_api(payload: GetWheelSpecificationQuery, db: Session):
    """
    Fetches wheel specification forms filtered by optional criteria.

    Args:
        payload (GetWheelSpecificationQuery): Optional query filters.
        db (Session): SQLAlchemy database session.

    Returns:
        dict: A response with list of matching forms, message, and success flag.
    """
    try:
        query = db.query(WheelSpecification)

        if payload.formNumber:
            query = query.filter(WheelSpecification.formNumber == payload.formNumber)
        if payload.submittedBy:
            query = query.filter(WheelSpecification.submittedBy == payload.submittedBy)
        if payload.submittedDate:
            query = query.filter(
                WheelSpecification.submittedDate == payload.submittedDate
            )

        results = query.all()

        if not results:
            raise HTTPException(
                status_code=404,
                detail="No wheel specifications found for the given filters.",
            )

        data = []
        for item in results:
            try:
                fields_data = (
                    json.loads(item.fields)
                    if isinstance(item.fields, str)
                    else item.fields
                )
            except json.JSONDecodeError:
                fields_data = {}

            data.append(
                WheelSpecificationListItem(
                    formNumber=item.formNumber,
                    submittedBy=item.submittedBy,
                    submittedDate=item.submittedDate,
                    fields=fields_data,
                )
            )

        return {
            "data": data,
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error while fetching wheel specifications: {e}")
        raise HTTPException(
            status_code=500, detail="Failed to fetch wheel specifications."
        )
