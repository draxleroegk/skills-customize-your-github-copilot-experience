# 📘 Assignment: Interactive Web Forms with JavaScript

## 🎯 Objective

Learn how to build interactive HTML forms with client-side validation and dynamic user feedback using JavaScript. You'll create a form that validates input in real-time, displays error messages, and processes data without page reloads.

## 📝 Tasks

### 🛠️ Create a User Registration Form

#### Description
Build an HTML form with multiple input fields and style it with CSS. The form should include fields for email, password, and a submit button.

#### Requirements
Completed program should:

- Create an HTML form with at least 4 input fields (email, password, confirm password, age)
- Add appropriate labels for each field
- Style the form with CSS to make it visually appealing
- Include a submit button
- Display the form in a centered container with proper spacing and colors

### 🛠️ Add JavaScript Form Validation

#### Description
Write JavaScript code to validate form inputs before submission. Check for empty fields, valid email format, matching passwords, and valid age range.

#### Requirements
Completed program should:

- Validate that all fields are filled before allowing submission
- Validate that the email follows a standard email format (e.g., contains @ and .)
- Verify that password and confirm password fields match
- Check that age is a number between 13 and 120
- Display error messages below each field when validation fails
- Clear error messages when the user corrects the input
- Prevent form submission if any validation fails

### 🛠️ Show Success Message and Reset Form

#### Description
When the form passes validation, display a success message to the user and reset the form fields for another submission.

#### Requirements
Completed program should:

- Display a success message (e.g., "Registration successful!") when validation passes
- Show the success message for 3 seconds before automatically hiding it
- Clear all input fields after successful submission
- Prevent multiple rapid submissions by temporarily disabling the submit button
- Allow the user to submit the form again after success
