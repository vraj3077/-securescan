from fastapi import FastAPI, HTTPException
from backend.schemas import WebsiteScanRequest, ScanAccepted

app = FastAPI(title="SecureScan API", version="0.1.0", description="Local-first authorized security scanning starter")


@app.get("/health")
def health():
    return {"status": "ok", "project": "SecureScan", "version": "0.1.0"}


@app.post("/scans/website", response_model=ScanAccepted)
def request_website_scan(request: WebsiteScanRequest):
    if not request.authorized:
        raise HTTPException(status_code=403, detail="Confirm authorization before requesting a scan")
    # Intentionally does not launch network activity yet. Host allow-listing,
    # DNS/IP validation, and passive ZAP orchestration must be implemented first.
    return ScanAccepted(status="accepted_not_started", message="Request recorded by the starter API; scanning is not implemented yet.")
