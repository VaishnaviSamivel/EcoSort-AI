# EcoSort AI 🌱

## AI-Powered Waste Segregation and Disposal Guidance Assistant

EcoSort AI is a generative-AI-powered sustainability assistant that helps users understand how everyday waste items can be categorized and handled more responsibly.

The project addresses **UN Sustainable Development Goal 12: Responsible Consumption and Production**.

## Problem

People often find it difficult to determine how everyday items should be segregated or disposed of. Incorrect segregation can reduce the effectiveness of recycling and waste-processing systems.

Examples include:

* Old shoes
* Mobile phones
* Batteries
* Food waste
* Plastic bottles
* Clothing

## Solution

EcoSort AI accepts a natural-language description of a waste item and uses generative AI to:

1. Understand the item description.
2. Classify the item into an appropriate waste category.
3. Explain the reasoning.
4. Recommend a responsible action.
5. Provide a sustainability tip.
6. Indicate when local verification may be required.

## Waste Categories

The system supports:

* Wet / Organic Waste
* Dry / Recyclable Waste
* E-Waste
* Hazardous Waste
* Textile / Reusable
* Special / Local Collection
* Unknown / Needs Verification

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* Generative AI API
* Structured JSON generation

### Environment

* Python virtual environment
* Environment variables for API credentials

## System Architecture

```text
User
  ↓
EcoSort AI Web Interface
  ↓
FastAPI Backend
  ↓
Generative AI Model
  ↓
Waste Classification
  ↓
Reason + Recommended Action
  ↓
Sustainability Guidance
  ↓
User
```

## Responsible AI

EcoSort AI is designed with responsible-use principles:

* **Transparency:** The system provides a reason for its classification.
* **Uncertainty handling:** Items that require additional verification can be flagged.
* **Privacy:** API credentials are stored in environment variables and are not included in the source code.
* **Safety:** The system avoids inventing specific recycling facilities.
* **Local verification:** Waste-management rules can differ by location, so users are advised to verify location-dependent disposal instructions.

## Example

### Input

```text
old shoe
```

### AI Output

```text
Category:
Textile / Reusable

Recommended action:
Reuse, repair, donate, or use an appropriate collection service.

Sustainability principle:
Extend the useful life of products before disposal.
```

## Future Scope

* Image-based waste recognition
* Multilingual interaction
* Local waste-management databases
* Retrieval-grounded disposal guidance
* Mobile application
* Integration with local recycling and collection services

## SDG Alignment

**Primary SDG:** SDG 12 — Responsible Consumption and Production

EcoSort AI encourages responsible consumption, reuse, repair, recycling, and informed disposal decisions.

## Project Status

Working prototype completed with:

* AI-powered classification
* FastAPI backend
* Interactive frontend
* Responsible AI considerations
* Sustainability recommendations
