from pydantic import BaseModel,field_validator,model_validator


class User(BaseModel):
    userName:str

    @field_validator('userName')
    def username_length(cls,v):
        if(len(v)<4):
            raise ValueError("Username must be al least 4 characters long.")
        else :
            return v

class SignUpData(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def check_pass(cls,values):
        if(values.password!=values.confirm_password):
            raise ValueError('Password do not match.')
        else:
            return values
            