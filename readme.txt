＊学習リセットするには下記ファイルを削除する
./model/すべて
./data/eventなんとか

＊学習実行
$ python main.py

＊学習過程をグラフ化
$ tensorboard --logdir=data

＊ローカルサーバー立ててウェブページ公開
$ python web.py

＊サーバーが立ちっぱなしで再起動できない場合
下記でweb.pyのプロセスIDを確認
$ ps -fA | grep python
下記でプロセスを殺す
$ kill プロセスID