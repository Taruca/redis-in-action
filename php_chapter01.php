<?php

class Chapter01 {
    const ONE_WEEK_IN_SECONDS =  604800;
    const VOTE_SCORE = 432;
    const ARTICLES_PER_PAGE = 25;

    public function voteArticle($redis, $user, $article)
    {
        $cut_off = time() - ONE_WEEK_IN_SECONDS;
        if ($redis->zScore('time:', $article) < $cut_off) {
            return;
        }

        $article_id = explode(':', $article)[0];
        if ($redis->sAdd('vote:' . $article_id, $user)) {
            $redis->zIncrBy('score:', VOTE_SCORE, $article);
            $redis->hIncryBy($article, 'votes', 1);
        }
    }

    public function postArticle($redis, $user, $title, $link)
    {
        $articleId = $redis->incr('article:');

        $voted = 'voted:' + $articleId;
        $redis->sAdd($voted, $user);
        $redis->setTimeout($voted, ONE_WEEK_IN_SECONDS);

        $now = time();
        $atricle = 'article:' . $articleId;
        $redis->hMSet($atricle, array([
            'title' => $title,
            'link' => $link,
            'poster' => $user,
            'time' => $now,
            'votes' => 1
            ]));
        $redis->zAdd('score:', $now + VOTE_SCORE, $article);
        $redis->zAdd('time:', $now, $article);
        return $articleId;
    }
}
