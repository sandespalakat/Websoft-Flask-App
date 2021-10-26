from course import app
from flask import render_template, redirect, url_for, flash, request, jsonify
from course.models import Candidate, Candidatecourses, Invoice
from course.forms import CandidateForm, AssignForm, InvoiceForm
from course.helper import create_pdf
from course import db


@app.route("/", methods=["GET", "POST"])
@app.route("/add-candidate", methods=["GET", "POST"])
def candidate_page():
    """
        Page for adding candidates
    :return: render_template
    """
    form = CandidateForm()
    if form.validate_on_submit():  # on successful form validation
        candidate = Candidate(name=form.name.data, email_address=form.email.data, phone=form.phone.data)
        db.session.add(candidate)
        db.session.commit()
        flash("Candidate created", category="success")
        return redirect(url_for("candidate_page"))
    if form.errors != {}:  # on validation error
        for error_msg in form.errors.values():
            flash("There was an error " + error_msg[0], category="danger")
    return render_template("add-candidate.html", form=form, head_title="Add Candidate", active_page="home")


@app.route("/assign-candidate", methods=["GET", "POST"])
def assign_candidate():
    """
    Page for assigning courses to the candidates
    :return: render_template
    """
    db.session.flush()
    form = AssignForm()
    if form.validate_on_submit():  # on successful form validation
        courses = Candidatecourses(candidate_id=form.candidate_id.data, course=form.course.data,
                                   total_fees=form.total_fees.data, installment=form.installment.data,
                                   doj=form.doj.data)
        db.session.add(courses)
        db.session.commit()
        flash("Candidate assigned", category="success")
        return redirect(url_for("assign_candidate"))
    if form.errors != {}:  # on validation errors
        for error_msg in form.errors.values():
            flash("There was an error " + error_msg[0], category="danger")
    return render_template("assign-candidate.html", form=form, head_title="Assign Candidate", active_page="assign")


@app.route("/create-invoice", methods=["GET", "POST"])
def create_invoice():
    """
    Page for creating invoice and emailing the pdf invoice to the candidate
    :return: render_template
    """

    form = InvoiceForm()
    if form.validate_on_submit():  # if no errors in form
        invoice = Invoice(candidate_id=form.candidate_id.data, course_id=form.course_id.data, amount=form.amount.data,
                          date=form.date.data, reason=form.reason.data)
        db.session.add(invoice)
        db.session.commit()
        # finding details for creating pdf invoice
        course = Candidatecourses.query.filter_by(id=form.course_id.data).first().course
        candidate = Candidate.query.filter_by(id=form.candidate_id.data).first().name
        amount = form.amount.data
        date = form.date.data
        reason = form.reason.data
        # creating mailing pdf invoice
        mail = create_pdf(candidate, course, amount, date, reason)
        if mail:
            flash("Invoice created and emailed to the candidate", category="success")
        else:
            flash("Something wrong has happened", category="danger")
        return redirect(url_for('create_invoice'))
    if form.errors != {}:  # on form errors
        for error_msg in form.errors.values():
            flash("There was an error " + error_msg[0], category="danger")
    return render_template("create-invoice.html", form=form, head_title="Create Invoice", active_page="invoice")


@app.route("/get-courses", methods=["GET", "POST"])
def get_courses():
    """
    Fetch the courses by candidate id
    :return: json
    """
    s_id = request.args.get("c_id")  # getting the argument from url
    # finding the courses for the candidate id = s_id
    courses = [(c.id, c.course) for c in Candidatecourses.query.filter(Candidatecourses.candidate_id == s_id).all()]
    return jsonify(result=courses)
