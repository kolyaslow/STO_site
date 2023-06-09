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

let availableKeywords = [
  "Ремонт АКПП",
  "Ремонт турбин",
  "Ремонт кондиционера",
  "Ремонт двигателя",
  "Ремонт ходовой",
  "Ремонт выхлопной системы",
  "Ремонт топливной системы",
  "Ремонт тормозной системы",
  "Ремонт подвески",
  "Замена сцепления",
  "Замена ГРМ",
  "Замена масла в МКПП",
  "Диагностика",
  "Техническое обслуживание",
  "Слесарный ремонт",
  "Промывка топливной системы",
  "Развал-схождение",
  "Хранение шин",
  "Шиномонтаж",
  "Диагностика ходовой",
];

const resultBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");

inputBox.onkeyup = function () {
  let result = [];
  let input = inputBox.value;
  if (input.length) {
    result = availableKeywords.filter((keyword) => {
      return keyword.toLowerCase().includes(input.toLowerCase());
    });
    display(result);
    if (!result.length) {
      resultBox.innerHTML = "";
    }
  }
};

function display(result) {
  const content = result.map((list) => {
    return "<li onclick=selectInput(this)>" + list + "</li>";
  });
  resultBox.innerHTML = "<ul>" + content.join("") + "</li>";
}

function selectInput(list) {
  inputBox.value = list.innerHTML;
  resultBox.innerHTML = "";
}


