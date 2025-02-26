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
    git clone https://github.com/sergeeximius/csp-demo.git
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

## Параметры Content Security Policy (CSP)

В проекте используется заголовок  `Content-Security-Policy-Report-Only`  с такими параметрами:
```nginx
add_header Content-Security-Policy-Report-Only "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; report-uri /csp-violation-report-endpoint";
```

### Что это значит?

1.  **`Content-Security-Policy-Report-Only`**:
    
    -   Это режим CSP, при котором политика безопасности  **не блокирует**  нарушающие ресурсы, но отправляет отчеты о нарушениях на указанный эндпоинт.
        
    -   Используется для тестирования и отладки CSP перед его полным внедрением.
        
2.  **`default-src 'self'`**:
    
    -   Указывает, что по умолчанию все ресурсы (скрипты, стили, изображения и т.д.) могут загружаться только с того же домена (`'self'`), на котором находится сайт.
        
    -   Например, если на странице есть  `<img src="https://example.com/image.png">`, браузер заблокирует загрузку этого изображения, так как оно загружается с внешнего домена.
        
3.  **`script-src 'self'`**:
    
    -   Разрешает загрузку и выполнение JavaScript-кода только с того же домена (`'self'`).
        
    -   Например,  `<script src="/js/script.js"></script>`  будет разрешен, а  `<script src="https://malicious-site.com/evil.js"></script>`  — заблокирован.
        
4.  **`style-src 'self'`**:
    
    -   Разрешает загрузку CSS-стилей только с того же домена (`'self'`).
        
    -   Например,  `<link rel="stylesheet" href="/css/style.css">`  будет разрешен, а  `<link rel="stylesheet" href="https://external-site.com/style.css">`  — заблокирован.
        
5.  **`img-src 'self'`**:
    
    -   Разрешает загрузку изображений только с того же домена (`'self'`).
        
    -   Например,  `<img src="/images/logo.png">`  будет разрешен, а  `<img src="https://external-site.com/image.jpg">`  — заблокирован.
        
6.  **`report-uri /csp-violation-report-endpoint`**:
    
    -   Указывает URL, на который браузер будет отправлять отчеты о нарушениях CSP.
        
    -   Отчеты отправляются в формате JSON и содержат информацию о заблокированных ресурсах.
