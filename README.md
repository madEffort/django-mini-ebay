<h1 align="center">
  <br>
  <a href="https://github.com/madEffort/django-mini-ebay.git"><img src="" alt="MiniEbay" width="200">작업 중</a>
  <br>
  MiniEbay
  <br>
</h1>

<h4 align="center">
A simple <a href="https://www.starbucks.com/">Starbucks</a> app for quick product selection, cart management, and payment.</h4>

<p align="center">
<a href="https://github.com/madEffort/django-mini-ebay/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-v3.10.12-yellow"></a>
<a href="https://hits.seeyoufarm.com"><img src=""/></a>
<a href="https://github.com/madEffort/django-mini-ebay.git"><img src="https://img.shields.io/badge/PRs-welcome-green"></a>
<a href="https://www.paypal.me/madEffort"><img src="https://img.shields.io/badge/$-donate-ff69b4"></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> • <a href="#how-to-use">How To Use</a> • <a href="#download">Download</a> • <a href="#credits">Credits</a> • <a href="#related">Related</a> • <a href="#support">Support</a> • <a href="#license">License</a>
</p>


## Key Features

**2024/04/15 - 현재 구현된 기능**

- 유저 관련 기능
  - 회원 가입, 탈퇴
  - 로그인, 회원 정보 수정
- 구매자 기능
  - 판매 중인 물건 구매
- 판매자 기능
  - 판매할 물건 등록, 삭제, 수정
- 구매 이력 조회
- 장바구니 기능


pip 사용자의 경우
```bash
# Clone this repository
$ git clone https://github.com/madEffort/django-mini-ebay.git

# Go into the repository
$ cd django-mini-ebay

# Install dependencies
$ pip install
```
슈퍼유저 생성후 카테고리를 추가하고 상품 추가해줘야 합니다.

슈퍼유저 생성시 이메일은 **필수**로 입력하여야 합니다.



## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/madEffort/django-mini-ebay.git

# Go into the repository
$ cd django-mini-ebay

# Install dependencies
$ poetry install
```


After setting up the database and templates, please use the `makemigrations`, `migrate` and `collectstatic` commands.

```bash
# Run the app
$ python manage.py runserver
```

## Download



## Credits

This software uses the following open source packages:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Related

- [YouTube Data API v3](https://developers.google.com/youtube/v3)

## Support

<a href="https://www.paypal.com/paypalme/madEffort">
<img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" alt="Donate with PayPal" width="200">
</a>


## License

This project adheres to the Apache-2.0 license, and you can find more detailed information in the [LICENSE](https://github.com/madEffort/django-mini-ebay/blob/main/LICENSE)

---

> GitHub [@madEffort](https://github.com/madEffort) &nbsp;&middot;&nbsp;
> Naver [@madEffort](https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjky&x_csa=%7B%22fromUi%22%3A%22kb%22%7D&pkid=1&os=32229226&qvt=0&query=%EA%B9%80%ED%98%84%EC%9A%B0)
