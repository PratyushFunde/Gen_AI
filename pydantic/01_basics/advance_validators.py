from pydantic import BaseModel,field_validator

class Person(BaseModel):
    first_name:str
    last_name:str

    @field_validator('first_name','last_name')
    def check_capital(cls,v):
        if not v.istitle():
            raise ValueError("Names must be capatalized.")
        else : 
            return v
        
class User(BaseModel):
    email:str

    @field_validator('email')
    def normalize_email(cls,value):
        return value.lower().strip()

class Product(BaseModel):
    name:str
    price:str #example $44

    @field_validator('price',mode='before')
    def parse_price(cls,v):
        if isinstance(v,str):
            v= v.replace('$','').replace(",",".")
            return str(float(v))
        
        return v

laptop=Product(
    name='laptop',
    price='4,44'
)

user=User(email='pratyushfunde04@gmail.com')           

print(laptop)
