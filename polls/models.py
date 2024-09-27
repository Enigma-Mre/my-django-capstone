from django.db import models

# Define the models here.

class Questions(models.Model):
    
    # Define a CharField for the question text with a maximum length of 200 characters.
    question_text = models.CharField(max_length = 200)

    # Define a DateTimeField for the publication date.
    pub_date = models.DateTimeField('date published')

    # Define a string representation for the Questions model.

    def __str__(self):
        return self.question_text

class Choice(models.Model):

    # Define a ForeignKey relationship with the Questions model.
    questions = models.ForeignKey(Questions, on_delete = models.CASCADE)

    # Define a CharField for the choice text with a maximum length of 200 characters.
    choice_text = models.CharField(max_length = 200)

    # Define an IntegerField for the votes count with a default value of 0.
    votes = models.IntegerField(default = 0)

    # Define a string representation for the Choice model.
    
    def __str__(self): 
        return self.choice_text