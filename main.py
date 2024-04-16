from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import api_router as chatbot_router

app = FastAPI()

# CORS configuration
origins = [
    
   
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)









    
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from services import router as chatbot_router


# app = FastAPI(
#     title="Chatbot API",
#     version="1.0",
# )

# # CORS configuration
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include the chatbot router
# app.include_router(chatbot_router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)









