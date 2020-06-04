template = {
    "info": {
        "description": "powered by Flasgger",
        "termsOfService": "/tos",
        "title": "flask_orator",
        "version": "0.0.1"
    },
    "basePath": "/",
    "paths": {
        "/api/auth/login": {
            "post": {
                
                "requestBody": {
                    "content": {
                        "application/json": {
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
                    },
                    "required": True
                },
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
                    {"bearerAuth": []}
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "me",
                "tags": ["users"]
            }
        },
        "/api/posts/": {
            "get": {
                "security": [
                    {"bearerAuth": []}
                ],
                "parameters": [
                    {
                        "name": "page",
                        "in": "query",
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    },
                    {
                        "name": "per_page",
                        "in": "query",
                        "schema": {
                            "type": "integer",
                            "default": 15,
                            "example": 15
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@index",
                "tags": ["posts"]
            },
            "post": {
                "security": [
                    {"bearerAuth": []}
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "default": '',
                                        "example": 'hello world',
                                        "type": "string"
                                    },
                                    "body": {
                                        "default": '',
                                        "example": 'my father goes to the market with donkey',
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@create",
                "tags": ["posts"]
            }
        },
        "/api/posts/{id}": {
            "get": {
                "security": [
                    {"bearerAuth": []}
                ],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@show",
                "tags": ["posts"]
            },
            "put": {
                "security": [
                    {"bearerAuth": []}
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "default": '',
                                        "example": 'hello world',
                                        "type": "string"
                                    },
                                    "body": {
                                        "default": '',
                                        "example": 'my father goes to the market with donkey',
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "required": True
                },
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@update",
                "tags": ["posts"]
            },
            "delete": {
                "security": [
                    {"bearerAuth": []}
                ],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@show",
                "tags": ["posts"]
            },
        },
        "/api/posts/{id}/comments": {
            "post": {
                "security": [
                    {"bearerAuth": []}
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "body": {
                                        "default": '',
                                        "example": 'my father goes to the market with donkey',
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "required": True
                },
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@comment.create",
                "tags": ["posts"]
            },
            "delete": {
                "security": [
                    {"bearerAuth": []}
                ],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "posts@comment.delete",
                "tags": ["posts"]
            }
        }
    },
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    }

}