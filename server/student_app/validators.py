import re

from django.core.exceptions import ValidationError

from django.core.validators import MaxValueValidator, MinValueValidator

def validate_name(name):
    pattern = r"^[A-Z][a-z]*\s[A-Z].{1}\s[A-Z][a-z]*$"
    if not re.match(pattern, name):
        raise ValidationError(
            'Name must be in the format "First Middle Initial. Last"'
        )

def validate_school_email(student_email):
    pattern = r"^[A-Za-z0-9]*@school.{1}com$"
    if not re.match(pattern, student_email):
        raise ValidationError(
            'Invalid school email format. Please use an email ending with "@school.com".'
        )

"""
Locker combination validation:
- Uses regex
- Must be in format "12-12-12"
  - 3 two digit numbers
  - separated by single dash between them
"""

def validate_combination_format(locker_combination):
    pattern = r"^[0-9]{2}-{1}[0-9]{2}-{1}[0-9]{2}$"
    if not re.match(pattern, locker_combination):
        raise ValidationError(
            'Combination must be in the format "12-12-12"'
        )
        
"""
Validators:
- locker number
  - between (including endpoints) 1 and 200

"""


    


    

