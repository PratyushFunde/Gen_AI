from pydantic import BaseModel
from typing import List,Optional,Dict

class Cart(BaseModel):
    userId:int
    items:List[str]
    quantities:Dict[str,int]

class Blog(BaseModel):
    title:str
    tags:List[str]
    imageURL:Optional[str] = None 

cart_data={
    "userId":123,
    "items":['Laptop','Mouse','Camera','Keyboard','Headphone'],
    "quantities":{'Laptop':3,'Mouse':2,'Keyboard':2},
}

cart=Cart(**cart_data)