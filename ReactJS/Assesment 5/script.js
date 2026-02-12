const form = document.getElementById("myForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const submitBtn = document.getElementById("submitBtn");
const togglePassword = document.getElementById("togglePassword");
const strengthBar = document.getElementById("strength-bar");
const successMsg = document.getElementById("successMsg");

// ---------- Utility functions ----------
function showError(input, message) {
  const error = input.parentElement.querySelector(".error");
  error.innerText = message;
  error.style.display = "block";
}

function hideError(input) {
  const error = input.parentElement.querySelector(".error");
  error.style.display = "none";
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function passwordStrong(password) {
  let strength = 0;
  if (password.length >= 6) strength++;
  if (/[A-Z]/.test(password)) strength++;
  if (/[0-9]/.test(password)) strength++;

  strengthBar.style.width = (strength / 3) * 100 + "%";
  strengthBar.style.background =
    strength === 1 ? "red" : strength === 2 ? "orange" : "green";

  return strength === 3;
}

function checkFormValid() {
  submitBtn.disabled = !(
    nameInput.value &&
    isValidEmail(emailInput.value) &&
    passwordStrong(passwordInput.value)
  );
}

// ---------- Events ----------
nameInput.addEventListener("blur", () => {
  nameInput.value === ""
    ? showError(nameInput, "Name is required")
    : hideError(nameInput);
  checkFormValid();
});

emailInput.addEventListener("input", () => {
  !isValidEmail(emailInput.value)
    ? showError(emailInput, "Invalid email")
    : hideError(emailInput);
  checkFormValid();
});

passwordInput.addEventListener("input", () => {
  passwordStrong(passwordInput.value)
    ? hideError(passwordInput)
    : showError(passwordInput, "Password must be strong");
  checkFormValid();
});

// Show / hide password
togglePassword.addEventListener("click", () => {
  passwordInput.type =
    passwordInput.type === "password" ? "text" : "password";
});

// ---------- REGISTRATION LOGIC ----------
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const user = {
    name: nameInput.value,
    email: emailInput.value,
    password: passwordInput.value
  };

  // Save user (registration success)
  localStorage.setItem("registeredUser", JSON.stringify(user));

  successMsg.innerText = "✅ Registration successful!";
  successMsg.style.color = "#00ffcc";

  form.reset();
  strengthBar.style.width = "0%";
  submitBtn.disabled = true;
});
