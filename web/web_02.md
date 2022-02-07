# Web

## CSS Layout

	### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 **인라인 요소들이 주변을 wrapping** 하도록 함
- 요소가 Normal flow를 벗어나도록 함
- 속성
  - `none`: 기본값
  - `left`: 요소를 왼쪽으로 띄움
  - `right`: 요소를 오른쪽으로 띄움

- 예시

  ```html
  <style>
    .box1 {
      width:150px;
      height:150px;
      
    }
    .clearfix::after {
      content= "";
      display: block;
      clear: both;
    } <
  </style>
  <body>
    <header>
      <div class="boc1 left">div</div>
    </header>
    	<div class="box2">div</div>
  </body>
  ```

- Clearing Float
  - Float는 Normal Flow에서 벗어나 부동 상태
  - 따라서, 이후 요소에 대하여 Float 속성이 적용되지 않도록 Clearing이 필수적임(높이가 생김)
    - ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
      - 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용
    - clear 속성 부여

- Float 정리
  - Float는 레이아웃을 구성하기 위해 필수적으로 활용 되었으며, 최근엔 Flexbox, Grid 등장과 함께 사용도가 낮아짐
  - Float 활용 전략 - Normal Flow 에서 벗어난 레이아웃 구성
    - 원하는 요소들을 Float로 지정하여 배치
    - 부모 요소에 반드시 Clearing Float를 하여 이후 요소부터 Normal Flow를 가지도록 지정

### Flex box

- CSS Flexible Box Layout
  - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  - 축
    - `flex-direction : row;` (or `column`)
    - main axis (메인 축)
    - cross axis (교차 축)
  - 구성 요소
    - Flex Container (부모 요소)
      - flexbox 레이아웃을 형성하는 가장 기본적인 모델
      - Flex Item들이 놓여있는 영역
      - `display` 속성을 `flex` 혹은 `inline-flex`로 지정
    - Flex Item (자식 요소)
      - 컨테이너에 속해 있는 컨텐츠(박스)
  
- 속성
  
  - 배치 설정
    - flex-direction
    - flex-wrap
  
  - 공간 나누기
    - justify-content (main axis)
    - align-content (cross axis)
  
  - 정렬
    - align-items (모든 아이템을 cross axis 기준으로)
    - align-self (개별아이템)
  
- flex-direction

  - Main axis 기준 방향 설정
  - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)
    - row
    - row-reverse
    - column
    - column-reverse

- flex 속성

  - flex-direction: Main axis의 방향을 설정

  - flex-wrap

  - flex-flow

    - flex-direction + flex-wrap 한번에

    

    

    

    - flex-start
    - flex-end
    - center
    - space-between
    - space-around
    - space-evenly

  - align-content

    - Cross axis를 기준으로 공간 배분(**아이템이 한줄로 배치되는 경우 확인할 수 없음**)
      - `flex-start`
      - `flex-end`
      - `center`
      - `space-between`
      - `space-around`
      - `space-evenly`

  - `align-items`

    - 모든 아이템을 Cross axis를 기준으로 정렬
      - `stretch`
      - `flex-start`
      - `flex-end`
      - `center`
      - `baseline`

  - `align-self`

    - 개별 아이템을 Cross axis

  - `flex-grow` : 남은 영역을 아이템에 분배

  - `flex-shrink` : 영역이 부족할 때 어떻게 축소를 할지

  - `flex-basis`: item의 기본 크기 결정(default 0), auto로 설정하면 콘텐츠 길이에 따라 크기가 결정(긴 콘텐츠는 더 길게)

  - `flex: grow/shrink/basis` 로 설정할 수 있음

  - `order` : 배치순서

##  Bootstrap

### bootstrap grid system



## Responsive web

