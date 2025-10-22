from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class Workout(Base):

    __tablename__="Workout"

    id= Column(Integer, primary_key=True, index=True)
    name=Column(String)
    age=Column(Integer)
    exercise_name=Column(String)
    num_of_sets=Column(Integer)

    