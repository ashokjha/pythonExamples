# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:11:09 2021

@author: Ashok Kumar Jha
"""
from flask import Flask
from flask_restful import Resource, reqparse ,Api

TGS = Flask(__name__)
api = Api(TGS)

articles = [
    {
        "category": "python",
        "views": 100,
        "title": "Dictionary"
    },
    {
        "category": "java",
        "views": 200,
        "title": "java10"
    },
    {
        "category": "elastic",
        "views": 300,
        "title": "elasticsearch"
    }
]

class Article(Resource):
    def get(self, category):
        for article in articles:
            if(category == article["category"]):
                return article, 200
        return "category not found", 404

    def post(self, category):
        parser = reqparse.RequestParser()
        parser.add_argument("views")
        parser.add_argument("title")
        args = parser.parse_args()

        for article in articles:
            if(category == article["category"]):
                return "category  {} already exists".format(category), 400

        article = {
            "category": category,
            "views": args["views"],
            "title": args["title"]
        }
        articles.append(article)
        return article, 201

    def put(self, category):
        parser = reqparse.RequestParser()
        parser.add_argument("views")
        parser.add_argument("title")
        args = parser.parse_args()

        for article in articles:
            if(category == article["category"]):
                article["views"] = args["views"]
                article["title"] = args["title"]
                return article, 200

        article = {
            "category": category,
            "views": args["views"],
            "title": args["title"]
        }
        articles.append(article)
        return article, 201

    def delete(self, category):
        global articles
        articles = [article for article in articles if article["category"] != category]
        return "{} is deleted.".format(category), 200

api.add_resource(Article, "/category/<string:category>")

TGS.run(debug=True,port=8080)
