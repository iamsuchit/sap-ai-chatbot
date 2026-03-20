from app.config import OPENAI_API_KEY
from fastapi import FastAPI

from app.services.pdf_loader import load_all_pdfs
from app.services.vector_store import create_vectorstore
from app.services.ai_chain import create_chain
from app.routes.webhook import create_webhook

# INIT APP
app = FastAPI()

# LOAD DATA
text = load_all_pdfs()
vectorstore = create_vectorstore(text)

# AI
chain = create_chain(vectorstore)

# ROUTES
app.include_router(create_webhook(chain))


@app.get("/")
def home():
    return {"message": "✅ AI Bot Running"}