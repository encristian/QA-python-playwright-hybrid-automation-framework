# Python Playwright Hybrid Automation Framework

This is a hybrid UI and API automation testing project built with Python, Playwright and PyTest.

The project tests the main UI and API flows from the Automation Exercise demo e-commerce application:

https://automationexercise.com/

## Project Purpose

The purpose of this project is to demonstrate QA Automation skills using Python, Playwright, PyTest and Requests.

This project covers:

- UI automation testing
- API automation testing
- Hybrid API and UI testing
- End-to-end test scenarios
- Positive test scenarios
- Negative test scenarios
- Page Object Model
- Reusable PyTest fixtures
- Test data generation with Faker
- GET, POST, PUT and DELETE requests
- Status code validation
- Response body validation
- API response structure validation
- Query parameter testing
- Form data testing
- Browser network monitoring
- Request and response validation
- API mocking
- Simulated server errors
- Request blocking
- Cross-browser testing
- Parallel test execution
- PyTest markers
- HTML test reports
- Screenshots and Playwright traces
- GitHub Actions continuous integration
- Git version control

## Background

I have 2 years of experience as a QC Tester and created this project to practice and demonstrate QA Automation skills using Python, Playwright, PyTest and Requests.

This project is part of my QA Automation portfolio and is intended to showcase my ability to write automated UI and API tests, build a reusable test automation framework, combine frontend and backend testing and use version control with Git.

## Technologies Used

- Python
- Playwright
- PyTest
- Requests
- Faker
- python-dotenv
- pytest-html
- pytest-xdist
- HTML
- CSS selectors
- Visual Studio
- Git
- GitHub
- GitHub Actions

## Test Scenarios Covered

### UI Tests

- Verify that the homepage is displayed
- Verify navigation to the Products page
- Verify navigation to the Signup/Login page
- Verify navigation to the Contact Us page
- Verify navigation to the shopping cart
- Verify login form fields accept user input
- Verify signup form fields accept generated user data
- Verify invalid login displays the correct error message
- Search for products
- Verify searched products are displayed
- Open product details
- Verify product name
- Verify product category
- Verify product price
- Verify product availability
- Verify product condition
- Verify product brand
- Handle the cookie consent popup

### End-to-End Tests

- Register a new user
- Complete the account registration form
- Verify successful account creation
- Verify the created user is logged in
- Log out
- Log in using the newly created account
- Verify the correct user is logged in
- Delete the user account
- Verify successful account deletion

### API GET Tests

- Retrieve all products
- Verify that the product list is not empty
- Validate the structure of each product
- Retrieve all brands
- Verify that the brand list is not empty
- Validate the structure of each brand
- Retrieve user details by email
- Validate returned user information
- Test query parameters

### API POST Tests

- Search for products
- Verify relevant products are returned
- Search using multiple test values
- Verify missing search parameters
- Create a user account
- Verify successful account creation
- Verify valid user credentials
- Verify invalid user credentials
- Verify missing login parameters
- Verify unsupported POST methods

### API PUT Tests

- Verify unsupported PUT requests
- Validate the logical response code
- Validate the error message

### API DELETE Tests

- Delete a user account
- Verify successful account deletion
- Verify a deleted user can no longer log in
- Verify unsupported DELETE requests
- Automatically delete generated test users during cleanup

### Hybrid API and UI Tests

- Create a user through the API
- Log in with the same user through the UI
- Verify the correct user is displayed in the browser
- Verify authenticated navigation options
- Delete the user through the API after the test

### Network Tests

- Monitor first-party browser requests
- Monitor first-party browser responses
- Monitor failed browser requests
- Verify the `GET /products` navigation request
- Verify the Products response status
- Capture the login request sent by the UI
- Validate the email sent by the login form
- Validate the password sent by the login form
- Verify the login response
- Detect failed critical requests

### API Mocking Tests

- Mock the Products API response
- Return controlled product data
- Verify mocked products
- Simulate an HTTP 500 server error
- Validate a simulated error response
- Return different responses based on request data
- Capture search parameters from an intercepted request
- Block image requests
- Verify that the Products page remains usable without images

### Cross-Browser Tests

The smoke test suite runs on:

- Chromium
- Firefox
- WebKit

## Project Structure

```text
python-playwright-hybrid-automation-framework/
│
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
│
├── api/
│   ├── __init__.py
│   ├── api_client.py
│   ├── endpoints.py
│   └── user_payloads.py
│
├── mocks/
│   ├── __init__.py
│   └── product_responses.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   ├── product_details_page.py
│   ├── cart_page.py
│   ├── contact_page.py
│   ├── account_created_page.py
│   └── account_deleted_page.py
│
├── tests/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── test_catalog_api.py
│   │   ├── test_method_validation_api.py
│   │   ├── test_search_api.py
│   │   └── test_user_api.py
│   │
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api_ui_authentication.py
│   │
│   ├── mocking/
│   │   ├── __init__.py
│   │   └── test_api_mocking.py
│   │
│   ├── network/
│   │   ├── __init__.py
│   │   └── test_browser_network.py
│   │
│   ├── __init__.py
│   ├── test_home_page.py
│   ├── test_login.py
│   ├── test_navigation.py
│   ├── test_products.py
│   └── test_user_lifecycle.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── network_recorder.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## BasePage

The project uses a `BasePage` class to store shared browser functionality.

`BasePage` contains:

- Base application URL
- Shared Playwright Page object
- Page navigation helper method
- Environment-based configuration
- Default timeout configuration
- Cookie consent handling

This reduces duplicated code inside page classes and makes the framework easier to maintain.

## Page Objects

The project uses Page Object Model to keep page locators and browser actions organized.

Page objects include:

- `HomePage`
- `LoginPage`
- `SignupPage`
- `ProductsPage`
- `ProductDetailsPage`
- `CartPage`
- `ContactPage`
- `AccountCreatedPage`
- `AccountDeletedPage`

The page objects contain:

- Page locators
- Navigation actions
- Form actions
- Login actions
- Signup actions
- Product actions
- Account actions

This keeps the test files cleaner because test scenarios are separated from page implementation details.

## API Client

The project uses a reusable `ApiClient` class for API requests.

`ApiClient` contains:

- Base API URL
- Reusable Requests session
- GET helper method
- POST helper method
- PUT helper method
- DELETE helper method
- Query parameter support
- Form data support
- JSON request support
- Configurable API timeout
- JSON response parsing
- Invalid JSON response handling

This reduces duplicated request code inside API tests and makes the tests easier to read and maintain.

## API Endpoints

The project uses an `ApiEndpoints` class to store API endpoint paths.

The endpoint constants include:

- Products list
- Brands list
- Product search
- Verify login
- Create account
- Update account
- Delete account
- Get user details

This separates API paths from test logic.

## User Payloads

The project uses reusable payload helper methods to prepare user data for API requests.

The payload helpers contain:

- Account creation payload
- Login credentials payload
- Conversion from internal Faker data to API parameter names

This keeps request data organized and prevents duplicated payload construction.

## Fixtures

The project uses PyTest fixtures from `conftest.py`.

The fixtures provide:

- Faker instance
- Generated test users
- Page objects
- Reusable API client
- API-created test users
- Automatic API cleanup
- Cross-browser support
- Parallel worker-safe user data

The `api_registered_user` fixture creates a user through the API before a test and deletes the same user after the test.

This makes tests independent and prevents test accounts from remaining in the application.

## Test Data

The project uses Faker to generate unique test data.

Generated test data includes:

- First name
- Last name
- Full name
- Email
- Password
- Company
- Address
- State
- City
- Zip code
- Mobile number

When tests run in parallel, the PyTest worker ID is included in the generated email address.

This reduces the risk of duplicate users and separates test data from test logic.

## Network Recorder

The project uses a reusable `NetworkRecorder` class to capture browser network activity.

`NetworkRecorder` stores:

- Request method
- Request URL
- Resource type
- Navigation request status
- Response status code
- Failed request details

The recorder filters first-party requests from the Automation Exercise domain.

This allows tests to validate browser traffic without including unrelated advertising or analytics requests.

## API Mocking

The project uses Playwright routing to intercept and control browser requests.

The mocking tests use:

- `page.route()`
- `route.fulfill()`
- `route.abort()`
- `route.continue_()`

Mocking is used to:

- Replace real API responses
- Return controlled products
- Simulate server errors
- Return responses based on request parameters
- Block image requests

This makes it possible to test scenarios that may be difficult to reproduce using the real application.

## Environment Configuration

The project uses environment variables to store configuration.

The `.env.example` file contains:

```env
BASE_URL=https://automationexercise.com
DEFAULT_TIMEOUT=60000
API_BASE_URL=https://automationexercise.com/api
API_TIMEOUT=30
```

The local `.env` file is excluded from Git.

## PyTest Markers

The project uses markers to organize test execution.

Available markers:

- `smoke`
- `regression`
- `ui`
- `api`
- `integration`
- `network`
- `mocking`
- `e2e`

Examples:

Run Smoke tests:

```powershell
pytest -m smoke -v
```

Run API tests:

```powershell
pytest -m api -v
```

Run UI tests:

```powershell
pytest -m ui --browser chromium -v
```

Run tests without the E2E scenario:

```powershell
pytest -m "regression and not e2e" --browser chromium -v
```

## Reports and Failure Artifacts

The project generates an HTML test report:

```text
reports/test-report.html
```

For failed browser tests, Playwright generates:

- Full-page screenshot
- Playwright trace
- Browser action details
- Page state information
- Network information

The Playwright trace can be opened using:

```powershell
playwright show-trace "test-results/path-to-test/trace.zip"
```

Generated reports and test artifacts are excluded from Git.

## Cross-Browser Testing

The framework supports:

- Chromium
- Firefox
- WebKit

Run the cross-browser Smoke suite:

```powershell
pytest -m smoke --browser chromium --browser firefox --browser webkit -n 0 -v
```

## Parallel Test Execution

The project uses `pytest-xdist` for parallel execution.

Run the Chromium test suite using two workers:

```powershell
pytest --browser chromium -n 2 -v
```

Serial execution can be used for debugging:

```powershell
pytest --browser chromium -n 0 -v
```

## GitHub Actions

The project includes a GitHub Actions CI pipeline.

The pipeline runs:

- Full regression in Chromium
- Smoke tests in Chromium
- Smoke tests in Firefox
- Smoke tests in WebKit

The workflow also uploads:

- HTML test report
- Screenshots from failed tests
- Playwright traces
- Test result artifacts

The workflow is triggered by:

- Push to the `main` branch
- Pull request to the `main` branch
- Manual execution

## How to Run the Tests

### 1. Clone the repository

```powershell
git clone https://github.com/encristian/python-playwright-hybrid-automation-framework.git
```

### 2. Open the project folder

```powershell
cd python-playwright-hybrid-automation-framework
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Install Playwright browsers

```powershell
python -m playwright install
```

### 7. Create the local environment file

Copy `.env.example` and rename the copy to:

```text
.env
```

### 8. Run the complete Chromium test suite

```powershell
pytest --browser chromium -n 0 -v
```

### 9. Run the cross-browser Smoke suite

```powershell
pytest -m smoke --browser chromium --browser firefox --browser webkit -n 0 -v
```

## Test Status

```text
Chromium Regression: 36 Passed
Cross-Browser Smoke Suite: 7 Passed
```

The project currently contains:

- 12 UI test executions
- 16 API test executions
- 1 integration test execution
- 3 network test executions
- 4 mocking test executions

Total Chromium regression:

```text
Passed: 36
```

## Known External Limitation

Automation Exercise is an external practice website.

The application may occasionally return temporary Cloudflare or HTTP 5xx errors.

Unexpected server errors are treated as failed tests and are not accepted as valid application behavior.

## What I Learned

Through this project, I practiced:

- Writing automated UI tests with Playwright
- Writing automated API tests with Requests
- Using PyTest fixtures
- Applying Page Object Model
- Testing GET, POST, PUT and DELETE requests
- Validating HTTP status codes
- Validating JSON response body data
- Validating API response structures
- Testing positive and negative scenarios
- Testing query parameters
- Testing form data
- Generating unique users with Faker
- Creating reusable API helper methods
- Separating endpoint data from test logic
- Separating test data from test logic
- Using APIs for test setup and cleanup
- Combining API and UI testing
- Monitoring browser requests and responses
- Validating request payloads
- Intercepting browser requests
- Mocking API responses
- Simulating HTTP 500 errors
- Blocking browser resources
- Running tests in Chromium, Firefox and WebKit
- Running tests in parallel
- Organizing tests with PyTest markers
- Generating HTML reports
- Generating screenshots on failure
- Using Playwright Trace Viewer
- Creating a GitHub Actions pipeline
- Uploading test artifacts in CI
- Using Git commits
- Structuring a professional QA Automation portfolio project

## Author

Created as part of my QA Automation portfolio.