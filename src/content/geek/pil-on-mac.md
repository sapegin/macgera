title: PIL на Mac
date: 2014-02-11
tags: [PIL, Python, Mac]

Иногда сталкиваюсь с проблей `decoder JPEG not available` и всегда разные способы ее решения. На Linux все очень просто решается. На mac, как оказалось бубны, и всякое. 

Очень помогает любимый мною [brew](http://brew.sh/). Он позволяет избежать всех этих бубнов.

Что бы все было круто, сначала нужно настроить права. 

`chown myusername /usr/local/include`

`chown myusername /usr/local/lib`


Потом ставить пакеты, только не по отдельности, а разом.

`brew install graphicsmagick`
