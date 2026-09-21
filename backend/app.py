from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json

# Load .env
load_dotenv()

# --------------------------------------------------
# FastAPI
# --------------------------------------------------

app = FastAPI(
    title="EcoSort AI",
    description="AI-powered waste segregation and disposal guidance assistant",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Gemini AI Configuration
# --------------------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash-lite"


# --------------------------------------------------
# Request Model
# --------------------------------------------------

class WasteRequest(BaseModel):
    item: str


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to EcoSort AI",
        "status": "running",
        "ai_model": MODEL_NAME
    }


# --------------------------------------------------
# AI Waste Analysis
# --------------------------------------------------

@app.post("/analyze")
def analyze_waste(request: WasteRequest):

    item = request.item.strip()

    if not item:
        return {
            "item": "",
            "category": "Unknown",
            "reason": "No waste item was provided.",
            "recommended_action": "Please enter an item to analyze.",
            "sustainability_tip": "Consider reducing, reusing, repairing, or recycling items before disposal.",
            "needs_local_verification": True
        }

    prompt = f"""
You are EcoSort AI, an AI assistant for responsible waste segregation.

Analyze the user's waste item and classify it into exactly ONE of these categories:

1. Wet / Organic Waste
2. Dry / Recyclable Waste
3. E-Waste
4. Hazardous Waste
5. Textile / Reusable
6. Special / Local Collection
7. Unknown / Needs Verification

User's item:
"{item}"

Rules:

- Understand the meaning of the item, not just individual keywords.
- Consider common household waste-management practices.
- Old shoes, clothes and reusable fabric items can belong to Textile / Reusable.
- Phones, laptops, chargers and electronic devices belong to E-Waste.
- Batteries, paints, pesticides and chemicals require special or hazardous handling.
- Food scraps and vegetable/fruit peels are Wet / Organic.
- Paper, cardboard and many common recyclable containers are Dry / Recyclable.
- Large or unusual items may require Special / Local Collection.
- Do NOT invent the name of a recycling facility or collection center.
- If disposal depends on local regulations, set needs_local_verification to true.
- If you are uncertain, use Unknown / Needs Verification.
- Give practical sustainability advice.
- Do not claim a disposal method is universally valid when local rules may differ.

Return ONLY valid JSON matching the requested schema.
"""


    response_schema = {
        "type": "OBJECT",
        "properties": {
            "item": {
                "type": "STRING"
            },
            "category": {
                "type": "STRING"
            },
            "reason": {
                "type": "STRING"
            },
            "recommended_action": {
                "type": "STRING"
            },
            "sustainability_tip": {
                "type": "STRING"
            },
            "needs_local_verification": {
                "type": "BOOLEAN"
            }
        },
        "required": [
            "item",
            "category",
            "reason",
            "recommended_action",
            "sustainability_tip",
            "needs_local_verification"
        ]
    }

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.2,
                max_output_tokens=500
            )
        )

        result = json.loads(response.text)

        return result

    except Exception as e:

        return {
            "item": item,
            "category": "Unknown / Needs Verification",
            "reason": "The AI service could not confidently analyze this item.",
            "recommended_action": "Please check local waste-management guidance.",
            "sustainability_tip": "Consider reducing, reusing, repairing, or recycling products whenever possible.",
            "needs_local_verification": True,
            "error": str(e)
        }