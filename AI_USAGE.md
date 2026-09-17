# AI Usage

## 1. AI Tool Used

I used ChatGPT as an AI assistance tool during the development of this assignment.

The AI was used mainly for understanding Django concepts, getting coding guidance, debugging, improving the project structure, and preparing documentation.

---

## 2. How AI Was Used

I used AI assistance for the following tasks:

- Understanding the assignment requirements
- Setting up the Django project
- Understanding Django project and app structure
- Creating Django models for Product and Box
- Creating views and URL configurations
- Creating HTML templates
- Creating CSS for the frontend
- Understanding the box recommendation logic
- Creating Django test cases
- Understanding test output
- Preparing project documentation

---

## 3. Example Prompts Used

Some of the prompts used during development included:

- "How to make this Django project?"
- "Give me the project structure."
- "How to add product and box models in Django?"
- "How to implement box recommendation?"
- "Add more products."
- "How to test the Django project?"
- "Give me full TEST_OUTPUT.md."
- "What next?"

These prompts were used to get development guidance and understand the implementation.

---

## 4. Accepted AI Output

I used AI suggestions for:

- Basic Django project structure
- Product and Box model structure
- Recommendation logic
- HTML templates
- CSS styling
- Django test cases
- README documentation structure

The generated code was added to the project and then tested locally.

---

## 5. Rejected or Modified Output

I did not blindly use every AI suggestion.

I modified the project based on my requirements and testing.

Examples of modifications included:

- Keeping the project structure simple instead of creating unnecessary separate service modules.
- Using Django templates with HTML and CSS instead of adding a separate frontend framework.
- Adding product and box data through Django Admin.
- Testing the recommendation logic with different product dimensions and weights.
- Creating actual Django tests and verifying their results through the terminal.

---

## 6. AI Mistakes / Issues Found

During development, I verified AI-generated suggestions instead of assuming that they were correct.

One issue identified during testing was that the initial Django test command reported:

```text
Found 0 test(s).
```

This showed that no actual automated tests had been created yet.

I then created tests in `boxes/tests.py` and ran the test command again.

The second test run reported:

```text
Found 3 test(s).
...
Ran 3 tests in 0.003s

OK
```

This confirmed that the tests were discovered and passed.

---

## 7. Verification Steps

I verified the project manually and through Django's testing framework.

### Manual Verification

I checked:

- Django server starts successfully.
- Home page loads.
- Product selection page works.
- Products can be managed through Django Admin.
- Boxes can be managed through Django Admin.
- Suitable boxes are recommended.
- No suitable box message is displayed when the product exceeds the available limits.

### Automated Verification

I ran:

```bash
python manage.py test
```

The final result was:

```text
Found 3 test(s).
Ran 3 tests in 0.003s

OK
```

Therefore, all three automated tests passed successfully.

---

## 8. My Responsibility

AI was used as an assistance and learning tool. I reviewed, modified, tested, and verified the implementation before including it in the project.

The final project was tested locally using Django and the application's web interface.
