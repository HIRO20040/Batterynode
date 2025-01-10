## batteryノード
[![test](https://github.com/HIRO20040/batterynode/actions/workflows/test.yml/badge.svg)](https://github.com/HIRO20040/batterynode/actions/workflows/test.yml)


## 概要
- パソコンのバッテリー残量, 充電中か否か, 残り時間を取得してトピックに流す機能を持つ。バッテリー残量が20%未満になると警告がでるようになっている。


## 使い方

### 実行例

```bash
 $ ros2 run batterynode battery
```

### 出力

```bash
 $ ros2 topic echo /battery_info
 data: 'バッテリー残量: 33.0% | 充電中: いいえ | 残り時間: 72分'
 data: 'バッテリー残量: 19.0% | 充電中: いいえ | 残り時間: 40分 | 警告: バッテリー残量が20%を下回りました！'　
```

## 参考
- [Pythonでシステム情報を取得！psutilでバッテリー状態を確認する方法](https://ameblo.jp/fiender/entry-12880810651.html)
- [Markdownの書き方|Pythonマニア](https://pythonmaniac.com/markdown/)

### 使用させていただいたコンテナ
- [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)


## テスト環境
- Ubuntu 22.04 LTS
- ROS 2 Humble
- Python


## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

- © 2025 Hiroaki Ohmatsu

