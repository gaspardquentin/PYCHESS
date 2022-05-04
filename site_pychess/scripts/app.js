const links = document.querySelectorAll(".nav-link");
const workButton = document.getElementById("my-work-btn");
const hireButton = document.getElementById("hire-me-btn");

for (const link of links) {
  link.addEventListener("click", clickHandler);
}

function clickHandler(e) {
  e.preventDefault();
  const href = this.getAttribute("href");
  const offsetTop = document.querySelector(href).offsetTop;

  scroll({
    top: offsetTop,
    behavior: "smooth",
  });
}

workButton.addEventListener("click", function () {
  const offsetTop = document.querySelector("#projects").offsetTop;
  scroll({
    top: offsetTop,
    behavior: "smooth",
  });
});

hireButton.addEventListener("click", function () {
  const offsetTop = document.querySelector("#contact").offsetTop;
  scroll({
    top: offsetTop,
    behavior: "smooth",
  });
});
