# Websoft-Flask-App
Create a simple ERP system where:

Admin can add a new candidate - with details like:

1. Name
2. Email
3. Phone

Auto generate a Candidate ID. No need of edit / delete.

Admin can assign candidate to multiple courses:

1. Selecting the candidate from dropdown
2. Course name
3. Total fees
4. Installment amount
5. Date of joining

Auto generate a Enrollment ID. No need of edit / delete.

Admin can create a new invoice by:

1. Selecting the candidate from dropdown
2. Selecting the enrollment id filtered by the candidate selected on step 1
3. Enter amount
4. Select Date
5. Enter reason

Auto generate a Invoice ID and a simple chalan PDF (You can create your own) which will be auto emailed to the candidate.  No need of edit / delete.

pip installs
1. flask
2. flask sqlalchmey
3. validate_email
4. Flask-wtf
5. fpdf
6. flask_mail

