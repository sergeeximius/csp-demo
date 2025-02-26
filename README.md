# CSP Demo: Стенд для демонстрации работы Content Security Policy (CSP)

Этот проект представляет собой демонстрационный стенд для тестирования и изучения механизма  **Content Security Policy (CSP)**.  

CSP — это важный инструмент безопасности, который помогает предотвращать атаки, такие как межсайтовый скриптинг (XSS),  инъекции данных и загрузку вредоносного контента.

## Что входит в demo стенд?

-   **Nginx**: Веб-сервер, который обслуживает тестовые HTML-страницы и отправляет заголовок  `Content-Security-Policy-Report-Only`.
    
-   **Python-приложение**: Принимает отчеты о нарушениях CSP и сохраняет их в файлы.
    
-   **Тестовые HTML-страницы**: Примеры страниц, которые генерируют нарушения CSP для демонстрации работы механизма.
    

## Как запустить стенд?

1.  Убедитесь, что у вас установлены  **Docker**  и  **Docker Compose**.
    
2.  Клонируйте репозиторий:
    ```bash    
    git clone https://github.com/ваш-репозиторий/csp-demo.git
    cd csp-demo
    ```
3.  Запустите стенд:
    ```bash
	docker-compose up -d
	```
    
4.  Откройте в браузере:
    
    -   http://csp.eximius.ru  — главная страница.
        
    -   http://csp.eximius.ru/xss.html  — пример XSS.
        
    -   http://csp.eximius.ru/inline-script.html  — пример inline-скрипта.
        

## Как сменить доменное имя?

Если вы хотите запустить проект в интернете с другим доменным именем:

1.  Откройте файл  `front/nginx.conf`.
    
2.  Замените  `csp.eximius.ru`  на ваше доменное имя:
    ```nginx
    server_name ваш-домен.ru;
    ```
	
3.  Пересоберите и запустите контейнеры:
    ```bash
	docker-compose up --build -d
    ```
    

## Запуск локально

Если вы запускаете проект локально, добавьте доменное имя в файл  `hosts`  вашей ОС:

-   **Linux/Mac**:  
    Откройте файл  `/etc/hosts`  и добавьте строку:
    ```bash
	127.0.0.1 csp.eximius.ru
    ```

-   **Windows**:  
    Откройте файл  `C:\Windows\System32\drivers\etc\hosts`  и добавьте строку:
    ```powershell
	127.0.0.1 csp.eximius.ru
    ```
    

## Где сохраняются отчеты?

Отчеты о нарушениях CSP сохраняются в каталог  `./csp-reports`  на хостовой машине.  
Каждый отчет представляет собой JSON-файл с подробной информацией о нарушении.

## Пример отчета
```json
{
  "csp-report": {
    "document-uri": "http://csp.eximius.ru/xss.html",
    "referrer": "",
    "violated-directive": "script-src 'self'",
    "effective-directive": "script-src",
    "original-policy": "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; report-uri /csp-violation-report-endpoint",
    "blocked-uri": "https://malicious-site.com/evil.js",
    "line-number": 10,
    "column-number": 5,
    "source-file": "http://csp.eximius.ru/xss.html",
    "status-code": 200,
    "script-sample": ""
  }
}
```
