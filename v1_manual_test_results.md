# Example workflow

<h4>Character Creation and Review</h4>

Five-Star Frank is a famous game character reviewer, but he has a secret: he likes to review his own original characters, and give them the highest reviews! Having heard of our database, he wants to upload his own character, DJ Heartbeats, and upload a review for it. Then, he will be able to fetch the review, show it to all of his associates, and earn the adoring praise he always knew he deserved!

Frank would go about this by:

- first creating a new user by calling POST /user/make and passing in his username, "StarStarStarStarStar" as a parameter
- next using that user to create a character by calling POST /character/make and passing in his user_id and the name and details of DJ Heartbeats into the request body.
- then writing a review by calling POST /character/review/{char_id}, passing in his user id, character id, and his description text highlighting DJ Heartbeats unparalleled health stat.
- finally fetching all of DJ Heartbeats' reviews with GET /character/get_review/{char_id} and passing in the character id

Now, Frank can see his review for his character, and is filled with a surge of pride upon reading the review.

# Testing results
