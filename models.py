
from pydantic import BaseModel

class pyWorkout_create(BaseModel):

    name:str
    age:int
    exercise_name:str
    num_of_sets:int

class pyWorkout(pyWorkout_create):
    id:int
    
    model_config = {
        "from_attributes": True
    }

    

