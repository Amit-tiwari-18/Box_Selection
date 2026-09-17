# Test Cases and Test Run Output

## 1. Automated Test Cases

The project uses Django's built-in testing framework.

### Test Case 1: Product Fits in Medium Box

**Product:** Laptop
**Dimensions:** 35 × 25 × 5 cm
**Weight:** 3 kg

**Medium Box:**

- Dimensions: 40 × 30 × 20 cm
- Maximum Weight: 10 kg

**Expected Result:** Product weight should be within the Medium Box weight limit.

**Test Result:** Passed

---

### Test Case 2: Product Exceeds Box Weight Limit

**Product:** Heavy Item
**Dimensions:** 30 × 20 × 15 cm
**Weight:** 25 kg

**Medium Box:**

- Maximum Weight: 10 kg

**Expected Result:** The product should not fit because its weight exceeds the box capacity.

**Test Result:** Passed

---

### Test Case 3: Large Product Fits in Large Box

**Product:** Large Item
**Dimensions:** 55 × 35 × 35 cm
**Weight:** 15 kg

**Large Box:**

- Dimensions: 60 × 40 × 40 cm
- Maximum Weight: 20 kg

**Expected Result:** Product weight should be within the Large Box weight limit.

**Test Result:** Passed

---

## 2. Test Run Command

The following command was used to run the automated Django tests:

```bash
python manage.py test
```

## 3. Actual Test Run Output

```text
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
Destroying test database for alias 'default'...
(venv) PS C:\Users\at389\OneDrive\Desktop\Box_Selection>
```

## 4. Test Summary

- Total automated tests: 3
- Passed: 3
- Failed: 0
- System check issues: 0

**Overall Status: All automated tests passed successfully.**
