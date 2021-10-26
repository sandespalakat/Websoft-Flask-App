from datetime import datetime
from fpdf import FPDF
from flask_mail import Mail, Message, Attachment
from course import mail
from course import app


def create_pdf(candidate, course, amount, date, reason):
    """
    create and e-mail the pdf invoice
    :param candidate: Name of the candidate
    :param course: Course of the candidate
    :param amount: Amount paid during this transaction
    :param date: Date of invoice
    :param reason: Reason of invoice
    :return: boolean
    """

    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # create a cell
    pdf.cell(200, 10, txt="Invoice",
             ln=1, align='C')

    # add another cell and add information
    pdf.cell(200, 10, txt="Name: " + candidate,
             ln=2, align='C')
    pdf.cell(200, 10, txt="Course: " + course,
             ln=2, align='C')
    pdf.cell(200, 10, txt="Amount: " + str(amount),
             ln=2, align='C')
    pdf.cell(200, 10, txt="Reason: " + reason,
             ln=2, align='C')
    pdf.cell(200, 10, txt="Date: " + str(date.strftime("%m/%d/%Y")),
             ln=2, align='C')

    # save the pdf with name .pdf
    now = datetime.now()
    pdf.output("pdfs/" + candidate + str(now.strftime("%m_%d_%Y_%H_%M_%S")) + ".pdf")
    # e-mailing the pdf as an attachment to the candidate
    msg = Message(
        'Invoice from ABC',
        sender='sandescolab@gmail.com',
        recipients=['sandesdevasree@gmail.com']
    )
    msg.body = 'Invoice of purchase amount ' + str(amount)
    # attaching the pdf invoice
    with open("pdfs/" + candidate + str(now.strftime("%m_%d_%Y_%H_%M_%S")) + ".pdf", 'rb') as fh:
        msg.attach(candidate + str(now.strftime("%m_%d_%Y_%H_%M_%S")) + ".pdf", "application/pdf", fh.read())
    try:  # sending email
        mail.send(msg)
        return True
    except:  # return False if there is any error in sending email
        return False
