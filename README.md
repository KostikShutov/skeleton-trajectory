# skeleton-autonomous

## Другие компоненты общей системы

[Car control](https://github.com/KostikShutov/skeleton-car)

[Webview for car control](https://github.com/KostikShutov/skeleton-webview)

## Docker

Поднять docker контейнеры

 ```bash
make d-up
 ```

Остановить docker контейнеры

```bash
make d-down
```

Перезапустить docker контейнеры

```bash
make d-restart
```

Зайти в контейнер с Python

```bash
make d-python
```

## Запуск

Поднять сервер (<http://localhost:3001>):

```bash
make generator
```

Запустить обучение нейронной сети:

```bash
make train
```

Запустить tensorboard (<http://localhost:3002>):

```bash
make tensorboard
```

Очистить папку с логами:

```bash
make clear
```

Запустить тесты:

```bash
make tests
```

## Скрипты

Сгенерировать траекторию в [model/\*/train.json](model):

```bash
python scripts/generate-trajectory.py
python scripts/generate-trajectory.py -m speed_dynamic
```

Запустить симуляцию траектории из [model/\*/\*.json](model):

```bash
python scripts/simulate-trajectory.py
python scripts/simulate-trajectory.py -m speed_dynamic -f squa-2
```
