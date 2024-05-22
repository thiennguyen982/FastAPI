from pydantic import BaseModel, validator

class ChangePasswordRequest(BaseModel):
    old_password : str
    new_password : str
    
    @validator("new_password")
    def validate_passwords(cls, value, values):
        if "old_password" in values and value == values["old_password"]:
            raise ValueError("New password must be different from the old password")
        return value