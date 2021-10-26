from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from course.models import Candidate, Candidatecourses


class CandidateForm(FlaskForm):
    """
        Form for adding a candidate
    """

    def validate_email(self, email):
        email = Candidate.query.filter_by(email_address=email.data).first()
        if email:
            raise ValidationError("Email exists")

    def validate_phone(self, phone):
        phone = Candidate.query.filter_by(phone=phone.data).first()
        if phone:
            raise ValidationError("Phone exists")

    name = StringField(label="Candidate Name", validators=[Length(min=1, max=50), DataRequired()])
    email = StringField(label="Candidate Email", validators=[DataRequired(), Email()])
    phone = StringField(label="Candidate Phone", validators=[DataRequired(), Length(min=10, max=13)])
    submit = SubmitField(label="Add Candidate")


class AssignForm(FlaskForm):
    """
        Form for assigning a course to a candidate
    """
    candidate_id = SelectField(label="Select Candidate", choices=[(c.id, c.name) for c in Candidate.query.all()],
                               validators=[DataRequired()])
    course = StringField(label="Course", validators=[DataRequired()])
    total_fees = FloatField(label="Total Fees", validators=[DataRequired()])
    installment = FloatField(label="Installment", validators=[])
    doj = DateField(label="Date of joining", validators=[])
    submit = SubmitField(label="Assign Course")


class InvoiceForm(FlaskForm):
    """
        Form for adding an invoice
    """
    candidate_id = SelectField(label="Select Candidate", choices=[(c.id, c.name) for c in Candidate.query.all()],
                               validators=[DataRequired()])
    course_id = SelectField(label="Select Course", choices=[(c.id, c.course) for c in Candidatecourses.query.all()],
                            validators=[DataRequired()])
    amount = FloatField(label="Amount", validators=[DataRequired()])
    date = DateField(label="Date ", validators=[])
    reason = StringField(label="Reason", validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField(label="Add Invoice")
