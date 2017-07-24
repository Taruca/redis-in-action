<?php
require 'php_redis_tool.php';

$redis = "";
$redis = redisConnect();

$chapter = new FOO\Chapter01();
$articleId = $chapter->postArticle($redis, 'liu', 'title', 'www.baidu.com');
echo "We posted a new article with id: $articleId";
echo "<br>";