# Lab 1 — Basic HTTP Server

Реалізація однакового контракту маршрутизації двома стеками: Python та Node.js.

## Stack verstion
|Стек|Версія|
|-------|------|
|Python|3.14.6|
|Node.js|26.8.1|

## Структура каталогів
```
web-apps-course/
├─ lab1/
│  ├─ python/
│  │  ├─ server.py
│  │  ├─ public/
│  │  │  ├─ index.html
│  │  │  ├─ about.html
│  │  │  ├─ styles.css
│  │  │  ├─ 404.html
│  ├─ node/
│  │  ├─ server.mjs
│  │  ├─ public/
│  │  │  ├─ index.html
│  │  │  ├─ about.html
│  │  │  ├─ styles.css
│  │  │  ├─ 404.html
│  ├─ README.md
├─ README.md
├─ .gitignore
```
## Клонування репозиторію

```bash
git clone https://github.com/RizelBeri/web-apps-course
```
## Запуск

### Pyhton
```bash
cd web-apps-course/lab1/python/ 
python server.py
```
Адреса: `localhost:3002`

### Node.js
```bash
cd web-apps-course/lab1/node/ 
node server.mjs
```
Адреса: `localhost:3001`
