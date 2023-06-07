window.addEventListener("load", () => {
  const left = document.querySelector(".btn-left");
  const rigth = document.querySelector(".btn-rigth");

  const slider = document.querySelector(".contBig");
  const div = document.querySelectorAll(".toCont");

  let counter = 0;
  const stepSize = div[0].clientWidth;

  slider.style.tranform = "translateX(" + `${-stepSize * counter}px)`;

  rigth.addEventListener("click", () => {
    if (counter >= div.length - 1) counter = -1;
    slider.classList.add("transfornAnimation");
    counter++;
    slider.style.transform = "translateX(" + `${-stepSize * counter}px)`;
  });

  left.addEventListener("click", () => {
    if (counter <= 0) counter = div.length;
    slider.classList.add("transfornAnimation");
    counter--;
    slider.style.transform = "translateX(" + `${-stepSize * counter}px)`;
  });
});
