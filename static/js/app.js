const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');

document.addEventListener('mousemove', e => {
  cursor.style.left = e.clientX + 'px';
  cursor.style.top = e.clientY + 'px';
  ring.style.left = e.clientX + 'px';
  ring.style.top = e.clientY + 'px';
});

function openModal() {
  document.getElementById('loginModal').classList.add('open');
}

function closeModal() {
  document.getElementById('loginModal').classList.remove('open');
}

function goToDashboard() {
  window.location.href = "/dashboard";
}

function goToLanding() {
  window.location.href = "/";
}

async function login() {
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const res = await fetch("/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  if (res.ok) goToDashboard();
}