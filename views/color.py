from flask import request, make_response

from .app import app
from db import Session, tables, session_scope


# Какого цвета конкретная машина
@app.route('/orm/brands/<title>/<car_id>/<color_id>', methods=['GET'])
def get_car_with_color(title, car_id, color_id):
    with session_scope() as session:
        color = session.query(tables.Color).filter(
            tables.Brand.title == title,
            tables.Car.car_id == car_id,
            tables.Color.color_id == color_id
        ).first()
        return {'color': color.to_dict()}


@app.route('/orm/colors', methods=['GET', 'POST'])
def get_colors():
    # Все доступные цвета
    if request.method == 'GET':
        with session_scope() as session:
            colors_list = session.query(tables.Color).all()
            result_list = [color.to_dict() for color in colors_list]
            return {'colors': result_list}
    # Создание нового цвета
    else:
        with session_scope() as session:
            request_data = request.get_json(force=True)
            new_color = tables.Color(title=request_data['title'])
            session.add(new_color)
            session.commit()
            response = make_response({'message': 'color created'}, 201)
            response.headers['Location'] = f"/orm/colors/{new_color.color_id}"
            return response


# Конкретный цвет
@app.route('/orm/colors/<color_id>', methods=['GET', 'PUT', 'DELETE'])
def get_some_color(color_id):
    with session_scope() as session:
        if request.method == 'GET':
            color = session.query(tables.Color).filter_by(color_id=color_id).first()
            color_dict = color.to_dict()
            return {'color': color_dict}
        elif request.method == 'DELETE':
            color = session.query(tables.Color).filter_by(color_id=color_id).first()
            session.delete(color)
            return {'message': 'color deleted'}
        else:
            color = session.query(tables.Color).filter_by(color_id=color_id).first()
            request_data = request.get_json(force=True)
            color.title = request_data['title']
            return {'message': 'color updated'}
