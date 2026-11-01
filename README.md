# SecureScan

Local-first starter for authorized black-box security checks of websites and Android APKs. No source-code upload is required.

## Status

This is an early scaffold, not a finished vulnerability scanner. The API currently provides health checks and guarded scan-request placeholders. MobSF and OWASP ZAP services can be started locally, but the API does not yet orchestrate scans or produce findings.

## Requirements

- Windows 10/11
- Python 3.11+
- VS Code
- Docker Desktop (for local scanner services)

## Run the API (PowerShell)

```powershell
py -3 -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Start local scanner services

```powershell
docker compose up -d mobsf zap
```

MobSF UI: http://127.0.0.1:8001. ZAP API is bound to localhost only. Do not expose either service to the public internet.

## Safety

Only test systems you own or have explicit written permission to assess. Start with staging systems and test accounts. The initial website integration is intended to use passive checks only. Do not use this scaffold against third-party targets.

## Roadmap

1. Add strict hostname allow-list and DNS/IP safety validation.
2. Integrate ZAP Baseline for passive website checks.
3. Integrate MobSF for APK static analysis.
4. Normalize findings and generate reports.
5. Add a React dashboard and authenticated local job management.
