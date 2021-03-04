from flask import request, make_response

from .app import app
from db import tables, session_scope


@app.route('/orm/brands/<title>', methods=['POST'])
def new_car(title):
    with session_scope() as session:
        request_data = request.get_json(force=True)

        brand = session.query(tables.Brand).filter_by(title=title).first()
        color = session.query(tables.Color).filter_by(
            title=request_data['color']
        ).first()

        new_car_obj = tables.Car(
            model=request_data['model'],
            price=request_data['price'],
            brand_id=brand.brand_id,
        )
        new_car_obj.colors.append(color)
        session.commit()
        response = make_response({'message': 'car created'}, 201)
        response.headers['Location'] = f"/orm/brands/{title}/{new_car_obj.car_id}"
        return response


@app.route('/orm/brands/<title>/<car_id>', methods=['GET'])
def certain_car(title, car_id):
    with session_scope() as session:
        car = session.query(tables.Car).filter(
            tables.Brand.title == title,
            tables.Car.car_id == car_id
        ).first()
        car_dict = car.to_dict()
        return {'car': car_dict}
