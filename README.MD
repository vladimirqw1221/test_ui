# Example Test

---

## Test Site
Open the test site [test site](https://www.saucedemo.com/)

**added .env file or using login and password in webpage**

![test_site](https://linuxhint.com/wp-content/uploads/2023/02/d-articles-selenium-sendkeys-login-png.png)

---

# Local Run Test

```bash
mkdir ./app

git clone https://github.com/vladimirqw1221/test_ui.git

cd ./app

pip3 install -r requrements.txt

pytest

```
> If need ui report. Run test from allure serve, using
> command
```bash
pytest --alluredir allure-resulte

allure serve allure-resulte/
```

