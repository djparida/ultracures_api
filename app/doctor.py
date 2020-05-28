from app import app, db, ma, CORS, api, Flask, Resource, DoctorSchema, Doctor, doctor_schema,doctors_schema, json, jsonify, request

class DoctorList(Resource):
    def get(self):
        doctorList = Doctor.query.all()
        return doctors_schema.dump(doctorList)
api.add_resource(DoctorList, '/doctor/list_all')

class DoctorResgister(Resource):
    def post(self):
        newDoctor = Doctor(
            Username = request.json['Username'],
            Email = request.json['Email'],
            Password = request.json['Password']
        )
        db.session.add(newDoctor)
        db.session.commit()
        return doctor_schema.dump(newDoctor)
api.add_resource(DoctorResgister, '/doctor/register')

class DoctorLogin(Resource):
    def get(self):
        Username = request.json['Username']
        Password = request.json['Password']
        doctor = Doctor.query.filter_by(Username=Username,Password=Password).first()
        if doctor is None:
            return None
        return doctor_schema.dump(doctor)

api.add_resource(DoctorLogin, '/doctor/login')


class DoctorGetone(Resource):
    def get(self, doctor_id):
        patient = Doctor.query.get_or_404(doctor_id)
        return doctor_schema.dump(patient)
    def delete(self, doctor_id):
        doctor = Doctor.query.get_or_404(doctor_id)
        db.session.delete(doctor)
        db.session.commit()
        return 'deleted doctor', 204
    def patch(self, doctor_id):
        doctor = doctor.query.get_or_404(doctor_id)
        if 'Username' and 'Password' and 'Email' in request.json:
            doctor.Username = request.json['Username']
            doctor.Password = request.json['Password']
            doctor.Email = request.json['Email']
        db.session.commit()
        return doctor_schema.dump(doctor)

api.add_resource(DoctorGetone, '/doctor/me/<int:doctor_id>')