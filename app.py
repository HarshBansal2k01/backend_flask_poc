from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:harsh%40Abi14%23@localhost/deliverydetails"

db.init_app(app)


CORS(app)


# checking db connection


@app.route("/check_db_connection")
def check_db_connection():
    try:
        db.engine.connect()
        return "Database connection successful"
    except Exception as e:
        return f"Database connection error: {str(e)}"


# get request


class User(db.Model):
    # Define the User model to match your "user" table structure
    id = db.Column(db.Integer, primary_key=True)
    phone_no = db.Column(db.String(15))
    pincode = db.Column(db.String(10))
    email_address = db.Column(db.String(255))


class Pickup(db.Model):
    # Define the Pickup model to match your "pickup" table structure
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone_no = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pincode = db.Column(db.Integer)
    pickuplocation = db.Column(db.String(255))
    preferred_time = db.Column(db.Time)


class Delivery(db.Model):
    # Define the Delivery model to match your "delivery" table structure
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone_no = db.Column(db.String(255))
    email = db.Column(db.String(255))
    address = db.Column(db.String(255))
    pincode = db.Column(db.Integer)


@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        user_data = [
            {
                "id": user.id,
                "phone_no": user.phone_no,
                "pincode": user.pincode,
                "email_address": user.email_address,
            }
            for user in users
        ]
        return jsonify(user_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/pickup", methods=["GET"])
def get_pickup():
    try:
        pickups = Pickup.query.all()
        pickup_data = [
            {
                "id": pickup.id,
                "Name": pickup.name,
                "phone_no": pickup.phone_no,
                "email": pickup.email,
                "pincode": pickup.pincode,
                "pickuplocation": pickup.pickuplocation,
                "preferred_time": pickup.preferred_time.strftime("%H:%M:%S")
                if pickup.preferred_time is not None
                else None,
            }
            for pickup in pickups
        ]
        return jsonify(pickup_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/delivery", methods=["GET"])
def get_delivery():
    try:
        deliveries = Delivery.query.all()
        delivery_data = [
            {
                "id": delivery.id,
                "name": delivery.name,
                "phone_no": delivery.phone_no,
                "email": delivery.email,
                "address": delivery.address,
                "pincode": delivery.pincode,
            }
            for delivery in deliveries
        ]
        return jsonify(delivery_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# POST


@app.route("/delivery", methods=["POST"])
def create_delivery():
    try:
        data = request.json  # Assuming the data is sent as JSON in the request body
        new_delivery = Delivery(
            name=data["name"],
            phone_no=data["phone_no"],
            email=data["email"],
            address=data["address"],
            pincode=data["pincode"],
        )
        db.session.add(new_delivery)
        db.session.commit()
        return jsonify({"message": "Delivery data added successfully"})
    except Exception as e:
        # Return a 500 Internal Server Error with a custom error message
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


@app.route("/pickup", methods=["POST"])
def create_pickup():
    try:
        data = request.json  # Assuming the data is sent as JSON in the request body
        new_pickup = Pickup(
            name=data["name"],
            phone_no=data["phone_no"],
            email=data["email"],
            pincode=data["pincode"],
            pickuplocation=data["pickuplocation"],
            preferred_time=data["preferred_time"],
        )
        db.session.add(new_pickup)
        db.session.commit()
        return jsonify({"message": "Pickup data added successfully"})
    except Exception as e:
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


# CHECK


@app.route("/check-email", methods=["POST"])
def check_email():
    try:
        data = request.json  # Assuming the data is sent as JSON in the request body
        email = data.get("email_address")

        if email is not None:
            user = User.query.filter_by(email_address=email).first()

            if user is not None:
                return jsonify(
                    {"success": True, "message": "Email found in the database"}
                )
            else:
                return jsonify(
                    {"success": False, "message": "Email not found in the database"}
                )
        else:
            return jsonify({"success": False, "message": "Invalid input data"}), 400

    except Exception as e:
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


@app.route("/check-phone", methods=["POST"])
def check_phone():
    try:
        data = request.json  # Assuming the data is sent as JSON in the request body
        phone = data.get("phone_no")

        if phone is not None:
            user = User.query.filter_by(phone_no=phone).first()

            if user is not None:
                return jsonify(
                    {"success": True, "message": "Phone found in the database"}
                )
            else:
                return jsonify(
                    {"success": False, "message": "Phone not found in the database"}
                )
        else:
            return jsonify({"success": False, "message": "Invalid input data"}), 400

    except Exception as e:
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


@app.route("/check-pincode", methods=["POST"])
def check_pincode():
    try:
        data = request.json  # Assuming the data is sent as JSON in the request body
        pincode = data.get("pincode")

        if pincode is not None:
            user = User.query.filter_by(pincode=pincode).first()

            if user is not None:
                return jsonify(
                    {"success": True, "message": "Pincode found in the database"}
                )
            else:
                return jsonify(
                    {"success": False, "message": "Pincode not found in the database"}
                )
        else:
            return jsonify({"success": False, "message": "Invalid input data"}), 400

    except Exception as e:
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


# DELETE


@app.route("/delete/<string:email>", methods=["DELETE"])
def delete_user(email):
    try:
        user = User.query.filter_by(email_address=email).first()

        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"success": True, "message": "User Deleted successfully"})
        else:
            return jsonify(
                {"success": False, "message": "User not found in the database"}
            )

    except Exception as e:
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


# PUT


@app.route("/update-user/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        data = request.json  # Assuming the data is sent as JSON in the request body
        phone = data.get("phone_no")
        pincode = data.get("pincode")
        email = data.get("email_address")

        if phone is not None and pincode is not None and email is not None:
            user = User.query.get(id)

            if user is not None:
                user.phone_no = phone
                user.pincode = pincode
                user.email_address = email

                db.session.commit()
                return jsonify(
                    {"success": True, "message": "User updated successfully"}
                )
            else:
                return jsonify(
                    {"success": False, "message": "User not found in the database"}
                )
        else:
            return jsonify({"success": False, "message": "Invalid input data"}), 400

    except Exception as e:
        return (
            jsonify({"error": "Internal Server Error: Failed to add delivery data"}),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True)
