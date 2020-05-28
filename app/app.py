from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_restful import Api, Resource 
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ultracures.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Username = db.Column(db.VARCHAR(20), nullable = False)
    Email = db.Column(db.VARCHAR(50), nullable = False)
    Password = db.Column(db.VARCHAR(20), nullable = False)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Username = db.Column(db.VARCHAR(20), nullable = False)
    Email = db.Column(db.VARCHAR(50), nullable = False)
    Password = db.Column(db.VARCHAR(20), nullable = False)

class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id','Username','Email','Password')

class DoctorSchema(ma.Schema):
    class Meta:
        fields = ('id','Username','Email','Password')

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)

class ApiIssuer(Resource):
    def get(self):
        Base_Url = request.base_url

        patient_list = '(get) ' + Base_Url + 'patient/list_all'
        patient_login = '(get) ' + Base_Url + 'patient/login'
        patient_resgister = '(post) ' + Base_Url + 'patient/register'
        getSingle_patient = '(get) ' + Base_Url + 'patient/me/<id>'
        patient_edit = '(patch) ' + Base_Url + 'patient/me/<id>'
        patient_delete = '(delete) ' + Base_Url + 'patient/me/<id>'
        PatientApi = {'patient_list':patient_list,'patient_login':patient_login,'patient_resgister':patient_resgister,'getSingle_patient':getSingle_patient,'patient_edit':patient_edit,'patient_delete':patient_delete}

        doctor_list = '(get) ' + Base_Url + 'doctor/list_all'
        doctor_login = '(get) ' + Base_Url + 'doctor/login'
        doctor_resgister = '(post) ' + Base_Url + 'doctor/register'
        getSingle_doctor = '(get) ' + Base_Url + 'doctor/me/<id>'
        doctor_edit = '(patch) ' + Base_Url + 'doctor/me/<id>'
        doctor_delete = '(delete) ' + Base_Url + 'doctor/me/<id>'
        DoctorApi = {'doctor_list':doctor_list,'doctor_resgister':doctor_resgister,'doctor_login':doctor_login,'getSingle_doctor':getSingle_doctor,'doctor_edit':doctor_edit,'doctor_delete':doctor_delete}

        return jsonify(PatientApi, DoctorApi)
api.add_resource(ApiIssuer,'/')




