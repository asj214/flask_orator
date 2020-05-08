template = {
    "info": {
        "description": "powered by Flasgger",
        "termsOfService": "/tos",
        "title": "flask_orator",
        "version": "0.0.1"
    },
    "basePath": "/",  # base bash for blueprint registration
    "paths": {
        "/api/auth/login": {
            "post": {
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "email": {
                                    "default": '',
                                    "example": 'asj214@naver.com',
                                    "type": "string"
                                },
                                "password": {
                                    "default": '',
                                    "example": '1234',
                                    "type": "string"
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "로그인",
                "tags": ["users"]
            }
        },
        "/api/auth/me": {
            "get": {
                "security": [
                    {
                        "Bearer": []
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "me",
                "tags": ["users"]
            }
        }
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }


}