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

## Run test on Telegram bot


- Navigate to the [bot](https://t.me/testretres_bot)
- Launch the bot by sending the /start command
- Tap on button [Запустить тесты]

![](https://lh3.googleusercontent.com/drive-viewer/AKGpihamwoK-QiOJikPcUZkcMBmmGy-4hXucMNpInzdQU6MIQUcZVfqFYu7EywMnjz4pGkk77jmkJYCYAa9S0HhBQJ9E9c4h=s2560)

