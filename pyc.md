Python 的程式是寫在 .py 裡，也就是說， .py 檔是 Python 的原始程式碼檔案，而 Python 會在執行 .py 檔時，將 .py 的程式碼編譯成中間程式碼檔 ( byte-compiled ) 的 .pyc 檔以加快下次執行的速度。

所以，當你執行一支 .py 檔時，Python 會先看看有沒有這支 .py 檔的 .pyc 檔，如果有，而且 .py 檔的修改時間和 .pyc 檔一樣時，Python 就會讀 .pyc 檔，否則， Python 就會去讀原來的 .py 檔。

不過，執行 .py 檔並不一定會產生出 .pyc 檔，通常是被來做 import 的 .py 檔才會產生出 .pyc 檔的。

Read more: http://www.arthurtoday.com/2010/02/python-py-pyc.html#ixzz4pMKCyUKa
