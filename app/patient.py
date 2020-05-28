from app import app, db, ma, CORS, api, Flask, Resource, PatientSchema, Patient, patient_schema,patients_schema, json, jsonify, request


class PatientList(Resource):
    def get(self):
        patientList = Patient.query.all()
        return patients_schema.dump(patientList)
api.add_resource(PatientList, '/patient/list_all')

class PatientResgister(Resource):
    def post(self):
        newPatient = Patient(
            Username = request.json['Username'],
            Email = request.json['Email'],
            Password = request.json['Password']
        )
        db.session.add(newPatient)
        db.session.commit()
        return patient_schema.dump(newPatient)
api.add_resource(PatientResgister, '/patient/register')

class PatientLogin(Resource):
    def get(self):
        Username = request.json['Username']
        Password = request.json['Password']
        patient = Patient.query.filter_by(Username=Username,Password=Password).first()
        if patient is None:
            return None
        return patient_schema.dump(patient)

api.add_resource(PatientLogin, '/patient/login')

class PatientGetone(Resource):
    def get(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        return patient_schema.dump(patient)
    def delete(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        db.session.delete(patient)
        db.session.commit()
        return 'deleted patient', 204
    def patch(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        if 'Username' and 'Password' and 'Email' in request.json:
            patient.Username = request.json['Username']
            patient.Password = request.json['Password']
            Patient.Email = request.json['Email']
        db.session.commit()
        return patient_schema.dump(patient)

api.add_resource(PatientGetone, '/patient/me/<int:patient_id>')



