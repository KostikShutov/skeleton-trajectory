#!/usr/bin/python

import os
import matplotlib
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.coordinate.CoordinateTransformer import CoordinateTransformer
from components.part.PartParser import PartParser
from components.part.PartTransformer import PartTransformer
from generator.InitService import InitService
from generator.PredictService import PredictService
from helpers.Env import env

matplotlib.use('Agg')

app: Flask = Flask(__name__, template_folder=os.getcwd())
cors: CORS = CORS(app)


def getCoordinateParser() -> CoordinateParser:
    return CoordinateParser()


def getInitService() -> InitService:
    return InitService(
        coordinateTransformer=CoordinateTransformer(),
    )


def getPartParser() -> PartParser:
    return PartParser(
        coordinateParser=CoordinateParser(),
    )


def getPredictService() -> PredictService:
    return PredictService(
        partTransformer=PartTransformer(),
        coordinateTransformer=CoordinateTransformer(),
    )


coordinateParser = getCoordinateParser()
initService = getInitService()
partParser = getPartParser()
predictService = getPredictService()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/openapi')
def openapi():
    return render_template('openapi.yaml')


@app.route('/init', methods=['POST'])
@cross_origin()
def init():
    data: any = request.get_json(force=True, silent=True)
    coordinates: list[Coordinate] = coordinateParser.parse(data=data)

    return initService.init(course=coordinates)


@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    data: any = request.get_json(force=True, silent=True)
    part, modelName = partParser.parse(data=data)

    return predictService.predict(part=part, modelName=modelName)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(env['SERVER_PORT']))
