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

<div style="width:300px; height:300px;">

  ![Alt текст](https://lh3.googleusercontent.com/drive-viewer/AKGpihamwoK-QiOJikPcUZkcMBmmGy-4hXucMNpInzdQU6MIQUcZVfqFYu7EywMnjz4pGkk77jmkJYCYAa9S0HhBQJ9E9c4h=s2560)

</div>

- Navigate to allure report

<div style="width:300px; height:300px;">

  ![Alt текст](https://lh3.googleusercontent.com/drive-viewer/AKGpihZ1H7Jl_cB3QAf3VW46DI6Bt3fPueg_VtNwSmyk8Rg1xPNnuT60IaKmU_6Er6l0i2d1lV0sZqxt8Znis5pHK-yFkp4oMw=s1600)

</div>


