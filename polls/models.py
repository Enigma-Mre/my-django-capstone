from django.db import models

# Define the models here.

class Questions(models.Model):
    """
    Represents a question in the application.

    Attributes:
        question_text (CharField): The text of the question, limited to 200 characters.
        pub_date (DateTimeField): The date and time when the question was published.
    """

    # Define a CharField for the question text with a maximum length of 200 characters.
    question_text = models.CharField(max_length=200)

    # Define a DateTimeField for the publication date.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Return the string representation of the question, which is the question text."""
        return self.question_text


class Choice(models.Model):
    """
    Represents a choice associated with a question.

    Attributes:
        questions (ForeignKey): A foreign key linking to a Questions instance.
        choice_text (CharField): The text of the choice, limited to 200 characters.
        votes (IntegerField): The number of votes the choice has received, defaulting to 0.
    """

    # Define a ForeignKey relationship with the Questions model.
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)

    # Define a CharField for the choice text with a maximum length of 200 characters.
    choice_text = models.CharField(max_length=200)

    # Define an IntegerField for the votes count with a default value of 0.
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return the string representation of the choice, which is the choice text."""
        return self.choice_text
