from course import db

class Candidate(db.Model):
    """
        Candidate table
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, )
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    courses = db.relationship("Candidatecourses", backref="taken_candidate", lazy=True)
    invoices = db.relationship("Invoice", backref="candidate_invoice", lazy=True)


class Candidatecourses(db.Model):
    """
        Candidate course table
    """
    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), db.ForeignKey("candidate.id"))
    course = db.Column(db.String(), nullable=False)
    total_fees = db.Column(db.Float(), nullable=False)
    installment = db.Column(db.Float(), nullable=False)
    doj = db.Column(db.Date(), nullable=False)
    invoice = db.relationship("Invoice", backref="candidate_invoice1", lazy=True)

class Invoice(db.Model):
    """
        Invoice table
    """
    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), db.ForeignKey("candidate.id"))
    course_id = db.Column(db.Integer(), db.ForeignKey("candidatecourses.id"))
    amount = db.Column(db.String(10), nullable=False )
    date = db.Column(db.Date(), nullable=False)
    reason = db.Column(db.String(10), nullable=True)


