# Ai_notes_project
Това е малък Python скрипт, който използва OpenAI API, за да разшири кратки идеи в няколко изречения.

## Как работи

1. Скриптът пита потребителя за кратка идея.
2. Изпраща идеята към OpenAI GPT модел (`gpt-4o-mini`).
3. Печата разширения отговор от AI.

## Изисквания

- Python 3.10+
- OpenAI Python SDK (v1+)
- API ключ от OpenAI

## Инструкции за ползване

1. Копирайте кода от `main.py`.
2. Сложете вашия OpenAI API ключ:
```python
client = OpenAI(api_key="YOUR_API_KEY_HERE")
