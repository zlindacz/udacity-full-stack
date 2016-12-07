########################################################################
# Project 1: Movie Trailer Website
# Date Completed: 12/6/2016
# Submitted by: Linda Zhang
########################################################################

###################### entertainment_center file #######################
# This module uses the class Movie defined in media.py to create
# Movie instances. It also requires the fresh_tomatoes module for
# its open_movies_page function to create the HTML page that will
# display these movie instances
########################################################################

import media
import fresh_tomatoes

the_machinist = media.Movie(
        "The Machinist",
        "An insomniac machinist starts to question his sanity",
        "R",
        "https://goo.gl/0RAxiP",
        "https://www.youtube.com/watch?v=H0fuHY4U1UA")

predestination = media.Movie(
        "Predestination",
        "A top temporal agent pursues the one criminal that has "
        "eluded him throughout time",
        "R",
        "https://goo.gl/TVQdBW",
        "https://www.youtube.com/watch?v=-FcK_UiVV40")

coherence = media.Movie(
        "Coherence",
        "People deal with strange occurrences following a "
        "comet sighting",
        "PG",
        "https://goo.gl/FgwwhE",
        "https://www.youtube.com/watch?v=sEceDz1Rodc")

the_lives_of_others = media.Movie(
        "The Lives of Others",
        "An agent of the secret police becomes absorbed by the lives "
        "of those he surveils",
        "R",
        "https://goo.gl/WYT7Ii",
        "https://www.youtube.com/watch?v=n3_iLOp6IhM")

the_truman_show = media.Movie(
        "The Truman Show",
        "He's the star of the show but he doesn't know it",
        "PG",
        "https://goo.gl/JVc4Rs",
        "https://www.youtube.com/watch?v=loTIzXAS7v4")

eternal_sunshine_on_the_spotless_mind = media.Movie(
        "Eternal Sunshine on the Spotless Mind",
        "An estranged couple erase each other from their memories",
        "R",
        "https://goo.gl/BNcg0N",
        "https://www.youtube.com/watch?v=hj7Wgd_Yn94")

the_orphanage = media.Movie(
        "The Orphanage",
        "A woman brings her family back to her childhood home and "
        "her son disappears",
        "R",
        "https://goo.gl/cxVXdg",
        "https://www.youtube.com/watch?v=oXfHOY3CC0g")

the_shining = media.Movie(
        "The Shining",
        "A family stays at an isolated hotel where an evil presence "
        "influences them",
        "R",
        "https://goo.gl/1j0yYE",
        "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

howls_moving_castle = media.Movie(
        "Howl's Moving Castle",
        "An unconfident young woman is cursed with an old body by "
        "a spiteful witch",
        "PG",
        "https://goo.gl/8ZHm2F",
        "https://www.youtube.com/watch?v=iwROgK94zcM")

amelie = media.Movie(
        "Amelie",
        "Amelie is an innocent and naive girl in Paris who decides to "
        "help those around her",
        "R",
        "https://goo.gl/CST9QB",
        "https://www.youtube.com/watch?v=2UT5xaAfxWU")

the_gand_budapest_hotel = media.Movie(
        "The Grand Budapest Hotel",
        "The adventures of a legendary concierge and his "
        "most trusted friend",
        "R",
        "https://goo.gl/m8Nr13",
        "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

her = media.Movie(
        "Her",
        "A lonely writer develops an unlikely relationship with "
        "an operating system designed to meet his every need",
        "R",
        "https://goo.gl/KGu7Vp",
        "https://www.youtube.com/watch?v=WzV6mXIOVl4")

minority_report = media.Movie(
        "Minority Report",
        "A police officer from a special unit that predicts crimes "
        "is himself accused of a future murder",
        "PG-13",
        "https://goo.gl/G8xFDy",
        "https://www.youtube.com/watch?v=lG7DGMgfOb8")

equilibrium = media.Movie(
        "Equilibrium",
        "In a fascist future where all forms of feeling are illegal, "
        "a man in charge of enforcing the law rises "
        "to overthrow the system",
        "R",
        "https://goo.gl/s8lc65",
        "https://www.youtube.com/watch?v=raleKODYeg0")

twelve_angry_men = media.Movie(
        "Twelve Angry Men",
        "A jury holdout attempts to prevent a miscarriage of justice "
        "by forcing his colleagues to reconsider the evidence",
        "G",
        "https://goo.gl/Z3JdFC",
        "https://www.youtube.com/watch?v=fSG38tk6TpI")

oceans_eleven = media.Movie(
        "Ocean's Eleven",
        "Danny Ocean and his eleven accomplices plan to rob "
        "three Las Vegas casinos simultaneously",
        "PG-13",
        "https://goo.gl/n5Y7ST",
        "https://www.youtube.com/watch?v=imm6OR605UI")

movies = [the_machinist, predestination, coherence, the_lives_of_others,
          the_truman_show, eternal_sunshine_on_the_spotless_mind,
          the_orphanage, oceans_eleven, the_gand_budapest_hotel,
          her, equilibrium, amelie, the_shining, twelve_angry_men,
          howls_moving_castle]

fresh_tomatoes.open_movies_page(movies)
