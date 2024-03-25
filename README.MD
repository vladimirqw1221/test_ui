## Полный пример проекта запуска тестов с генерацией allure отчетов, непрерывной интеграции и запуска через телеграм бота в любой момент, когда требуется пройти тесты

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



<div style="width:200px; height:300px;">

  ![](https://lh3.googleusercontent.com/drive-viewer/AKGpihY82WKIC4fLY2jytIINNNFMPZlnExgu5DOhqOYDXz5UdMVc4ghv7p9X5ol0tIBt8I7Q5w5XFsq9S1LaLNEvn6CA2esQXQ=s1600)
</div>

- Enter password

<div style="width:200px; height:300px;">

  ![](https://lh3.googleusercontent.com/drive-viewer/AKGpihbBbuTqfInuAmLn_8wj35z4nAqo4sFltScD47OjL0j-nphWDZl7fJxPQrRvPTNyERuRXcGyFGUbQQWFcA_mQhHMUKZZhw=s1600)
</div>
<br>

- Tap on button [Запустить тесты]

- Navigate to allure report

<br>

<div style="width:200px; height:300px;">

  ![](https://lh3.googleusercontent.com/drive-viewer/AKGpihZISfrh7aHfm6qr0f3SFrboA8tszyMfjYToSzhwiei8mL8I6Z6dJNJ5DbfN7V-lPDj6eX8aSCJpgoQ5WNMNFWgcDUS1CA=s2560)

</div>


