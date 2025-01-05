## batteryノード
[![test](https://github.com/HIRO20040/ros/actions/workflows/test.yml/badge.svg)](https://github.com/HIRO20040/ros/actions/workflows/test.yml)

## 概要
- このリポジトリはROS 2のパッケージを利用している。

## 必要なソフトウェア
- Python


## ノードの説明
- バッテリー残量をトピックにのせるもので、数字が100から1秒に1ずつ減っていくようになっている。実際のバッテリー残量ではないので注意。

## 実行方法
- 1つのターミナルで以下を実行
```
 git clone https://github.com/HIRO20040/batterynode
```
``` 
 cd batterynode
```
```
 ros2 run batterynode battery
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
- ROS 2(Humble)









- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

- © 2025 Hiroaki Ohmatsu

