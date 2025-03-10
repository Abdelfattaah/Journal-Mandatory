### Overview

The Journal Mandatory Fields module enhances the accounting functionality by enforcing mandatory analytic account and partner assignments on specific accounts. This ensures consistent and accurate financial records while allowing authorized users to bypass these validations.

### Demo

A 40-second demo video of the functionality is available here:  
[![Watch the demo](https://img.youtube.com/vi/a5jQw5OCzU4/0.jpg)](https://youtu.be/a5jQw5OCzU4)

---

### Features

- Adds new fields to the Chart of Accounts to specify mandatory requirements:
  - Mandatory Analytic Account: Enforces selecting an analytic account.
  - Mandatory Partner: Enforces selecting a partner.
  - Bypass Users: Allows specifying users who can bypass the mandatory validations.
- Validates Journal Items during creation and prevents posting if:
  - An analytic account is mandatory but not selected.
  - A partner is mandatory but not selected.
- Displays clear and user-friendly error messages when validations fail.

---

### Usage

1. Go to Accounting > Configuration > Chart of Accounts.
2. Open or create an account and configure:
   - Mandatory Analytic Account
   - Mandatory Partner
   - Bypass Users (optional)
3. Create or edit a Journal Entry and assign the configured account.
4. Try posting the journal entry and observe the validation behavior.

---

### Example Scenarios

- If the Consulting Expenses account requires both an analytic account and a partner:
  - Failing to specify either will trigger a validation error.
  - Authorized users listed as bypass users can skip the validation.

---

### Technical Details

**Models:**
- Extends `account.account` to add mandatory fields.
- Extends `account.move.line` to enforce validation.

**Views:**
- Inherits the account form view to add configuration fields.

