# Mock Order-to-Dispatch Automation Suite

A light QA automation suite simulating an end-to-end operational flow: UI checkout, backend dispatch API processing, and continuous integration.

## 📌 Architecture & Test Scope

- **UI Automation (SauceDemo):** Validates user checkout flow and verifies that numerical pricing logic aligns ($\text{Item Total} + \text{Tax} == \text{Total}$).
- **API Automation (ReqRes):** Validates order dispatch creation (positive path) and negative test cases for missing driver payload parameters.
- **CI/CD Pipeline (GitHub Actions):** Automatically executes test runs on every pull request and push to `main`.

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Test Runner:** Pytest
- **UI Automation:** Playwright
- **API Automation:** Requests
- **Environment Management:** Python-dotenv

## 🚀 Quickstart

1. **Clone & Setup Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   playwright install



