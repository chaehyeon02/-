// 슬라이드 이미지들 선택자
const $slides = document.querySelectorAll(".slide");

// 현재 보이는 슬라이드 index값
let current = 0;

const reset = () => {
  $slides.forEach((slide) => {
    slide.style.display = "none";
  });
};

// 자동 슬라이드 기능
const autoSlide = () => {
  // 모든 슬라이드 이미지를 보이지 않는 상태로 설정
  reset();
  // 마지막 슬라이드 이미지라면,
  if (current === $slides.length - 1) {
    // current 값을 -1로 설정
    current = -1;
  }
  //마지막이 아니면 +1로 설정
  current++;
  $slides[current].style.display = "block";
};

setInterval(autoSlide, 5000);

// 수동 슬라이드 기능: 화살표
// 왼쪽 화살표
const $arrowLeft = document.querySelector(".arrow--left");
// 오른쪽 화살표
const $arrowRight = document.querySelector(".arrow--right");

const slideToRight = () => {
  // 모든 슬라이드 이미지 display를 none으로 리셋
  reset();
  // current(현재 보여지는 슬라이드 이미지)의 
  // 다음 슬라이드 이미지가 보이도록 스타일 변경
  if (current === $slides.length - 1) {
    current = -1;
  }
  current++;
  $slides[current].style.display = "block";
};

$arrowRight.addEventListener("click", slideToRight);

const slideToLeft = () => {
  reset();
  if (current === 0) {
    current = $slides.length;
  }
  current--;
  $slides[current].style.display = "block";
};

$arrowLeft.addEventListener("click", slideToLeft);