class BlogPost:
    author_name = ""
    title = ""
    text  = ""
    publication_date = ""

lorem_ipsum = BlogPost()
lorem_ipsum.author_name = "John Doe"
lorem_ipsum.title = "Lorem Ipsum"
lorem_ipsum.text = "Lorem ipsum dolor sit amet."
lorem_ipsum.publication_date = "2000.05.04."

wait_but = BlogPost()
wait_but.author_name = "Tim Urban"
wait_but.title = "Wait but why"
wait_but.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
wait_but.publication_date = "2010.10.10."

engineer = BlogPost()
engineer.author_name = "William Turton"
engineer.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
engineer.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn't want to be the center of attention. When I asked to take his picture outside one of IBM's New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
engineer.publication_date = "2017.03.28."

print(engineer.text)