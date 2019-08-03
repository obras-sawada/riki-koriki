ja={
    "copyright":"Developed by 日曜大工",
    "title":"Mr. 黒電話",
    "subtitle":"AI画像判定",
    "select_image":"画像を選択する",
    "reselect_image":"画像を選びなおす",
    "judge":"判定する",
    "judging":"判定中...",
    "tweet":"結果をツイートする",
    "description":"AIが金正恩か黒電話かを判定します",
    "try_again":"別の画像で試す",
    "answer_description":"この画像は",
    "kim":"金正恩",
    "phone":"黒電話",
    "hashtag":"Mr.黒電話",
    "image_missing":"画像は見つかりませんでした。"
}
en={
    "copyright":"Developed by DIY (日曜大工)",
    "title":"Mr. Phone",
    "subtitle":"AI Image Recognition",
    "select_image":"Select image",
    "reselect_image":"Change image",
    "judge":"Judge",
    "judging":"Judging...",
    "tweet":"Tweet this result",
    "description":"This AI judges if it is Kim or Phone.",
    "try_again":"Try with another image",
    "answer_description":"This is ",
    "kim":"Kim Jong-un",
    "phone":"Phone",
    "hashtag":"Mr.Phone",
    "image_missing":"Image Not Found."
}


def get_textdef(language):
    if language=="ja":
        return ja
    else:
        return en