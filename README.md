##batteryノード
[![test](https://github.com/HIRO20040/ros/actions/workflows/test.yml/badge.svg)](https://github.com/HIRO20040/ros/actions/workflows/test.yml)

## 概要
- このリポジトリはRos2のパッケージを利用している。

## 必要なソフトウェア
- Python
 - テスト済みバージョン: 3.7~3.10

## ノードの説明
- バッテリー残量をトピックにのせるもので、数字が100から1秒に1ずつ減っていくようになっている。実際のバッテリー残量ではないので注意。

## 実行方法
- 1つのターミナルで以下を実行
```
 git clone git@github.com:HIRO20040/ros.git
```
``` 
 cd ros
```
```
 ros2 run mypkg battery
```

- 別のターミナルで以下を実行
```
 ros2 topic echo /battery
```

## 出力
- ros2 topic echo /batteryを打ったターミナルの方に以下が出力される

data: 100
data: 99
data: 98
...

## テスト環境
- Ubuntu 24.04 LTS









- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

- © 2025 Hiroaki Ohmatsu

