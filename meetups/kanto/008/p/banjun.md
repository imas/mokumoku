# ばんじゅん🍓

## 担当

- 橘ありす
- ほか

## P業以外で普段やっていること

iOSアプリをつくっています

またべつのLinked Open Dataのメンテをちまちまと

外出自粛中

## 今日やること

PhotoStudioPlayerのメンテつづきやろうかな

## 今日の成果

https://github.com/banjun/PhotoStudioPlayer/pull/15

PhotoStudioPlayerでキャプチャしているとiPhoneの音が消える問題があるので、音もMacからスルーで再生すればよいと思った。音は出たが課題がある。

* いつも音が出ていてよいのか (windowごとのmute, volumeがほしい)
* 負荷によって音が消えたりする
* main windowのView Controllerにbindしてmute/unmuteするメニューほしい