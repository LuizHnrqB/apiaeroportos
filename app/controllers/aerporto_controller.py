from flask import Blueprint, request, jsonify, make_response
from app import sqlDB, marsh
from app.models.aeroporto import Aeroporto, AeroportoSchema


class AirportController:
    airport_controller = Blueprint(
        name='aeroporto_controller', import_name=__name__)

    @airport_controller.route('/aeroportos', methods=['GET'])
    def get_airport():
        aeroporto_list = Aeroporto.query.all()
        aeroporto_schema = AeroportoSchema(many=True)
        aeroporto_json = aeroporto_schema.dump(aeroporto_list)
        return make_response(jsonify({"Aeroportos": aeroporto_json}), 200)

    @airport_controller.route('/aeroportos/<String: iata>', methods=['GET'])
    def get_airport(iata):
        aeroporto = Aeroporto.query.filter_by(codigo_iata=iata).first()
        if aeroporto:
            aeroporto_schema = AeroportoSchema()
            aeroporto_json = aeroporto_schema.dump(aeroporto)
            return make_response(jsonify({"Aeroporto": aeroporto_json}), 200)
        else:
            return make_response(jsonify({"Aeroporto": None}), 404)

    @airport_controller.route('/aeroportos', methods=['POST'])
    def post_airport():
        data = request.get_json()
        aeroporto_schema = AeroportoSchema(unknown=marsh.EXCLUDE)
        aeroporto = aeroporto_schema.load(data)
        result = aeroporto_schema.dump(aeroporto.create())
        return make_response(jsonify({"Aeroporto": result}), 201)

    @airport_controller.route('/aeroportos/<String: iata>', methods=['PUT'])
    def put_airport(iata):
        aeroporto = Aeroporto.query.filter_by(codigo_iata=iata).first_or_404()
        aeroporto_schema = AeroportoSchema()
        data = request.get_json()

        if data.get('nome_aeroporto'):
            aeroporto.nome_aeroporto = data['nome_aeroporto']
        if data.get('codigo_iata'):
            aeroporto.codigo_iata = data['codigo_iata']
        if data.get('cidade'):
            aeroporto.cidade = data['cidade']
        if data.get('pais'):
            aeroporto.pais = data['pais']
        if data.get('latitude'):
            aeroporto.latitude = data['latitude']
        if data.get('longitude'):
            aeroporto.longitude = data['longitude']
        if data.get('altitude'):
            aeroporto.altitude = data['altitude']

        sqlDB.session.add(aeroporto)
        sqlDB.session.commit()

        update_aeroporto = aeroporto_schema.dump(aeroporto)
        return make_response(jsonify({"Aeroporto": update_aeroporto}), 200)

    @airport_controller.route('/aeroportos/<String: iata>', methods=['DELETE'])
    def delete_airport(iata):
        aeroporto = Aeroporto.query.filter_by(codigo_iata=iata).first_or_404()
        sqlDB.session.delete(aeroporto)
        sqlDB.session.commit()
        return make_response(jsonify(), 204)
