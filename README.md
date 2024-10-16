# Automation and Manual tests and Theoretical questions

## Directory MANUAL-TESTS

- **main_crypto_concepts.md:** the answer to the theoretical question "familiarize yourself with some main Crypto concepts, explain in a few lines each one of the concepts"
- **manual_test_cases.md:** test suite for Transaction History tab
- **bonus_manual_test_cases.md:** bonus manual task, a description of Functional Test Cases for ChainPortX & CCTP protocols

## Directory AUTOMATION-TEST-THEORETICAL-QUESTION
- **tokens-farm.md**: the answer to the question "Task 1 - TokensFarm: Find the element and write the locators you would use". If I understood correctly I do not need to write automation tests for this task but only provide xpath and css selector.

## Automation tests including both basic and automation bonus tasks

### Setup Instructions

- **clone the repository**
git clone https://github.com/Buezrello/dcentralab_home_assignment.git
- **install dependencies:**
pip install -r requirements.txt
- **run automated tests:**
pytest --alluredir=allure-results
- **view Allure report:**
allure serve allure-results

## Estimated Time Worked
- Total time worked on this assignment: 4 hours

Note: I didn't work all four hours straight, I'm in the North now and because of the war I had to go down to the bomb shelter from time to time, so because of the breaks the task actually took longer.
