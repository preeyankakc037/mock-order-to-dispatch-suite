# Mock Order-to-Dispatch Automation Suite

A QA automation portfolio project built with Python, Playwright, Requests, and Pytest. It simulates an operational order-to-dispatch workflow inspired by logistics and delivery platforms.

## 🏢 Workflow Architecture

| Workflow Stage | Target Platform | Test Strategy |
| --- | --- | --- |
| **1. Order Creation (UI)** | SauceDemo | Validates checkout flow and verifies that numerical pricing math holds ($\text{Item Total} + \text{Tax} == \text{Total}$). |
| **2. Order Dispatch (API)** | ReqRes API | Validates backend dispatch creation (positive path) and tests payload validation for missing fields (negative path). |
| **3. Continuous Integration** | GitHub Actions | Automatically triggers and executes the full test suite in an Ubuntu container on every push to `main`. |

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.11+
* **Test Runner:** Pytest
* **UI Engine:** Playwright (`pytest-playwright`)
* **API Client:** Requests
* **Environment Secrets:** Python-dotenv

## 🚀 Local Setup & Execution

1. **Clone the repository and activate virtual environment:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/mock-order-to-dispatch-suite.git](https://github.com/YOUR_USERNAME/mock-order-to-dispatch-suite.git)
   cd mock-order-to-dispatch-suite
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies and browser binaries:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. **Configure environment secrets:**
   Create a `.env` file in the project root directory:
   ```env
   REQRES_API_KEY=your_reqres_api_key
   ```

4. **Execute test suite:**
   ```bash
   # Run full test suite headlessly
   pytest -v

   # Run UI test visually in headed mode
   pytest tests/test_ui_checkout.py -v --headed
   ```

## 📈 Future Scope / Enhancement Roadmap

* Implement **Page Object Model (POM)** pattern to decouple UI elements from test execution logic.
* Expand API coverage using data-driven testing (`@pytest.mark.parametrize`) for complex payload variations.
* Integrate `pytest-html` or Allure reporting artifacts into the GitHub Actions CI workflow.