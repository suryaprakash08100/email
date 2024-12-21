from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email_service import send_email  # This should be correct

app = FastAPI()

class EmailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str


@app.post("/send-email/")
async def send_email_endpoint(request: EmailRequest):
    result = await send_email(request.to_email, request.subject, request.body)
    if result["status"] == "success":
        return {"message": "Email sent successfully"}
    else:
        raise HTTPException(status_code=500, detail=result["message"])
