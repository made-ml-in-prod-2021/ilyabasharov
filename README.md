##  Homework 04
Assignments for "ML in production" course by Mail.ru group

### Project structure

```
├── kubernetes <- pods for kubernetes
│
└── README.md <- this file you are reading right now
```

### Installation

I was playing with kubernetes locally using (kind)[https://kind.sigs.k8s.io/docs/user/quick-start/] and (kubectl)[https://kubernetes.io/docs/tasks/tools/] and (Lens)[https://k8slens.dev]. After downloading follow these steps:

#### Create the server locally

```bash
# Create cluster with name made
kind create cluster --name made

# Check if it works
kubectl cluster-info --context kind-made
```

#### Push pods to the server

```bash
# Task 2: online-inference-pod
kubectl apply -f kubernetes/online-inference-pod.yaml

#Task 2a: online-inference-pod-resources
kubectl apply -f kubernetes/online-inference-pod-resources.yaml

#Task 3: liveness и readiness
kubectl apply -f kubernetes/online-inference-pod-probes.yaml

#Task 4: replicaset
kubectl apply -f kubernetes/online-inference-replicaset.yaml
```

To see what happend online, enable port forwarding:

```bash
kubectl port-forward pod/online-inference 8000:8000
```

#### Answers

1. Task 2a: Зачем нужны ресурсы? Чтобы контролировать путем ограничения входные мощности приложение. Это поможет эффективнее пользоваться памятью и другими ресурсами между приложениями
2. Task 3: Описание работы liveness и readiness при "падении" программы. Вход: развертывание приложения в течение 40 сек, загрузка моделей 1 сек, работа приложения 30 сек, падение с ошибкой. Тогда readiness падает в течение 1 сек, далее все норм, потом опять все падает (liveness). Тем самым мы эмулируем загрузку моделей, когда кластер не готов принимать сообщения, но находится в режиме `ready`. Мы фиксируем этот момент с помощью readiness. Далее эмулируем падение программы с помощью liveness.
3. Task 3: ReplicaSet и его изменение. ReplicaSet поддерживает фиксированное кол-во нодов, если что то удалим, то он сам добавит новые, если что то добавим, он удалит старые. Новые ноды будут с новыми образами.

#### Review

Всего :one::eight:
