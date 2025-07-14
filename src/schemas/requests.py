from pydantic import  BaseModel
from datetime import date
from typing import Optional
from fastapi import Query


class GetWheelSpecificationQuery:
    def __init__(self,
                 
    formNumber: Optional[str] = Query(default=None),
    submittedBy: Optional[str] = Query(default=None),
    submittedDate: Optional[date] = Query(default=None)
                 ):
        self.formNumber=formNumber
        self.submittedBy=submittedBy
        self.submittedDate=submittedDate



class WheelSpecificationItems(BaseModel):
    axleBoxHousingBoreDia:str
    bearingSeatDiameter:str
    condemningDia:str
    intermediateWWP:str
    lastShopIssueSize:str
    rollerBearingBoreDia:str
    rollerBearingOuterDia:str
    rollerBearingWidth:str
    treadDiameterNew:str
    variationSameAxle:str
    variationSameBogie:str
    variationSameCoach:str
    wheelDiscWidth:str
    wheelGauge:str
    wheelProfile:str

    class Config:
        from_attributes = True

class AddWheelSpecificationPayload(BaseModel):
    fields:WheelSpecificationItems
    formNumber:str
    submittedBy:str
    submittedDate:date

    class Config:
        from_attributes = True
