<?php
/**
 *
 * 简单队列
 */

$redis = new Redis();
$redis->connect('127.0.0.1');

//入队
$userId = mt_rand(000000, 999999);
$redis->rpush('QUEUE_NAME', json_encode['user_id' => $user_id]);
$userId = mt_rand(000000, 999999);
$redis->rpush('QUEUE_NAME', json_encode['user_id' => $user_id]);
$userId = mt_rand(000000, 999999);
$redis->rpush('QUEUE_NAME', json_encode['user_id' => $user_id]);
echo "入队成功 \n";

//查看队列
$res = $redis->lrange('QUEUE_NAME', 0, -1);
echo "当前队列数据为： \n";
print_r($res);

echo "______________________ \n";

//出队
$redis->lpop('QUEUE_NAME');
echo "出队成功 \n";

//查看队列
$res = $redis->lrange('QUEUE_NAME', 0, -1);
echo "当前队列数据为： \n";
print_r($res);