from flask import Blueprint, request
from pydantic import BaseModel, EmailStr

from services import MainService

api_bp = Blueprint('api', __name__)

@api_bp.route("/")
def hello_world():
    return {"message": "Hello, API!"}

@api_bp.route("/send_email", methods=["POST"])
def send_email():
    
    try:
        
        request_data = request.json 
    
        class EmailContent(BaseModel):
            username: str
            email: EmailStr
            message: str

        EmailContent(**request_data)

        MainService().process_sending_email(request_data)
        return {"status": "success", "message": "Email sent successfully"}

    except Exception as e:
        return {"status": "error", "message": str(e)}, 400
    
        return {'message': 'Please provide a valid email address'}, 400
