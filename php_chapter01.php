<?php
public class Chapter01 {
    define(ONE_WEEK_IN_SECONDS, 7 * 86400);
    define(VOTE_SCORE, 432);
    define(ARTICLES_PER_PAGE, 25);

    public function articleVote($redis, $user, $article)
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
}