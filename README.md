# Django 1주차 -hw1

-------------

## < 1주차 과제 >

**과제1 : django 에서 css 어떻게 연결하는지 구글링해서 혼자 해보기**
**과제2 : repl에 한거 좀 더 수정해서 django에서 runserver 돌린 결과물 자랑하기**

----------------

필자는 과제1 css 연동 과제부터 진행하였다. 

자세한 개념은 나중에 정리하고 간략하게 순서를 정리해 보았다. 

1. static 폴더를 만들어주고 하위에 css폴더를 만들어 준 후 style.css 파일을 만들어주자

   <img width="153" alt="image-20200409203029419" src="https://user-images.githubusercontent.com/49120090/78891015-9ff24700-7aa1-11ea-96c4-6ae350bbc51a.png">

2. Setting.py 변경~~

   <img width="372" alt="image-20200409203127732" src="https://user-images.githubusercontent.com/49120090/78891030-aa144580-7aa1-11ea-9e3e-710688db561b.png">

   맨 밑에 추가해주자

3. html파일 안에 정적 파일의 경로에 있는 모든 파일을 불러올 수 있도록 해주자.

   <img width="584" alt="image-20200409203259443" src="https://user-images.githubusercontent.com/49120090/78891038-b0a2bd00-7aa1-11ea-94c3-b97049d708fb.png">

