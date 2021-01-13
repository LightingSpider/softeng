from flask import Flask, request, jsonify
from flask_restx import Resource, Api, fields, marshal_with, abort

app = Flask(__name__)
api = Api(app=app, version="1.0", title="My APIs")


@api.route('/charge/<charge_id>')
class Charge(Resource):

    def get(self,charge_id):
        try:
            return {
                    "charge_id": charge_id,
                    "user_id": 1,
                    "station_id": 1,
                    "parking_id": 1,
                    "total_cost": 15,
                    "date": "11 / 01 / 2021",
                    "payment_method": "card",
                    "bonus_points": 150,
                    "protocol": "i dont know",
                    "start_power_percentage": 33,
                    "end_power_percentage": 88,
                    "start_time": "14:22",
                    "end_time": "15:00",
                    "total_kwatts": "1100",
                    "cost_per_kwh": 2
            }

        except:
            abort(400, 'Error', statusCode=400)


    # def put(self):

    # def delete(self):

@api.route('/user/<user_id>')
class User(Resource):
    def get(self, user_id):

        try:
            return {
                    "user_id": user_id,
                    "username": "Big Dick",
                    "password": "ilovecoding69",
                    "first_name": "Mitsaras",
                    "last_name": "Komninakos",
                    "date_of_birth": "01/01/2001",
                    "cars": [],
                    "contact": {
                        "address": {
                            "street": "ABC street",
                            "number": 3,
                            "city": "Pagrati",
                            "zip": 46373,
                            "country": "Greece"
                        },
                        "phones": [
                            {
                                "mobile": 691111115
                            },
                            {
                                "mobile": 691111116
                            }
                        ],
                        "mails": [
                            {
                                "mail": "lolaras@gmail.com"
                            }
                        ]
                    }
                }


        except KeyError:
            abort(400, 'Error', statusCode=400)


@api.route('/station/<station_id>')
class Station(Resource):
    def get(self, parking_id):

        try:
            return \
                {
                    'parking_id': parking_id,
                    'rating': 5,
                    'comments': 'Nice!'
                }

        except KeyError:
            abort(400, 'Error', statusCode=400)


@api.route('/station/<station_id>/<connection_id>')
class Connection(Resource):
    def get(self, parking_id, station_id):

        try:
            return \
                {
                    "station_id": station_id,
                    "parking_id": parking_id,
                    "charging_power": 100,
                    "type": "Fast",
                    "status": "Available",
                }

        except KeyError:
            abort(400, 'Error', statusCode=400)


app.run(debug=True)