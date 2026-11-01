from pydantic import BaseModel, Field, HttpUrl


class WebsiteScanRequest(BaseModel):
    url: HttpUrl
    authorized: bool = Field(..., description="Confirm you own this target or have written permission to test it")


class ScanAccepted(BaseModel):
    status: str
    message: str
