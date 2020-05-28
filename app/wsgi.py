from app import app, db, api, CORS
import patient
import doctor


if __name__ == '__main__':
    db.create_all()
    # app.run(debug=True)
    app.run(debug = True,host='0.0.0.0', port=443, ssl_context='adhoc')