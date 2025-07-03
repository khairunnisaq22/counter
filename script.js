document.querySelectorAll(".reset-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    alert("Reset action triggered.");
    // Real logic would go here like resetting values via API
  });
});

document.querySelector(".add-btn").addEventListener("click", () => {
  alert("Add Tester Part clicked!");
  // Implement dynamic part addition logic here
});
