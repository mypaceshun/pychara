.. pychara documentation master file, created by
   sphinx-quickstart on Fri Apr  5 17:27:53 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pychara's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   changelog.rst
   pychara.rst

pycharaは某兄さんへのスクレイピングを補助するツールです。

インストール
------------------------------------

pipコマンドを利用してインストールします。

   $ pip install pychara


クイックスタート
------------------------------------

ログイン処理のみを行う簡単なサンプルは以下の通りです ::

   >>> from pychara.session import Session
   >>> s = Session()
   >>> s.login('username', 'password')
   'username'

`status` 関数を利用することでログイン済みかどうかを確認出来ます。 ::

   >>> s.status()
   'login'


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
