from sqlalchemy import Column, Integer, String, Numeric
from app import marsh, sqlDB


class Aeroporto(sqlDB.Model):

    __tablename__ = 'aeroportos'

    id_aeroporto = Column(Integer, primary_key=True)
    nome_aeroporto = Column(String(120), nullable=False)
    codigo_iata = Column(String(3), nullable=False)
    cidade = Column(String(120), nullable=False)
    pais = Column(String(120), nullable=False)
    latitude = Column(Numeric(10, 6), nullable=False)
    longitude = Column(Numeric(10, 6), nullable=False)
    altitude = Column(Numeric(10, 6), nullable=False)

    def __init__(self, nome_aeroporto, codigo_iata, cidade, pais, latitude, longitude, altitude) -> None:
        self.nome_aeroporto = nome_aeroporto
        self.codigo_iata = codigo_iata
        self.cidade = cidade
        self.pais = pais
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def create(self):
        sqlDB.session.add(self)
        sqlDB.session.commit()
        return self

    def __repr__(self):
        return f'<Aeroportos: {self.name}'


class AeroportoSchema(marsh.Schema):
    class Meta:
        model = Aeroporto
        sql_session = sqlDB.session
        load_instance = True

    id_aeroporto = marsh.auto_field()
    nome_aeroporto = marsh.auto_field()
    codigo_iata = marsh.auto_field()
    cidade = marsh.auto_field()
    pais = marsh.auto_field()
    latitude = marsh.auto_field()
    longitude = marsh.auto_field()
    altitude = marsh.auto_field()
