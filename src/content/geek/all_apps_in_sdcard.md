title: Все программы на SD Card.
date: 2013-12-24
type: blog
tags: [Android]

На моем довольно старом Андроиде вечно не хватает места для установки программ, а некоторые программы нельзя перенести на SD Card. Но выход есть, нужно сказать дройду что бы он ставил все на SD Card, и собственно переносить все программы на карту, и устанавливать новые туда же.

Сначала нужно подружить дройд с маком по USB. В настройках дройда идите в Настройки > приложения > Разработка > Отладка через USB

Далее в Mac

В своем `.profile` файлике впишите следующую строчку: 

	export PATH=${PATH}:/path_to_android-sdk-mac_86/platform-tools

Потом подключаем дройд к маку в режиме *только зарядка* и в терминале

	adb shell
	pm setInstallLocation 2
	exit

И все. Все программы будут доступны для переноса на SDCard