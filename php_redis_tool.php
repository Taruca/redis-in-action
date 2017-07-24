<?php
function redisConnect()
{
	$redis = new Redis();
	return $redis->connect('127.0.0.1', 6370);
}

function redisDisConnect($redis)
{
	$redis->close();
}