const links = document.querySelectorAll(".nav-link");

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
  const offsetTop = document.querySelector("#pres").offsetTop;
  scroll({
    top: offsetTop,
    behavior: "smooth",
  });
});

hireButton.addEventListener("click", function () {
  const offsetTop = document.querySelector("#dowload").offsetTop;
  scroll({
    top: offsetTop,
    behavior: "smooth",
  });
});
