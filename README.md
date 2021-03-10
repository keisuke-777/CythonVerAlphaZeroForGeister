# CythonVerAlphaZeroForGeister


## Features
<!-- プロダクトが何かを簡潔に紹介する -->
<!-- プロダクトのセールスポイントや差別化などを説明 -->
ガイスターの学習をするコード．学習速度を上げたいが0から書き直すのは嫌なので，Cython+jpblib(並列化)で茶を濁す．  
tensorflowはGPU版でも動作確認済み．  
setup.pyはCythonでコンパイルするだけです．各種ライブラリは手動でインストールしてください．


## Requirement
<!-- プロダクトを動かすのに必要なライブラリなどを列挙 -->

* python 3.7.3
* Cython 0.29.21
* joblib 1.0.1
* tensorflow 2.4.1
* numpy 1.19.5


## Usage
<!-- DEMOの実行方法などのプロダクトの基本的な使い方を説明 -->

```bash
git clone https://github.com/keisuke-777/CythonVerAlphaZeroForGeister.git
cd CythonVerAlphaZeroForGeister
python setup.py build_ext --inplace
python train_cycle.py
```

## Note
<!-- 注意点などがあれば記載 -->
python3.6以前では恐らく動作しません．