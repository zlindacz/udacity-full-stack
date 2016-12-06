import media
import fresh_tomatoes

the_machinist = media.Movie("The Machinist",
                            "An insomniac machinist starts to question his sanity",
                            "R",
                            "https://upload.wikimedia.org/wikipedia/en/b/b9/The_Machinist_poster.JPG",
                            "https://www.youtube.com/watch?v=H0fuHY4U1UA")

predestination = media.Movie("Predestination",
                             "A top temporal agent pursues the one criminal that has eluded him throughout time",
                             "R",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Predestination_poster.jpg/220px-Predestination_poster.jpg",
                             "https://www.youtube.com/watch?v=-FcK_UiVV40")

coherence = media.Movie("Coherence",
                        "People deal with strange occurrences following a comet sighting",
                        "PG",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/Coherence_2013_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=sEceDz1Rodc")

the_lives_of_others = media.Movie("The Lives of Others",
                                  "An agent of the secret police becomes absorbed by the lives of those he surveils",
                                  "R",
                                  "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
                                  "https://www.youtube.com/watch?v=n3_iLOp6IhM")

the_truman_show = media.Movie("The Truman Show",
                              "He's the star of the show but he doesn't know it",
                              "PG",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Trumanshow.jpg/220px-Trumanshow.jpg",
                              "https://www.youtube.com/watch?v=loTIzXAS7v4")

eternal_sunshine_on_the_spotless_mind = media.Movie("Eternal Sunshine on the Spotless Mind",
                                                    "An estranged couple erase each other from their memories",
                                                    "R",
                                                    "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                                                    "https://www.youtube.com/watch?v=hj7Wgd_Yn94")

the_orphanage = media.Movie("The Orphanage",
                            "A woman brings her family back to her childhood home and her son disappears",
                            "R",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/2/2d/Elorfanato.jpg/220px-Elorfanato.jpg",
                            "https://www.youtube.com/watch?v=oXfHOY3CC0g")

the_shining = media.Movie("The Shining",
                          "A family stays at an isolated hotel where an evil presence influences them",
                          "R",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/The_Shining_poster.jpg/220px-The_Shining_poster.jpg",
                          "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

howls_moving_castle = media.Movie("Howl's Moving Castle",
                                  "An unconfident young woman is cursed with an old body by a spiteful witch",
                                  "PG",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/a/a0/Howls-moving-castleposter.jpg/220px-Howls-moving-castleposter.jpg",
                                  "https://www.youtube.com/watch?v=iwROgK94zcM")

amelie = media.Movie("Amelie",
                     "Amelie is an innocent and naive girl in Paris who decides to help those around her",
                     "R",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=2UT5xaAfxWU")

the_gand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                                      "The adventures of a legendary concierge and his most trusted friend",
                                      "R",
                                      "https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/The_Grand_Budapest_Hotel_Poster.jpg/220px-The_Grand_Budapest_Hotel_Poster.jpg",
                                      "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

her = media.Movie("Her",
                  "A lonely writer develops an unlikely relationship with an operating system designed to meet his every need",
                  "R",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Her2013Poster.jpg/220px-Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

minority_report = media.Movie("Minority Report",
                              "A police officer from a special unit that predicts crimes is himself accused of a future murder",
                              "PG-13",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Minority_Report_Poster.jpg/220px-Minority_Report_Poster.jpg",
                              "https://www.youtube.com/watch?v=lG7DGMgfOb8")

equilibrium = media.Movie("Equilibrium",
                          "In a fascist future where all forms of feeling are illegal, a man in charge of enforcing the law rises to overthrow the system",
                          "R",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Equilibriumposter.jpg/220px-Equilibriumposter.jpg",
                          "https://www.youtube.com/watch?v=raleKODYeg0")

twelve_angry_men = media.Movie("Twelve Angry Men",
                               "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence",
                               "G",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/12_angry_men.jpg/220px-12_angry_men.jpg",
                               "https://www.youtube.com/watch?v=fSG38tk6TpI")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "Danny Ocean and his eleven accomplices plan to rob three Las Vegas casinos simultaneously",
                            "PG-13",
                            "https://zuts.files.wordpress.com/2013/06/oceans-eleven-poster.jpeg",
                            "https://www.youtube.com/watch?v=imm6OR605UI")

movies = [the_machinist, predestination, coherence, the_lives_of_others,
          the_truman_show, eternal_sunshine_on_the_spotless_mind,
          the_orphanage, oceans_eleven, the_gand_budapest_hotel,
          her, equilibrium, amelie, the_shining, twelve_angry_men,
          howls_moving_castle]

fresh_tomatoes.open_movies_page(movies)
