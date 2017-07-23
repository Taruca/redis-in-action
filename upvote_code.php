<?php
# <start id="upvote-code"/>
define(ONE_WEEK_IN_SECONDS, 7 * 86400);				#A
define(VOTE_SCORE, 432);							#A

function article_vote($conn, $user, $article)
{
	$cutoff = time() = ONE_WEEK_IN_SECONDS;			#B
	if ($conn->zscore('time:', $article) < $cutoff) {
		return;
	}
}
def article_vote(conn, user, article):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS      #B
    if conn.zscore('time:', article) < cutoff:      #C
        return

    article_id = article.partition(':')[-1]         #D
    if conn.sadd('voted:' + article_id, user):      #E
        conn.zincrby('score:', article, VOTE_SCORE) #E
        conn.hincrby(article, 'votes', 1)           #E
# <end id="upvote-code"/>
#A Prepare our constants
#B Calculate the cutoff time for voting
#C Check to see if the article can still be voted on (we could use the article HASH here, but scores are returned as floats so we don't have to cast it)
#D Get the id portion from the article:id identifier
#E If the user hasn't voted for this article before, increment the article score and vote count (note that our HINCRBY and ZINCRBY calls should be in a Redis transaction, but we don't introduce them until chapter 3 and 4, so ignore that for now)
#END