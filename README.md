## batteryノード
[![test](https://github.com/HIRO20040/batterynode/actions/workflows/test.yml/badge.svg)](https://github.com/HIRO20040/batterynode/actions/workflows/test.yml)

## 概要
- このリポジトリはROS 2のパッケージを利用している。

## 必要なソフトウェア
- Python


## ノードの説明
- パソコンのバッテリ残量, 充電中か否か, 残り時間を取得してトピックに流す機能を持つ。


## 使い方

### 実行例

```bash
 $ ros2 run batterynode battery
```

### 出力

```bash
 $ ros2 topic echo /battery_info
 data: 'バッテリー残量: 33.0% | 充電中: いいえ | 残り時間: 72分'

```

## 参考
- [Pythonでシステム情報を取得！psutilでバッテリー状態を確認する方法](https://ameblo.jp/fiender/entry-12880810651.html)
- [Markdownの書き方|Pythonマニア](https://pythonmaniac.com/markdown/)



## テスト環境
- Ubuntu 20.04 LTS
- ROS 2 Humble



## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

- © 2025 Hiroaki Ohmatsu

