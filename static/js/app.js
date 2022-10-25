const coment = document.getElementById("delle");

console.log("js working");
coment.addEventListener("click", () => {
  console.log("click");
  userId = coment.dataset.id;
  action = coment.dataset.action;
  console.log("userId:", userId, "action", action);
});
